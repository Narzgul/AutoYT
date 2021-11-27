import praw
import my_secrets

num_comments = 20 # Number of comments to load

reddit = praw.Reddit(
    client_id = my_secrets.client_id,
    client_secret = my_secrets.secret,
    user_agent = my_secrets.user_agent
)

hot_posts = reddit.subreddit('AskReddit').hot(limit=15)

for post in hot_posts:
    if not post.over_18:
        print(post.title)
        # post.comments.replace_more()
        for comment in post.comments.list():
            print(comment.body)
            if num_comments == 0:
                break
            else: num_comments -= 1

        break