import os
import json
def run_command(self):
    if self == "temp":

        if (os.system(
                "python3 main.py -i ../vitals/temp -r ../vitals/temp/temp_rules.json -o ../vitals/temp/temp_mock.json")):

            return "failed",401
        else:
            temp_data = open('/home/deep/Desktop/mock_data_generator-main/vitals/temp/temp_mock.json')
            data_temp = json.load(temp_data)
            return data_temp["FVNTu8vnH9QMLDH24CPGn7mm2In2"], 201

    elif self == "bp":
        if (os.system(
                "python3 main.py -i ../vitals/bp -r ../vitals/bp/bp_rules.json -o ../vitals/bp/bp_mock.json")):
            return "failed",401
        else:
            bp_data = open('/home/deep/Desktop/mock_data_generator-main/vitals/bp/bp_mock.json')
            data_bp = json.load(bp_data)
            return data_bp["FVNTu8vnH9QMLDH24CPGn7mm2In2"], 201
    elif self == "pulse":
        if (os.system(
                "python3 main.py -i ../vitals/pulse -r ../vitals/pulse/pulse_rules.json -o ../vitals/pulse/pulse_mock.json")):
            return "failed",401
        else:
            pulse_data = open('/home/deep/Desktop/mock_data_generator-main/vitals/pulse/pulse_mock.json')
            data_pulse = json.load(pulse_data)
            return data_pulse["FVNTu8vnH9QMLDH24CPGn7mm2In2"], 201
    else:
        return "failed",401


count_num = [0]

# def return_count(count):
#     count_num.append(count)
#     print("count_para", count)
#     print('igfsjkbkj', type(count))


# count_num=5


# print(run_command("temp"))
# .__path__
# print(os.system("cd /home/deep/Desktop/mock_data_generator-main/server/openapi_server/mock_data"))
