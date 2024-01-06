# Zero Shot Classification CLIP model

Source : [link](https://huggingface.co/docs/transformers/tasks/zero_shot_object_detection)

## Features
- Convert HuggingFace Model into TF Savedmodel format
- Preprocessed datasets
- Write REST API using Flask

## Requirements

Install the project dependencies
```bash
pip install requirements.txt 
```

## Usage
1. Download Necessary Models from[Drive](https://drive.google.com/drive/folders/11q-9LsGQLlhwEmv1zVItsH8qAkDlE87C?usp=drive_link).
- Consist of :
   - Models folder - Savedmodel in TF format
   - Tokenizer folder - Tokenizer (Text processor) json file saved from huggingface
   - image_processor folder - Image Processor json file saved from hugging face
- To obtain TF Savedmodel format - [ConvertCLIPtoTF](https://github.com/RobertBiehl/CLIP-tf2) 

2. Runnning the Flask API:
```python
python app.py
```

3. Making API Request
```
curl -X POST -H "Content-Type: application/json" -d '{"image_path": [...], "candidate_labels": [...]}' http://localhost:5000/predict
```
## Project Structure
```
app/
|--app.py
|--dto.py
|--model.py
|--utils.py
DTO/
|--request.json
|--response.json
hf_save/
|--image_processor/
|--models/
|--Tokrnixer/
```

