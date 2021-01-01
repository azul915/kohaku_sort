from apiclient.discovery import build
import settings

from matplotlib import pyplot as plt

labels = ['鰯', '鯖', '秋刀魚', 'リュウグウノツカイ']
x = list(range(1, len(labels) + 1))
y = [1, 3, 5, 15]
plt.bar(x, y, align='center')
plt.xticks(x, labels, rotation='vertical')
plt.xlabel('魚の種類')
plt.ylabel('強さ (pt)')
plt.tight_layout()
plt.savefig('plot.png')

# youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

# response = youtube.search().list(
# part='snippet',
# channelId=settings.NHK_CHANNEL_ID,
# maxResults=50,
# order='date'
# ).execute()

# dict = {}
# for item in response['items']:
#     if '2020-12-31' in item['snippet']['publishedAt'] and '『' in item['snippet']['title']:
#         video_id = item['id']['videoId']
#         res = youtube.videos().list(part='statistics',id=video_id).execute()
#         for video in res['items']:
#             dict[item['snippet']['title']]=int(video['statistics']['viewCount'])

# desc_list = sorted(dict.items(), reverse=True, key=lambda x:x[1])

# for title, count in desc_list:
#     print(title + ": " + str(count))