import os
import json



def run_command(self):
    cmd = os.system(
        "py main.py -i ../vitals/{type} -r ../vitals/{type}/{type}_rules.json -o ../vitals/{type}/{type}_mock.json".format(
            type=self))

    if cmd:
        return "failed", 401
    else:
        data = open(r"C:\Users\deepa\Documents\GitHub\mock_data_generate-uing-pythonfaker\vitals\{type}\{type}_mock.json".format(type=self))
        d = json.load(data)
        return d, 201
