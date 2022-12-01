import os
import json
import sys


def run_command(self):
    cmd = os.system(
        "py generate.py -i ../vitals/{type} -r ../vitals/{type}/{type}_rules.json -o ../vitals/{type}/{type}_mock.json".format(
            type=self))

    if cmd:
        return "failed", 401
    else:
        vitals_path=r"C:\Users\deepa\Documents\GitHub\mock_data_generate-uing-pythonfaker\vitals"
        data = open(r"{path}\{type}\{type}_mock.json".format(path=vitals_path,type=self))
        d = json.load(data)
        return d, 201
