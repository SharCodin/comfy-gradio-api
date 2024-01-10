import json
import os
import time
import random


import numpy as np
import requests

from PIL import Image



URL = "http://127.0.0.1:8188/prompt"
INPUT_DIR = "D:/AI/01_ComfyUI_Testing/ComfyUI/input"
OUTPUT_DIR = "D:/AI/01_ComfyUI_Testing/ComfyUI/output"


def get_latest_image(folder):
    files = os.listdir(folder)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
    latest_image = os.path.join(folder, image_files[-1]) if image_files else None
    return latest_image


def start_queue(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    requests.post(URL, data=data)


def generate_image(promt):
    previous_image = get_latest_image(OUTPUT_DIR)
    start_queue(prompt)

    while True:
        latest_image = get_latest_image(OUTPUT_DIR)
        if latest_image != previous_image:
            return latest_image

        time.sleep(1)


with open("workflow_api.json", "r") as file_json:
    prompt = json.load(file_json)

for model in ["Model 1", "Model 2", "Model 3"]: # replace with model names like this: aniverse_thxEd14Pruned.safetensors
    for i in range(11): # replace with number of iteration
        prompt["4"]["inputs"]["ckpt_name"] = model # the values may be different based on your workflow
        merge_ratio = 0 + (i * 0.1)
        print(f"Merge Ratio: {merge_ratio}")
        prompt["10"]["inputs"]["ratio"] = merge_ratio # the values may be different based on your workflow
        generate_image(prompt)
        print(f"{i} - Completed...")

print("\n\nDONE.")