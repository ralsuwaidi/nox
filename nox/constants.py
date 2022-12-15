MODEL_IDS = {
    "oj": "prompthero/openjourney",
    "sd1.5": "runwayml/stable-diffusion-v1-5",
    "sd2": "stabilityai/stable-diffusion-2-1",
    "comic": "ogkalu/Comic-Diffusion",
    "ink": "Envvi/Inkpunk-Diffusion",
    "samu": "samdoesartsUltmerge_v1.ckpt"
}

GUIDANCE_SCALE_DEFAULT = 7
NUM_INFERENCE_STEPS_DEFAULT = 100

INVOKE_CMDS = {
    "Envvi/Inkpunk-Diffusion": ["nvinkpunk"],
    "samdoesartsUltmerge_v1.ckpt": ["samdoesarts style"],
    "ogkalu/Comic-Diffusion": [
                 "charliebo artstyle",
                 "holliemengert artstyle",
                 "marioalberti artstyle",
                 "pepelarraz artstyle",
                 "andreasrocha artstyle",
                 "jamesdaly artstyle",
    ],
}