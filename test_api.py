import json
import unittest


class APITestCase(unittest.TestCase):

    def input_json(self):
        request_json_filepath = "DTO/equest.json"
        # Load input data from a JSON file
        with open(request_json_filepath, 'r') as file:
            self.input_data = json.load(file)
        
    def test_predictAPI(self):

        # URL of model in Flask API
        api_url = "localhost"

        # Sample input data for testing
        input_data = self.input_json
        print(input_data)

if __name__ == ‘__main__’:
      unittest.main()
    

test_predictAPI()
