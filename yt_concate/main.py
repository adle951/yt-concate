import getopt
import sys
sys.path.append('../')

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

    argv = sys.argv[1:]
    short_OPT = 'hc:s:l:'
    long_OPT = 'help channel_id= search_item= limit='.split()

    try:
        opts, args = getopt.getopt(argv, short_OPT, long_OPT)
        print(opts)
        print(args)
    except getopt.GetoptError:
        # Print a message or do something useful
        print('Something went wrong!')
        sys.exit(2)

    for key, content in opts:
        if key in ['-c', '--channel_id']:
            inputs['channel_id'] = content
        elif key in ['-s', '--search_item']:
            inputs['search_item'] = content
        elif key.isdigit():
            inputs['limit'] = content
        elif key in ['-h', '--help']:
            print('python command_arguement.py -u <username> -p <password>')
            sys.exit(0)


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


