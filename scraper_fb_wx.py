from facebook_scraper import get_posts
import pandas as pd
import numpy as np
 
listposts = []
for post in get_posts("disneyplus", pages=7, options={"comments": True}):
    print(post['text'][:50])
    listposts.append(post)
    
''' extract like, comment, share count from the returned data '''
# jc
jc_stats = []
jc_stats.append(listposts[14]['comments'])
jc_stats.append(listposts[14]['likes'])
jc_stats.append(listposts[14]['shares'])

jc_stats = pd.DataFrame(jc_stats).T
jc_stats = jc_stats.rename(columns = {0:'comment count', 1:'likes count', 2:'shares count'})


# simpsons
simpsons_stats = []
simpsons_stats.append(listposts[16]['comments'])
simpsons_stats.append(listposts[16]['likes'])
simpsons_stats.append(listposts[16]['shares'])

simpsons_stats = pd.DataFrame(simpsons_stats).T
simpsons_stats = simpsons_stats.rename(columns = {0:'comment count', 1:'likes count', 2:'shares count'})


# shark
shark_stats = []
shark_stats.append(listposts[23]['comments'])
shark_stats.append(listposts[23]['likes'])
shark_stats.append(listposts[23]['shares'])

shark_stats = pd.DataFrame(shark_stats).T
shark_stats = shark_stats.rename(columns = {0:'comment count', 1:'likes count', 2:'shares count'})


combined_stats_fb = pd.concat([jc_stats, simpsons_stats, shark_stats], ignore_index=True)
combined_stats_fb = combined_stats_fb.rename(index={0:'JC', 1:'Simpsons', 2:'Shark'})



# extract comments from the returned data
jc_comments = listposts[14]['comments_full']
jc2_comments = []
for i in range(29):
    jc2_comments.append(jc_comments[i]['comment_text'])
    
simpsons_comments = listposts[16]['comments_full']
simpsons2_comments = []
for i in range(30):
    simpsons2_comments.append(simpsons_comments[i]['comment_text'])

shark_comments = listposts[23]['comments_full']
shark2_comments = []
for i in range(30):
    shark2_comments.append(shark_comments[i]['comment_text'])
        
# exporting to csv
listposts_pd = pd.DataFrame(listposts)
listposts_pd.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_fb\all_fb_comment.csv')

jc2_comments_pd = pd.DataFrame(jc2_comments, columns=['Value'])
jc2_comments_pd.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_fb\jc_comment.csv')
jc_stats.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_fb\results\jc_stats_fb.csv')

simpsons2_comments_pd = pd.DataFrame(simpsons2_comments, columns=['Value'])
simpsons2_comments_pd.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_fb\simpsons_comment.csv')
simpsons_stats.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_fb\results\simpsons_stats_fb.csv')

shark2_comments_pd = pd.DataFrame(shark2_comments, columns=['Value'])
shark2_comments_pd.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_fb\shark_comment.csv')
shark_stats.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_fb\results\shark_stats_fb.csv')

combined_stats_fb.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_fb\results\combined_stats_fb.csv')