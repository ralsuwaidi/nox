from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
from slugify import slugify
import subprocess
from ..constants import MODEL_IDS, INVOKE_CMDS


class AiModel:

    def get_model(self):
        """sets self.model depending on the prompt"""
        if "models" in self.options and self.model_id is not None:
            self.model_id = MODEL_IDS[self.options["models"]]

            if self.options["models"] == "comic":
                self.response += """
                invoke keywords:
                >> charliebo artstyle
                >> holliemengert artstyle
                >> marioalberti artstyle
                >> pepelarraz artstyle
                >> andreasrocha artstyle
                >> jamesdaly artstyle

                """

            if self.options["models"] == "samu":
                self.special_gen = True

                
        if self.model_id == None:
            # if no model has been chosen go for default 
            self.model_id = MODEL_IDS["oj"]

        self.add_response("model: " + self.model_id)

    def get_shortcut_model(self, shortcut):
        # populate self.model_id with shortcut model
        if shortcut in MODEL_IDS:
            self.model_id = MODEL_IDS[shortcut]


    def add_invoke(self):
        """add invoke if needed"""
        if self.model_id in INVOKE_CMDS:
            invoke_cmd = INVOKE_CMDS[self.model_id][0]
            self.prompt = f'{invoke_cmd} ' + self.prompt


    def gen_image(self, out_name=""):

        if not self.special_gen:

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
            prepare_cmd = "cd /home/rashed/dev/stable-diffusion && /home/rashed/miniconda3/bin/conda run -n ldm python /home/rashed/dev/stable-diffusion/scripts/txt2img.py --ckpt /home/rashed/dev/nox/models/"
            cmd = ["{}{} --prompt \"{}\" --plms --outdir \"/home/rashed/dev/nox/output\"".format(prepare_cmd, self.model_id,self.prompt)]
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            output, error = process.communicate()
            return 'output/grid-0000.png'



    @classmethod
    def show_ai_models(cls):
        all_options = ""
        for k,v in MODEL_IDS.items():
            all_options += f'{k}: {v}\n'
        
        return all_options