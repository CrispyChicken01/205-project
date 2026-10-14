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

video_ids = [for item in response.get("items", [])]


for item in response.get("items", []):
    video_id = item["id"]["videoId"]
    title = item["snippet"]["title"]
    channel = item["snippet"]["channelTitle"]
    publish_time = item["snippet"]["publishedAt"]
    
    print(f"Title: {title}")
    print(f"Channel: {channel}")
    print(f"URL: https://www.youtube.com/watch?v={video_id}")
    print(f"Published: {publish_time}\n")

