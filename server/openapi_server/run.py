import os
import json

from openapi_server.dtjfyku import UploadJsonFileToFirestore


def run_command(self):
    cmd = os.system(
        "python3 main.py -i ../vitals/{type} -r ../vitals/{type}/{type}_rules.json -o ../vitals/{type}/{type}_mock.json".format(
            type=self))

    if cmd:
        return "failed", 401
    else:
        data = open('/home/deep/Desktop/mock_data_generator-main/vitals/{type}/{type}_mock.json'.format(type=self))
        d = json.load(data)
        return d, 201
