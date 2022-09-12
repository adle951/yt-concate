from yt_concate.pipeline.steps.step import StepException

class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        for step in self.steps:
            data = None
            try:
                data = step.process(data, inputs)
            except StepException as e:
                print('Exception happened at', e)
                break
