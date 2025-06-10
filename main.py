import streamlit as st
import os
import random
from PIL import Image

st.title("🖼️ Random Image Viewer with Copyable Filename")

# Path to image folder
img_folder = "img"

# Get list of supported image files
supported_exts = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"]
images = [file for file in os.listdir(img_folder) if os.path.splitext(file)[1].lower() in supported_exts]

# Shuffle image list
random.shuffle(images)

# Display images with copyable filename
for img_file in images:
    img_path = os.path.join(img_folder, img_file)
    image = Image.open(img_path)
    
    # Show image
    st.image(image, caption=img_file, use_container_width=True)
    
    # Copyable filename using st.code (click to copy)
    st.code(img_file, language="text")
    
    st.markdown("---")  # separator between images
