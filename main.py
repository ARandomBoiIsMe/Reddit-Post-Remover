import praw
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('details.ini')

    client_id = config['REDDIT']['CLIENT_ID']
    client_secret = config['REDDIT']['CLIENT_SECRET']
    password = config['REDDIT']['PASSWORD']
    username = config['REDDIT']['USERNAME_REDDIT']
    user_agent = config['REDDIT']['USER_AGENT']

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        password=password,
        username=username,
        user_agent=user_agent
    )

    subreddit_name = config['VARS']['SUBREDDIT_NAME']
    subreddit = reddit.subreddit(subreddit_name)

    posts = getPosts(subreddit)

    """
    Returns updated list of posts after each removal, 
    which removes, from the list, the objects of posts
    which have been removed from the subreddit.

    Proceeds to remove comments from remaining posts which contain the keywords.
    """
    keywords = config['VARS']['KEYWORDS'].split(',')
    posts = remove_by_post_title(posts, keywords)
    posts = remove_by_post_body(posts, keywords)
    remove_comments(posts, keywords)
    
    
def getPosts(subreddit):
    """
    Don't know why, but the results of subreddit.new() can only be used once.
    So I saved each post directly into a list to allow for reuse.
    """
    posts = []
    new_posts = subreddit.new()

    for post in new_posts:
        posts.append(post)
    
    return posts

def remove_by_post_title(posts, keywords):
    for post in posts:
        if any(item in post.title.lower() for item in keywords):
            post.mod.remove()
            posts.remove(post)
            print(f'Post removed due to title: {post.title}.')

    return posts

def remove_by_post_body(posts, keywords):
    for post in posts:
        if any(item in post.selftext.lower() for item in keywords):
            post.mod.remove()
            posts.remove(post)
            print(f'Post removed due to body: {post.title}.')

    return posts

def remove_comments(posts, keywords):
    for post in posts:
        post.comments.replace_more() # Handles extra comments that need to be loaded
        for comment in post.comments.list():
            if any(item in comment.body.lower() for item in keywords):
                comment.mod.remove()
                print(f'Comment removed: {comment.body}.')

main()
