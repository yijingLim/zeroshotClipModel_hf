# savimg Hugging face model

# convert pytorch CLIP model into Savedmodel TF format 
# https://github.com/RobertBiehl/CLIP-tf2/tree/d86dfd484e54183d9e060fb121fc575b708c7acb

# save processor from hugging face
from transformers import CLIPImageProcessor, CLIPTokenizerFast

checkpoint = "openai/clip-vit-large-patch14"

# Load Processor
image_processor = CLIPImageProcessor.from_pretrained(checkpoint)
tokenizer = CLIPTokenizerFast.from_pretrained(checkpoint)


# Save into config lightweight
image_processor.save_pretrained('Image_processor')
tokenizer.save_pretrained('Tokenizer')
