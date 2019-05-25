import datetime

import praw

reddit = praw.Reddit(client_id='<id>', \
                     client_secret='<secret>', \
                     user_agent='Scraper')

team = input("Team: ")
new_posts = list(reddit.subreddit('SoccerBetting').new())

for submission in new_posts:
    submission.comments.replace_more(limit=0)
    comments = submission.comments.list()
    for comment in comments:
        if comment:
            cbody = comment.body
            if any(keyword.lower() in cbody.lower() for keyword in [team]):
                print("==========================================")
                for item in str(cbody).split("\n"):
                    if team.lower() in item.lower():
                        print(datetime.datetime.fromtimestamp(submission.created), " || ",
                              submission.title, " || ", item.strip())

print("\nGood luck")
