from apiclient.discovery import build
import settings
import datetime
import pytz

from matplotlib import pyplot as plt

youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

response = youtube.search().list(
part='snippet',
channelId=settings.NHK_CHANNEL_ID,
maxResults=50,
order='date'
).execute()

dict = {}
for item in response['items']:
    if '2020-12-31' in item['snippet']['publishedAt'] and '『' in item['snippet']['title']:
        video_id = item['id']['videoId']
        res = youtube.videos().list(part='statistics',id=video_id).execute()
        for video in res['items']:
            dict[item['snippet']['title']]=int(video['statistics']['viewCount'])

desc_list = sorted(dict.items(), reverse=True, key=lambda x:x[1])

labels = []
y = []
for title, count in desc_list:
    txt = title[7:]
    pos = txt.find('『')
    labels.append(txt[:pos])
    y.append(count)
    print(title + ": " + str(count))


x = list(range(1, len(labels) + 1))
plt.bar(x, y, align='center')
plt.xticks(x, labels, rotation='vertical')
now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
plt.xlabel('title')
plt.ylabel('count')
plt.title(now)
plt.tight_layout()
plt.savefig('plot.png')