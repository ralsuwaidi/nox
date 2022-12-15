def improve_prompt(prompt, level="high"):

    detail_levels = {
        "high":  "highly detailed, realistic, unreal engine, octane render, vray, houdini render, quixel megascans, depth of field, 8k uhd, raytracing, lumen reflections, ultra realistic, cinema4d, studio quality",
        "alpha": "intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by gaston bussiere and alphonse mucha",
        "beta": "cinematic lighting, photorealistic, ornate, intricate, realistic, detailed, volumetric light and shadow, hyper HD, octane render, unreal engine insanely detailed and intricate, hypermaximalist",
        "gamma": "by tim okamura, victor nizovtsev, greg rutkowski, noah bradley. trending on artstation, 8k, masterpiece, graffiti paint, fine detail, full of color, intricate detail, golden ratio illustration",
    }

    return prompt.strip() + " " + detail_levels[level]


ALL_OPTIONS = {
    "n": "(int) repeat image gen with same settings n amount of times",
    "gs": "(int) set guidance scale",
    "steps": "(int) set number of steps",
    "models": "(str) choose from a preset saved model",
    "detailed": "(str) choose from preset saved prompts",
    "custom": "(str) choose from custom model (any diffuser model from huggingface"
}


class Options:

    def options(self, options):

        # choose the right model
        self.get_model(options)

        if "n" in options:
            self.repeat = int(options["n"])

        if "gs" in options:
            self.guidance_scale = int(options["gs"])

        if "steps" in options:
            self.num_inference_steps = int(options["steps"])

        if "custom" in options:
            self.model_id = options["custom"]

        if "detailed" in options:

            if options["detailed"] == "all":
                self.all_details = True
            else:
                self.prompt = improve_prompt(self.prompt, options["detailed"])

    def update_response(self):
        self.response += "\nguidance scale:" + str(self.guidance_scale)
        self.response += "\ninference steps:" + str(self.num_inference_steps)
        self.response += f'\nmodel: {self.model_id}'

    @classmethod
    def show_all_options(cls):
        all_options = ""
        for k,v in ALL_OPTIONS.items():
            all_options += f'{k}: {v}\n'
        
        return all_options
