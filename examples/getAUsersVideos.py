# NOTE: This python file cannot be run from the examples folder.
# It MUST BE in the same directory as tiktok.py is located!
# Yeah sorry, it's kind of annoying, but it's more organized this way.
from tiktok import TikTokapi

# Starts T
api = TikTokapi()

# The Number of trending TikToks you want to be displayed
results = 10

# The TikTok user's ID, can be found in the JSON from trending
id = "7119601"

trending = api.userPosts(id, results)

for tiktok in trending:
    # Prints the music play URL for the tiktok in trending
    print(tiktok['musicInfos']['playUrl'][0])

    # Prints the text of the tiktok
    print(tiktok['itemInfos']['text'])

print(len(trending))