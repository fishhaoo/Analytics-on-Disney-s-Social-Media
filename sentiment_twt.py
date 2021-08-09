from textblob import TextBlob
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import string
from nltk import FreqDist
from nltk import bigrams
import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean


# reading datasets
twt_master = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_twt/sharks_replies_twt.csv')


# dataset cleaning 
twt = twt_master[['Content']]

''' top words'''
def lemmatize_sentence(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else: 
            pos ='a'
        lemmatized_sentence.append(lemmatizer.lemmatize(word,pos))
    return lemmatized_sentence


def remove_noise(tweet_tokens, stop_words):
    cleaned_tokens = []
    for token in tweet_tokens:
        token = re.sub('http[s]', '', token) #remove https
        token = re.sub('//t.co/[A-Za-z0-9]+', '', token) # remove remaining link
        token = re.sub('(@[A-Za-z0-9_]+)', '', token) # remove mentions
        token = re.sub('[0-9]', '', token) #remove numbers
        if (len(token) > 3 ) and (token not in string.punctuation) and (token.lower() not in stop_words):
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

stop_words = stopwords.words('english')

twt_token = twt['Content'].apply(word_tokenize).tolist()


cleaned_tokens = []
for tokens in twt_token:
    rm_noise = remove_noise(tokens, stop_words)
    lemma_tokens = lemmatize_sentence(rm_noise)
    cleaned_tokens.append(lemma_tokens)
    
def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token
            
tokens_flat = get_all_words(cleaned_tokens)

#create counter of words in clean bigrams
freq_dist = FreqDist(tokens_flat)

#top 20 words
top_20 = freq_dist.most_common(20)
print(top_20)


''' bigrams '''
bigram_list = [list(bigrams(cmt)) for cmt in cleaned_tokens]

#flatten list of bigrams in clean tweets
bigrams_flat = get_all_words(bigram_list)

#create counter of words in clean bigra,s
freq_dist_bigrams = FreqDist(bigrams_flat)
print(freq_dist_bigrams.most_common(10))

#create network graph
network_token_df = pd.DataFrame(freq_dist_bigrams.most_common(50), columns=['token', 'count'])

bigrams_d = network_token_df.set_index('token').T.to_dict('records')

network_graph = nx.Graph()

#Create connections between nodes
for k, v in bigrams_d[0].items():
    network_graph.add_edge(k[0], k[1], weight=(v*10))
    
fig, ax = plt.subplots(figsize=(20, 17))

pos = nx.spring_layout(network_graph, k=1)

#plot networks
nx.draw_networkx(network_graph, pos,
                 font_size = 20,
                 node_size = 50, 
                 width =3, 
                 edge_color = 'grey', 
                 node_color = 'blue',
                 with_labels = True,
                 ax= ax)

''' 
sentiment analysis 
'''

text_blob = []
for cmt in twt['Content'].tolist():
    analysis = TextBlob(cmt)
    if analysis.sentiment.polarity == 0:
        sentiment = "Neutral"
    elif analysis.sentiment.polarity > 0:
        sentiment = "Positive"
    elif analysis.sentiment.polarity < 0:
        sentiment = "Negative"
    text_blob.append(sentiment)
    
twt['Sentiment'] = text_blob

polarity = []
subjectivity = []
for i, value in twt.iterrows():
    text = TextBlob(value['Content'])
    polarity.append(text.sentiment.polarity)
    subjectivity.append(text.sentiment.subjectivity)

c = list(zip(polarity, subjectivity))
c = pd.DataFrame(c, columns=['Polarity', 'Subjectivity'])
labelled_twt_replies = pd.concat([twt, c], axis=1)

m = []
m.append(mean(c['Polarity']))
m.append(mean(c['Subjectivity']))
m = pd.DataFrame(m)
m = m.rename(index={0: 'Polarity', 1: 'Subjectivity'})

# # sentiment counts
# twt_sent_count = twt['Sentiment'].value_counts()
# twt_sent_counts = pd.DataFrame(twt_sent_count, columns=['Sentiment'])
m.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_twt\results\shark_sent_average_twt.csv')
labelled_twt_replies.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_twt\results\shark_sent_twt.csv')