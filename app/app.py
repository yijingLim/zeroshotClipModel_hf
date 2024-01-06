# controller flask restful API
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import utils, model
from utils import *
from model import ZeroShotClipModel
from dto import RequestDTO, ResponseDTO


app = Flask(__name__)

# Test case
@app.route("/")
def hello_world():
    return "Hello, World!"

# @app.route('/predict0', methods=['POST'])
# def predict():
#     try:
#         # xx
#         data = request.get_json()
        
#         # Validate the input values
#         data = UserDTO.ValidateRequest(data)

#         # Access validated data
#         image = data['image']
#         labels = data['labels']

#         for image_path in image: 
#             # preprossed data
#             image_input = utils.preprocess_image(image_path)
#             text_input = utils.preprocess_text(labels)

#             # model
#             model_instance = ZeroShotClipModel()
#             tf_probs = model_instance.model_load(image_input, text_input)

#             prediction = [
#             {"label": labels, "score": str(round(score, 5)) }
#             for score, labels in sorted(zip(tf_probs, labels), key=lambda x: -x[0])
#             ]

#             # Combine with image urls and prediction
#             data = {'image_url': image_path, 'prediction': prediction}


#         # convert results to final i want
       
#         # return prediction
#         return jsonify(data=data)
#     except Exception as e:
#         return jsonify({'error': str(e)})


@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Accepting data from request...")
        data = request.get_json()

        # Validate request data
        requestdto = RequestDTO(data)
        validated_data = requestdto.ValidateRequest()
        print("Request data has been validated")
        
        # Access validated data
        image = validated_data['image']
        labels = validated_data['labels']

        final_results = []
        image_count = 0
        print("Modelling.....")
        for image_path in image:
            #  Increment count in each image
            image_count +=1
            # Predicting results with model
            model = ZeroShotClipModel()
            results = model.model_inferencing(image_path, labels)
            
            print(f"Image {image_count} processed successfully")

            # append all results into a list
            final_results.append(results)

        print("Model run has been completed and successful!", final_results)

        # Validate results
        response_dto = ResponseDTO(final_results)
        validated_results = response_dto.to_dict()
        print("Results has been validated")

        return jsonify(validated_results)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/testvalidateresponse', methods=['POST'])
def test():
    try:
        data = request.get_json()
        data = data.get("results",[])
        # print("hey", results)
        response_dto = ResponseDTO(data)
        final_results= response_dto.to_dict()
        print(final_results)

        return jsonify(final_results)
    except Exception as e:
        return jsonify({'error': str(e)})

# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 