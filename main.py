import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import pandas as pd


load_dotenv()
q = "Apple"
api_key= os.environ.get("yt-api")
APPLE_CHANNEL_ID = "UCE_M8A5yxnLfW0KghEeajjw"

youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.search().list(
    part="snippet", q=q,
    channelId=APPLE_CHANNEL_ID,
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
  
    # stats = item.get("statistics")
    # print(stats)
    # print("*"*100)
    # print(stat_response)
    pass

videos=[]
for item in stat_response.get("items", []):
    stats = item.get("statistics", {})
    video_id = item["id"]#["videoId"]
    title = item["snippet"]["title"]
    view = int(stats.get("viewCount", 0))
    likes = int(stats.get("likeCount", 0))
    comment = int(stats.get("commentCount", 0))
    channel = item["snippet"]["channelTitle"]
    publish_time = item["snippet"]["publishedAt"]

    videos.append({
        "title":title,
        "views":view,
        "likes":likes,
        "comments":comment,
        "published":publish_time

    })
    
    # print(f"Title: {title}")
    # print(f"Channel: {channel}")
    # print(f"Views: {view}")
    # print(f"Likes: {likes}")
    # print(f"Comments: {comment}")
    # print(f"URL: https://www.youtube.com/watch?v={video_id}")
    # print(f"Published: {publish_time}\n")

df = pd.DataFrame(videos)



total_views = df["views"].sum()
avg_views = df["views"].mean()
avg_likes = df["likes"].mean()
avg_comments = df["comments"].mean()
print("Total views:", total_views)
print("avg_views:", round(avg_views, 0))
print("avg_likes:", round(avg_likes, 0))
print("avg_comments:", avg_comments)
# df2 = pd.DataFrame([{"total_views":total_views, "avg_views":round(avg_views, 0)}])







