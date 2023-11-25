# Python API for Comfy UI with Gradio

This repo contains the code from my YouTube tutorial on building a Python API to connect Gradio and Comfy UI for AI image generation with Stable Diffusion models.

## Tutorial Video

Here is the video walking through the code in this repo:

[YouTube link to tutorial video](https://youtu.be/yspMVTL08Rc)

## Overview

This project shows:

- How to connect a Gradio front-end interface to a Comfy UI backend
- Sending workflow data as API requests
- Updating generation parameters dynamically
- Displaying generated images in Gradio 
- Adding text and image inputs
- Using a smartphone camera for image inputs

By the end, you'll understand the basics of building a Python API and connecting a user interface with an AI workflow.

## Running the Code

To run the code:

1. Clone the repo
2. Install dependencies (`pip install requests Pillow gradio numpy`)
3. Modify the Comfy UI installation path
4. Open `python app.py` and modify the `INPUT_DIR` and `OUTPUT_DIR` folder path
5. Run `python app.py`
6. Open the localhost link to view in Gradio interface

The main files:

- `app.py` - Contains Gradio UI and API logic
- `workflow_api.json` - Saved Comfy UI workflow

Let me know if you have any other questions!

## Credits

Credit to my YouTube channel [Code Crafters Corner](https://www.youtube.com/channel/UCZGXfClJ2l8MP0l2bMbHa6w) for the original tutorial. Please subscribe there for more AI/coding videos.
