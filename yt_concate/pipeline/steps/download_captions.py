from pytube import YouTube

from .step import Step
from .step import StepException
import time

class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start_time = time.time()
        for yt in data:
            if utils.caption_file_exists(yt):
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                # print(en_caption_convert_to_srt)
            except AttributeError:
                print('AttributeError when downloading caption for', yt.url)
                continue
            text_file = open(yt.caption_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        end_time = time.time()
        print('took', end_time - start_time, 'seconds')
        return data


