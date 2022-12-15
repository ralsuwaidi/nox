from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
from slugify import slugify
import subprocess


MODEL_IDS = {
    "oj": "prompthero/openjourney",
    "sd1.5": "runwayml/stable-diffusion-v1-5",
    "sd2": "stabilityai/stable-diffusion-2-1",
    "comic": "ogkalu/Comic-Diffusion",
    "ink": "Envvi/Inkpunk-Diffusion",
    "samu": "Samdoesarts Ultmerge"
}


class AiModel:
    def __init__(self):
        self.model_id = ""

    def get_model(self, options):
        if "models" in options:
            self.model_id = MODEL_IDS[options["models"]]

            if options["models"] == "comic":
                self.response += """
                invoke keywords:
                >> charliebo artstyle
                >> holliemengert artstyle
                >> marioalberti artstyle
                >> pepelarraz artstyle
                >> andreasrocha artstyle
                >> jamesdaly artstyle

                """

            if options["models"] == "ink":
                self.response += """
                invoke keywords:
                >> nvinkpunk

                """ 

            if options["models"] == "samu":
                self.skip_gen = True
                self.response += """
                invoke keywords:
                >> samdoesarts style

                """ 

                
        if self.model_id == "":
            # if no model has been chosen go for default 
            self.model_id = MODEL_IDS["oj"]


    def gen_image(self, out_name=""):

        if not self.skip_gen:

            image_name = out_name or slugify(self.prompt[:10])

            pipe = StableDiffusionPipeline.from_pretrained(
                self.model_id, torch_dtype=torch.float16)
            pipe.scheduler = DPMSolverMultistepScheduler.from_config(
                pipe.scheduler.config)
            pipe = pipe.to("cuda")

            image = pipe(self.prompt, guidance_scale=self.guidance_scale,
                        num_inference_steps=self.num_inference_steps).images[0]
            image.save(f'{image_name}.png')

            return f'{image_name}.png'

        else:
            if self.model_id == "Samdoesarts Ultmerge":
               
                cmd = ["cd /home/rashed/dev/stable-diffusion && /home/rashed/miniconda3/bin/conda run -n ldm python /home/rashed/dev/stable-diffusion/scripts/txt2img.py --ckpt /home/rashed/dev/nox/models/samdoesartsUltmerge_v1.ckpt --prompt \"{}\" --plms --outdir \"/home/rashed/dev/nox/output\"".format(self.prompt)]
                process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                output, error = process.communicate()
            return 'output/grid-0000.png'



    @classmethod
    def show_ai_models(cls):
        all_options = ""
        for k,v in MODEL_IDS.items():
            all_options += f'{k}: {v}\n'
        
        return all_options