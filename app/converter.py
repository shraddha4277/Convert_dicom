# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TC_2QMXWeUwoESA-ptJbM2DXWdx9hKG6
"""

import os
import pydicom
from PIL import Image
import numpy as np

# Function to convert DICOM to JPEG
def convert_dicom_to_jpg(dicom_path, jpg_path):
    dicom = pydicom.dcmread(dicom_path)
    img = dicom.pixel_array

    # Convert 16-bit grayscale to 8-bit
    img_scaled = np.uint8(img / np.max(img) * 255)  # Scale and convert to 8-bit

    img_mem = Image.fromarray(img_scaled)  # Create image from scaled array
    img_mem.save(jpg_path)

# # Path to the folder containing DICOM files
# dicom_folder = '/content/drive/MyDrive/ARJUN YADAV  35YM_36263_115723/ARJUN YADAV  35YM_36263_115723/1.0_Thin_CONTRAST_121050_302'

# # Path to save JPG files
# jpg_folder = '/content/drive/MyDrive/output5'

# # Create output folder if it doesn't exist
# os.makedirs(jpg_folder, exist_ok=True)

# # Iterate through each file in the DICOM folder
# for filename in os.listdir(dicom_folder):
#     if filename.endswith(".dcm"):
#         dicom_path = os.path.join(dicom_folder, filename)
#         jpg_path = os.path.join(jpg_folder, filename.replace('.dcm', '.jpg'))
#         convert_dicom_to_jpg(dicom_path, jpg_path)

# print("Conversion complete.")

