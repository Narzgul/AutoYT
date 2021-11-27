import praw
from gtts import gTTS
import pathlib
import os
from mutagen.mp3 import MP3

import my_secrets

num_comments = 15 # Number of comments to load

title = ""
all_comments = []



# Fetching the Reddit comments

reddit = praw.Reddit(
    client_id = my_secrets.client_id,
    client_secret = my_secrets.secret,
    user_agent = my_secrets.user_agent
)

hot_posts = reddit.subreddit('AskReddit').hot(limit=10) # Loads 10 posts to filter out NSFW

for post in hot_posts:
    if not post.over_18: # Checks for NSFW
        title = post.title
        print(title)
        # post.comments.replace_more()
        for comment in post.comments.list():
            all_comments.append(comment.body)
            print(all_comments[-1])
            if num_comments == 0: # Limits to 15 comments
                break
            else: num_comments -= 1

        break



# Converting and saving the fetched data to audio:
#   Create folders for the outputs:
current_path = pathlib.Path().absolute()
output_path_audio = str(current_path) + "/output/" + title + "/audio"
output_path_video = str(current_path) + "/output/" + title + "/video"
os.makedirs(output_path_audio)
os.makedirs(output_path_video)

#   Save the title:
tts = gTTS(title)
tts.save(output_path_audio + "/title.mp3")

#   Save the comments:
for i, comment in enumerate(all_comments):
    tts = gTTS(comment)
    tts.save(output_path_audio + "/comment" + str(i) + ".mp3")



# Creating the Video:
#   Getting the combined audio length
total_audio_lenght = 0
for filename in os.listdir(output_path_audio):
    audio = MP3(output_path_audio + "/" + filename)
    total_audio_lenght += audio.info.length

print(total_audio_lenght)