from .step import Step

from moviepy.editor import VideoFileClip, concatenate_videoclips

class Edit_video(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            start, end = self.parse_caption_time(found.time)
            clip = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            clips.append(clip)
            if len(clips) >= inputs['limit']:
                break
        final_clip = concatenate_videoclips(clips)
        output_file_path = utils.get_output_video_path(inputs['channel_id'], inputs['search_item'])
        final_clip.write_videofile(output_file_path)

    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parse_time(start), self.parse_time(end)

    def parse_time(self, time):
        h, m, s = time.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms)/1000
