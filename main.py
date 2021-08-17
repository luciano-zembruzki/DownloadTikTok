from TikTokApi import TikTokApi

api = TikTokApi.get_instance()

url = "<URL DO VÍDEO>"

video = api.get_video_by_url(url)

with open("video.mp4", "wb") as out:
    out.write(video)
