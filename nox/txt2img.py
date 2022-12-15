
from . import utils
from .helper.ai_models import AiModel
from .helper.option_helper import Options

class Txt2img(AiModel, Options):
    def __init__(self, prompt):
        AiModel.__init__(self)
        self.prompt = prompt
        self.guidance_scale = 7
        self.num_inference_steps = 100

        self.repeat = 1
        self.all_details = False
        self.skip_gen = False

        self.response = ""

        self.init()

    def init(self):

        # save additional options from prompt
        options = utils.get_opt(self.prompt)
        # clean prompt
        self.prompt = utils.remove_opt(self.prompt)
        self.options(options)



