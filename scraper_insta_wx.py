from instascrape import Post
import pandas as pd

''' example 1 '''
# Instantiate the scraper objects 
igpost1 = Post('https://www.instagram.com/p/CQwEyiVsqLa/?utm_source=ig_web_copy_link')
# Scrape their respective data 
igpost1.scrape()

igpost2 = Post('https://www.instagram.com/p/CQvzQz3sUr3/?utm_source=ig_web_copy_link')
igpost2.scrape()

igpost3 = Post('https://www.instagram.com/p/CQtcM3MMLUY/?utm_source=ig_web_copy_link')
igpost3.scrape()


''' example 2'''
from instascrape import Profile
profile = Profile('disneyplus')
profile.scrape()


''' scraping, cleaning and exporting example 1 '''
# scraping for post jc
flat_json1 = igpost1.flat_json_dict
basename = "_node_text"
insta_comment1 = []
for i in range(96):
    current = str(i) + basename
    if current in flat_json1:
        insta_comment1.append(flat_json1[current])
    else:
        break

jc_stats_ig = []
jc_stats_ig.append(igpost1.comments)
jc_stats_ig.append(igpost1.likes)
jc_stats_ig = pd.DataFrame(jc_stats_ig).T
jc_stats_ig = jc_stats_ig.rename(columns = {0:'comment count', 1:'likes count'})


# scraping for post simpsons
flat_json2 = igpost2.flat_json_dict
basename = "_node_text"
insta_comment2 = []
for i in range(96):
    current = str(i) + basename
    if current in flat_json2:
        insta_comment2.append(flat_json2[current])
    else:
        break

simpsons_stats_ig = []
simpsons_stats_ig.append(igpost2.comments)
simpsons_stats_ig.append(igpost2.likes)
simpsons_stats_ig = pd.DataFrame(simpsons_stats_ig).T
simpsons_stats_ig = simpsons_stats_ig.rename(columns = {0:'comment count', 1:'likes count'})

    
# scraping for post shark    
flat_json3 = igpost3.flat_json_dict
basename = "_node_text"
insta_comment3 = []
for i in range(96):
    current = str(i) + basename
    if current in flat_json3:
        insta_comment3.append(flat_json3[current])
    else:
        break

shark_stats_ig = []
shark_stats_ig.append(igpost3.comments)
shark_stats_ig.append(igpost3.likes)
shark_stats_ig = pd.DataFrame(shark_stats_ig).T
shark_stats_ig = shark_stats_ig.rename(columns = {0:'comment count', 1:'likes count'})

combined_stats_ig = pd.concat([jc_stats_ig, simpsons_stats_ig, shark_stats_ig], ignore_index=True)
combined_stats_ig = combined_stats_ig.rename(index={0:'JC', 1:'Simpsons', 2:'Shark'})

''' cleaning and export '''
jc_ig_comment = pd.DataFrame(insta_comment1, columns=['Comments'])
jc_ig_comment.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_ig\jc_ig_comment.csv')
jc_stats_ig.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_ig\results\jc_stats_ig.csv')

simpsons_ig_comment = pd.DataFrame(insta_comment2, columns=['Comments'])
simpsons_ig_comment.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_ig\simpsons_ig_comment.csv')
simpsons_stats_ig.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_ig\results\simpsons_stats_ig.csv')

shark_ig_comment = pd.DataFrame(insta_comment3, columns=['Comments'])
shark_ig_comment.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_ig\shark_ig_comment.csv')
shark_stats_ig.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_ig\results\shark_stats_ig.csv')

combined_stats_ig.to_csv(r'D:\Program Files\Python\Social Media Analytics File\Assignment 2\com_ig\results\combined_stats_ig.csv')
