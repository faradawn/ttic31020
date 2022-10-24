import os
import json
import pandas as pd

def entrypoint(request_file_path: str):
    with open(request_file_path, 'r') as f:
        request = json.load(f)

    response = perform_main_business_logic(request)

    with open("response.json", "w") as outfile:
        json.dump(response, outfile, indent=4)

def perform_main_business_logic(input_request):
    print(input_request)
    data = {
        "name": "sathiyajith",
        "rollno": 56,
        "cgpa": 8.6,
        "phonenumber": "9976770500"
    }
    return data


if __name__ == "__main__":
    entrypoint("./tests/sample_request_1.json")
