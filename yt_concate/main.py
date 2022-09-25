from yt_concate.utils import Utils
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_video import DownloadVideo
from yt_concate.pipeline.steps.edit_video import Edit_video
from yt_concate.pipeline.steps.postflight import Postflight

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_item': 'incredible',
        'limit': 20,
    }
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideo(),
        Edit_video(),
        Postflight(),

    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)

if __name__ == '__main__':
    main()


