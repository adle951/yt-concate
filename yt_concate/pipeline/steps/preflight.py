from .step import Step

class Preflight(Step):
    def process(self, data, input, utils):
        print('in preflight')
        utils.creat_dirs()
