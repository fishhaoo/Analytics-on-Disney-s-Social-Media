import pandas as pd
import matplotlib.pyplot as plt

''' importing datasets '''
# twitter
twt_jc_sent = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_twt/results/jc_sent_average_twt.csv')
twt_shark_sent = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_twt/results/shark_sent_average_twt.csv')
twt_simpsons_sent = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_twt/results/simpsons_sent_average_twt.csv')
twt_combined_stats = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_twt/results/combined_stats_twt.csv')


# facebook 
fb_jc_sent = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_fb/results/jc_sent_average_fb.csv')
fb_shark_sent = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_fb/results/shark_sent_average_fb.csv')
fb_simpsons_sent = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_fb/results/simpsons_sent_average_fb.csv')
fb_combined_stats = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_fb/results/combined_stats_fb.csv')

#instagram
ig_jc_sent = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_ig/results/jc_sent_average_ig.csv')
ig_shark_sent = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_ig/results/shark_sent_average_ig.csv')
ig_simpsons_sent = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_ig/results/simpsons_sent_average_ig.csv')
ig_combined_stats = pd.read_csv('D:/Program Files/Python/Social Media Analytics File/Assignment 2/com_ig/results/combined_stats_ig.csv')


''' dataset manipulation '''
# rename
twt_jc_sent = twt_jc_sent.rename(columns={'Unnamed: 0': 'Subject', '0': 'Score'})
twt_shark_sent = twt_shark_sent.rename(columns={'Unnamed: 0': 'Subject', '0': 'Score'})
twt_simpsons_sent = twt_simpsons_sent.rename(columns={'Unnamed: 0': 'Subject', '0': 'Score'})
twt_combined_stats = twt_combined_stats.rename(columns={'Unnamed: 0': 'Post', 'replyCount': 'comment count', 'retweetCount': 'shares count', 'likeCount': 'likes count'})

fb_jc_sent = fb_jc_sent.rename(columns={'Unnamed: 0': 'Subject', '0': 'Score'})
fb_shark_sent = fb_shark_sent.rename(columns={'Unnamed: 0': 'Subject', '0': 'Score'})
fb_simpsons_sent = fb_simpsons_sent.rename(columns={'Unnamed: 0': 'Subject', '0': 'Score'})
fb_combined_stats = fb_combined_stats.rename(columns={'Unnamed: 0': 'Post'})


ig_jc_sent = ig_jc_sent.rename(columns={'Unnamed: 0': 'Subject', '0': 'Score'})
ig_shark_sent = ig_shark_sent.rename(columns={'Unnamed: 0': 'Subject', '0': 'Score'})
ig_simpsons_sent = ig_simpsons_sent.rename(columns={'Unnamed: 0': 'Subject', '0': 'Score'})
ig_combined_stats = ig_combined_stats.rename(columns={'Unnamed: 0': 'Post'})


# assign a grouping for them 
twt_jc_sent['Group'] = 'Twitter'
twt_shark_sent['Group'] = 'Twitter'
twt_simpsons_sent['Group'] = 'Twitter'
twt_combined_stats['Group'] = 'Twitter'

fb_jc_sent['Group'] = 'Facebook'
fb_shark_sent['Group'] = 'Facebook'
fb_simpsons_sent['Group'] = 'Facebook'
fb_combined_stats['Group'] = 'Facebook'


ig_jc_sent['Group'] = 'Instagram'
ig_shark_sent['Group'] = 'Instagram'
ig_simpsons_sent['Group'] = 'Instagram'
ig_combined_stats['Group'] = 'Instagram'

# combine them according to posts
combined_jc = pd.concat([twt_jc_sent, fb_jc_sent, ig_jc_sent])
combined_simpsons = pd.concat([twt_simpsons_sent, fb_simpsons_sent, ig_simpsons_sent])
combined_shark = pd.concat([twt_shark_sent, fb_shark_sent, ig_shark_sent])

# combine datasets according to like, share, comment count
combined_stats_all = pd.concat([twt_combined_stats, fb_combined_stats, ig_combined_stats])
likes = combined_stats_all[['Post', 'likes count', 'Group']]
comment = combined_stats_all[['Post', 'comment count', 'Group']]
share = combined_stats_all[['Post', 'shares count', 'Group']]



''' plotting '''

combined_jc.groupby(['Group','Subject']).sum().unstack().plot(kind='bar')
combined_simpsons.groupby(['Group','Subject']).sum().unstack().plot(kind='bar')
combined_shark.groupby(['Group','Subject']).sum().unstack().plot(kind='bar')

likes.groupby(['Group','Post']).sum().unstack().plot(kind='bar')
comment.groupby(['Group','Post']).sum().unstack().plot(kind='bar')
share.groupby(['Group','Post']).sum().unstack().plot(kind='bar')





