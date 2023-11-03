import json
import os
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from googleapiclient.discovery import build
import re

CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
YOUTUBE_API_KEY = os.environ["YOUTUBE_API_KEY"]
NOT_GET_VIDEO_ERROR_MESSAGE = "YoutubeのShort動画を共有してください"
NOT_GET_URL_ERROR_MESSAGE = "動画本編のURLを取得できませんでした"

def lambda_handler(event, context):
    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    
    try:
        body = json.loads(event["body"])
        reply_token = body["events"][0]["replyToken"]
        short_url = body["events"][0]["message"]["text"]
        video_id = re.search(r'\/([^/?]+)\?', short_url).group(1)

        request = youtube.commentThreads().list(
            part = 'snippet',
            videoId = video_id,
            order = 'relevance',
            maxResults = 1
        )
        
        response = request.execute()
    except:
        line_bot_api.reply_message(reply_token, TextSendMessage(text=NOT_GET_VIDEO_ERROR_MESSAGE))
        return {
            'statusCode' : 400,
            'body' : json.dumps('NotGetVideoError')
        }

    comment = response['items'][0]['snippet']['topLevelComment']['snippet']['textDisplay']
    urls = re.findall(r'https://youtu.be/[A-Za-z0-9]*', comment)
    if len(set(urls)) == 1:
        url = urls[0]
    else :
        line_bot_api.reply_message(reply_token, TextSendMessage(text=NOT_GET_URL_ERROR_MESSAGE))
        return {
            'statusCode' : 400,
            'body' : json.dumps('NotFoundUrl')
        }

    try:
        line_bot_api.reply_message(reply_token, TextSendMessage(text=url))
    except LineBotApiError as e:
        return {
            'statusCode' : 500,
            'body' : json.dumps(e.message)
        }
    
    return {
        'statusCode' : 200,
        'body' : json.dumps('success')
    }
