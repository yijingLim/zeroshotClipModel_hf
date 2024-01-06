class RequestDTO:
    def __init__(self,data):
         # initialise
         self.data = data

    def ValidateRequest(self):

        required_keys = ['image_path', 'candidate_labels']
        expected_types = {'image_path': list, 'candidate_labels': list}

    
        # Validate key values in Json data
        if not all(key in self.data for key in required_keys):
            raise ValueError(f"Missing required keys. Expected keys: '{required_keys}'")

        # Validate format types and value not none/empty
        for key,value_type in expected_types.items():
            if key in self.data:
                if self.data[key] is None or not self.data[key]:
                    raise ValueError(f"Value for '{key}' cannot be None")
                if not all(isinstance(self.data[key], list) for item in self.data[key]):
                    raise ValueError(f"All items in '{key}' must be string") 

        # return the value if validation pass
        return {'image': self.data['image_path'], 'labels': self.data['candidate_labels']}

# -----------------------------------Response DTO------------------------------

class PredictionDTO:
    def __init__(self,label,score):
        self.label = self.validate_label(label)
        self.score = self.validate_score(score)

    def validate_label(self, label):
        if label is None:
            raise ValueError(f"Label cannot be None")

        if not isinstance(label, str):
            raise ValueError(f"Label must be a string, but got {type(label).__name__}")
        return label

    def validate_score(self,score):
        if score is None:
            raise ValueError(f"Score cannot be None")
        if not isinstance(score, (float, str, int)):
             raise ValueError(f"Score must be a number or a string, but got {type(score).__name__}")
        return float(score) if isinstance(score, str) else score

    def to_dict(self):
        return{
            "label" : self.label,
            "score" : self.score
        }

class Image_urls_DTO:
    def __init__(self,image_url, prediction):
        self.image_url = self.validate(image_url)
        self.prediction = [PredictionDTO(**pred) for pred in prediction]

    def validate(self, image_url):

        if image_url is None: 
            raise ValueError(f"Value for Image URL cannot be None")
        if not isinstance(image_url, str):
            raise ValueError(f"Image_URL must be a string, but got {type(image_url).__name__}")
        return image_url
    
    def to_dict(self):
        return{
            "image_url": self.image_url,
            "prediction": [pred.to_dict() for pred in self.prediction]
        }

class ResponseDTO:
    def __init__(self, results):
        self.results = [Image_urls_DTO(**result) for result in results]
    
    def to_dict(self):
        return{
            "results": [result.to_dict() for result in self.results]
        }