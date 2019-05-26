import datetime
from datetime import datetime, timedelta

import praw

reddit = praw.Reddit(client_id='WMX9GgDwAmbZ5Q',
                     client_secret='RIHACIOMK04v7hOZgP_of2f2ZII',
                     user_agent='Scraper')

teams = input("Team: ").lower().split(" ")
# team = "torino"
new_posts = list(reddit.subreddit('SoccerBetting').new(limit=1000))


def filter_last_week(s):
    week = datetime.utcnow() - timedelta(hours=168)
    return datetime.fromtimestamp(s) >= week


def print_entry():
    for item in str(body).split("\n"):
        for t in teams:
            if t.lower() in item.lower():
                print(datetime.fromtimestamp(submission.created), " || ",
                      submission.title, " || ",
                      str(item).lower().replace(str(t), '\x1b[4;30;47m' + t + '\x1b[0m'))
    print("More: " + "https://www.reddit.com" + submission.permalink + str(comment))


for submission in new_posts:
    if filter_last_week(submission.created):
        submission.comments.replace_more(limit=0)
        comments = submission.comments.list()
        for comment in comments:
            if comment:
                body = comment.body
                if any(keyword.lower() in body.lower() for keyword in teams):
                    print("=======================================================================================")
                    print_entry()

print("\nGood luck :)")
