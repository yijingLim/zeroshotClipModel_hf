import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
import utils

class ZeroShotClipModel:
    def __init__(self):
        # intialise the model

        pass
    
    def model_load(self):
       # predict model value
        model_path = 'hf_save\models'
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(current_dir,model_path)

        model = keras.models.load_model(path)
        
        return model
    
    def model_inferencing(self, image_path, labels):
        # preprossed data
        image_input = utils.preprocess_image(image_path)
        text_input = utils.preprocess_text(labels)

        #  load model
        model = self.model_load()
        # Prediction uing loaded model
        logits_per_image, logits_per_text = model.predict((image_input, text_input))
        tf_probs = tf.nn.softmax(logits_per_image, axis=1)
        tf_probs = np.array(tf_probs)[0]

        prediction = [
            {"label": str(labels), "score": float(round(score, 5)) }
            for score, labels in sorted(zip(tf_probs, labels), key=lambda x: -x[0])
            ]

        # Combine with image urls and prediction
        data = {'image_url': image_path, 'prediction': prediction}

        # return value a image_path with their prediction
        return data 
