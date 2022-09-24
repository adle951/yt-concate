import os

from yt_concate.setting import DOWNLOADS_DIR
from yt_concate.setting import VIDEOS_DIR
from yt_concate.setting import CAPTIONS_DIR


class Utils:
    def __init__(self):
        pass

    def get_video_list_file_path(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_file_path(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def creat_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)


    def caption_file_exists(self, yt):
        path = yt.caption_filepath
        return os.path.exists(path) and os.path.getsize(path) > 0
