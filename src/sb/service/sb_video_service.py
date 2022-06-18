import urllib.parse
import urllib.request
import uuid
import requests
from moviepy.editor import *
import re


def get_random_int():
    return str(uuid.uuid4().fields[5])


def merge_video(video_path_1: str, video_path_2: str, merged_video: str):
    video_1 = VideoFileClip(video_path_1)
    video_2 = VideoFileClip(video_path_2)
    promo_resized = video_2.resize(width=video_1.size[0])
    merged_ht_video = concatenate_videoclips([promo_resized, video_1], method='compose')
    merged_ht_video.write_videofile(
        merged_video, fps=30, temp_audiofile="tmp_audio.m4a", remove_temp=True, audio_codec="aac")


def get_xvideo_url(xvideo_url: str):
    if '/' in xvideo_url:
        xvideo_url = urllib.parse.quote(xvideo_url, safe='')

    download_site = 'https://www.tubeoffline.com/downloadFrom.php?host=Xvideos&slct=Normal&slct2=MP4&video='
    download_url = download_site + xvideo_url

    session = requests.Session()
    session.get('https://www.tubeoffline.com/download-Xvideos-videos.php')

    result = requests.get(download_url, cookies=session.cookies.get_dict())

    video_url = re.findall(
        r'(?<=<a href=")([^\n]*mp4[^\n]*)(?=" rel="noreferrer nofollow noopener" target="_blank" download>DOWNLOAD<\/a>)',
        result.text)[0]
    while '<a href="' in video_url:
        video_url = video_url.partition('<a href="')[2]

    return video_url


def download_from_url(from_url: str, to_file: str):
    with open(to_file, "wb") as f:
        print("Downloading %s" % to_file)
        response = requests.get(from_url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                sys.stdout.flush()


def combine_xvideo(base_location, promo_file, video_file, merged_file):
    merge_video(
        base_location + video_file,
        base_location + promo_file,
        base_location + merged_file
    )
