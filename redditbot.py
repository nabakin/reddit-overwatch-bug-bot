from urllib import quote_plus

import praw, time

KEYWORDS = ['bug', 'glitch']
REPLY_TEMPLATE = "Hey I noticed you have found a bug!  If you haven't already, I would highly recommend putting it on the Overwatch Forums [here](https://us.battle.net/forums/en/overwatch/22813881/) because there's no guarantee the Overwatch Devs will see it over here on reddit.\n\nHow did I do?  Were you posting about a bug?  Feel free to pm this account for feedback.  Thanks! \n\n*****\n\n*bot created by /u/nabakin*"

reddit = praw.Reddit(user_agent='OverwatchBugBot (by /u/nabakin)',
                    client_id='CLIENT_ID', client_secret='CLIENT_SECRET',
                    username='OverwatchBugBot', password='PASSWORD')

def main():
    subreddit = reddit.subreddit('Overwatch')
    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):
    normalized_title = submission.title.lower()
    for keyword in KEYWORDS:
        if keyword in normalized_title:
            url_title = quote_plus(submission.title)
            reply_text = REPLY_TEMPLATE.format(url_title)
            print('Replying to: {}'.format(submission.title))
            submission.reply(reply_text)
            print('Posts left: {}'.format(reddit.auth.limits))
            break


main()
