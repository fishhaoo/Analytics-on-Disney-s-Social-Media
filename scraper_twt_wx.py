import snscrape.modules.twitter as sntwitter
import pandas as pd


''' 1. obtain replies in the form of tweets to disney '''

tweets_list1 = []
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('to:disneyplus').get_items()):
    if i>10000:
        break
    tweets_list1.append([tweet.url, tweet.date,  tweet.renderedContent, tweet.id, tweet.user, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.conversationId, tweet.hashtags])
    
# Creating a dataframe from the tweets list above 
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Link', 'Datetime', 'Content', 'Tweet Id', 'User', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'conversationId', 'hashtags'])


''' 2. obtain the tweets posted by disney to get the conversation id '''

tweets_list2 = []
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:disneyplus').get_items()):
    if i>40:
        break
    tweets_list2.append([tweet.url, tweet.date,  tweet.renderedContent, tweet.id, tweet.user, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.conversationId, tweet.hashtags])
    
# Creating a dataframe from the tweets list above 
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Link', 'Datetime', 'Content', 'Tweet Id', 'User', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'conversationId', 'hashtags'])



''' 3. append the replies/tweets that has the same conversation id as ori tweet into a new dataframe '''

# finding the replies to tweets using conversation id
jc =[]
for i in range(10001):
    if tweets_df1['conversationId'][i] == 1410276130586722309:
        jc.append(tweets_df1.loc[i])
        
simpsons =[]
for i in range(10001):
    if tweets_df1['conversationId'][i] == 1410236709351018502:
        simpsons.append(tweets_df1.loc[i])
        
sharks =[]
for i in range(10001):
    if tweets_df1['conversationId'][i] == 1409904506528145420:
        sharks.append(tweets_df1.loc[i])
        
        
jc_replies = pd.concat(jc, axis=1).T
simpsons_replies = pd.concat(simpsons, axis=1).T
sharks_replies = pd.concat(sharks, axis=1).T

''' 4. scrape the stats of the tweets '''

jc_stats_twt = tweets_df2.loc[tweets_df2['Tweet Id'] == 1410276130586722309]
jc_stats_twt = jc_stats_twt[['replyCount', 'retweetCount', 'likeCount']]

simpsons_stats_twt = tweets_df2.loc[tweets_df2['Tweet Id'] == 1410236709351018502]
simpsons_stats_twt = simpsons_stats_twt[['replyCount', 'retweetCount', 'likeCount']]

shark_stats_twt = tweets_df2.loc[tweets_df2['Tweet Id'] == 1409904506528145420]
shark_stats_twt = shark_stats_twt[['replyCount', 'retweetCount', 'likeCount']]

combined_stats_twt = pd.concat([jc_stats_twt, simpsons_stats_twt, shark_stats_twt], ignore_index=True)
combined_stats_twt = combined_stats_twt.rename(index={0:'JC', 1:'Simpsons', 2:'Shark'})
       
''' 5. final export '''        

# exporting to csv
tweets_df1.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_twt\all_twt_replies.csv')
tweets_df2.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_twt\all_disney_twt.csv')

jc_replies.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_twt\jc_replies_twt.csv')
simpsons_replies.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_twt\simpsons_replies_twt.csv')
sharks_replies.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_twt\sharks_replies_twt.csv')

jc_stats_twt.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_twt\results\jc_stats_twt.csv')
simpsons_stats_twt.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_twt\results\simpsons_stats_twt.csv')
shark_stats_twt.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_twt\results\shark_stats_twt.csv')

combined_stats_twt.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_twt\results\combined_stats_twt.csv')   
