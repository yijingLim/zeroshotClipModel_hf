# save helper functions
from PIL import Image
from transformers import CLIPImageProcessor, CLIPTokenizerFast
import numpy as np
import requests, os

image_processor_path = "hf_save\Image_processor"
tokenizer_path = "hf_save\Tokenizer"

current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_processor_path = os.path.join(current_dir,image_processor_path)
tokenizer_path = os.path.join(current_dir,tokenizer_path)

# ---------------------- Funcitons -------------------
def preprocess_image(image_path):
    # Perform  preprocessing on image
    image_processor = CLIPImageProcessor.from_pretrained(image_processor_path)
    image = Image.open(requests.get(image_path, stream=True).raw) #URL or #local image - Image.open(image)
    images = image_processor(images=image)
    image_array = np.array(images['pixel_values'][0])  # shape = (1,3, 224, 224)
    image_array = np.expand_dims(image_array,axis= 0) #unsquueze(0)
    reshape_image = np.moveaxis(image_array, [0,1,2,3], [0,3,1,2]) #shape = (1,224,224,3) permute

    return reshape_image

def preprocess_text(candidate_labels):
    # Perform  preprocessing(tokenization) on text
    text_tokenizer = CLIPTokenizerFast.from_pretrained(tokenizer_path)

    tokenized_text = text_tokenizer(candidate_labels)
    text_array = np.array(tokenized_text['input_ids'])
    text_array = np.pad(text_array, [(0,0),(0,77-3)], mode ='constant', constant_values =0)     # Fill up the space to fit the size [4,77]
    reshape_text = np.expand_dims(text_array, axis = 0).astype(np.int32)

    return reshape_text


