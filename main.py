from nox.txt2img import model_ids, gen_image, default_options

model_id = model_ids["oj"]
prompt = "store full of curious collectibles :: incredible, anime, Digital 2D, animated by Kyoto Animation, Studio Ghibli, Miyazaki, AKIRA art style, beautiful, gorgeous, dramatic lighting, rule of thirds, perfect composition, trending on ArtStation, 4k"

gen_image(model_id, prompt, default_options)