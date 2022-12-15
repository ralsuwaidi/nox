
from . import utils
from .helper.ai_models import AiModel
from .helper.option_helper import Options
from dataclasses import dataclass

@dataclass
class Txt2ImgModel:
    # https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion
    prompt: str
    guidance_scale: int
    num_inference_steps: int
    height: int
    width: int
    negative_prompt: str


class Txt2img(AiModel, Options):
    def __init__(self, prompt, model_sc=None):
        AiModel.__init__(self)
        self.prompt = prompt
        self.model_sc=model_sc
        self.guidance_scale = None
        self.num_inference_steps = None

        self.repeat = 1
        self.all_details = False
        self.special_gen = False

        self.response = ""
        self.model_id = None
        self.options = None

        self.init()

    def init(self):

        # save additional options from prompt
        if self.model_sc is not None:
            self.get_shortcut_model(self.model_sc)


        self.options = utils.get_opt(self.prompt)
        self.prompt = utils.remove_opt(self.prompt)

        self.get_model()
        self.parse_options()
        self.add_invoke()

        if self.model_id.endswith(".ckpt"):
            self.special_gen = True





