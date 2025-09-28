# import yt_dlp
# import time
# class YoutubeDownloader: 
#     def download_video(self, url, path="downloads"):
#         """Download YouTube video with retries if it fails mid-way."""

#         # ydl_opts = {
#         #     'outtmpl': f'{path}/%(title)s.%(ext)s',
#         #     'format': 'bestvideo+bestaudio/best',
#         #     'merge_output_format': 'mp4',
#         #     'http_chunk_size': 10 * 1024 * 1024,   # <--- add this
#         #     'postprocessors': [{
#         #         'key': 'FFmpegVideoConvertor',
#         #         'preferedformat': 'mp4',
#         #     }],
#         # }


#         ydl_opts = {
#             'outtmpl': f'{path}/%(title)s.%(ext)s',
#             'format': 'bestvideo+bestaudio/best',
#             'merge_output_format': 'mp4',
#             'http_chunk_size': 10 * 1024 * 1024,  # 10 MB chunks
#             'postprocessors': [{
#                 'key': 'FFmpegVideoConvertor',
#                 'preferedformat': 'mp4',
#             }],
#         }

#         for attempt in range(1, retries + 1):
#             try:
#                 with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                     info = ydl.extract_info(url, download=True)
#                     print(f"✅ Downloaded: {info.get('title')}")
#                     return  # success → exit function
#             except Exception as e:
#                 print(f"❌ Attempt {attempt} failed: {e}")
#                 if attempt < retries:
#                     print(f"🔁 Retrying in {delay} seconds...")
#                     time.sleep(delay)
#                 else:
#                     print("⚠️ All retries failed. Please try again later.")



#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=True)
#             print(f"Video Downloaded: {info.get('title')}")
#             print("downloaded the video.....")



#-----------------------------------------------------------------------------------------
import yt_dlp
import time
class YoutubeDownloader: 

    def download_video(self, url, path="."):
        try: 
            ydl_opts = {
                'outtmpl': f'{path}/%(title)s.%(ext)s',
                'format': 'bestvideo+bestaudio/best',   # best video + best audio
                'merge_output_format': 'mp4',           # force mp4 after merging
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4'             # ensure conversion to mp4
                }]
            }
            title = ""
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title')
                print(f"Downloaded: {title}")
                
            return title

        except Exception as e:
            print("unable to download yt video, error occured: ", e)

