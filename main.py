import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
q = "Apple"
api_key= os.environ.get("yt-api")

youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.search().list(
    part="snippet", q=q,
    maxResults=10,
    type="video",
    order="relevance"

        )

response = request.execute()

# video_ids = [item["id"]["videoId"] for item in response.get("items", []) if "videoId" in item.get("id", {})]
video_ids = []
for item in response.get("items", []):
    if "videoId" in item.get("id", {}):
        video_ids.append(item["id"]["videoId"])

stat_request = youtube.videos().list(
    part="snippet,statistics",
    id=",".join(video_ids)
)

stat_response = stat_request.execute()

for item in stat_response.get("items"):
    # view = int(x["viewCount"])
    # like = int(x["likeCount"])
    # comment = int(x["commentCount"])
    stats = item.get("statistics")
    print(stats)

    # print(view, like, comment)
#print(stat_response)
for item in stat_response.get("items", []):
    stats = item.get("statistics")
    video_id = item["id"]["videoId"]
    title = item["snippet"]["title"]
    view = int(item["viewCount"])
    likes = int(item["likeCount"])
    comment = int(item["commentCount"])
    channel = item["snippet"]["channelTitle"]
    publish_time = item["snippet"]["publishedAt"]
    
    print(f"Title: {title}")
    print(f"Channel: {channel}")
    print(f"Views: {view}")
    print(f"Likes: {likes}")
    print(f"Comments: {comment}")
    print(f"URL: https://www.youtube.com/watch?v={video_id}")
    print(f"Published: {publish_time}\n")

