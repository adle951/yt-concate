from .step import Step
from yt_concate.model.found import Found

class Search(Step):
    def process(self, data, inputs, utils):
        search_item = inputs['search_item']
        founds = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if search_item in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    founds.append(f)
        print(len(founds))
