import os


def run_command(self):
    if self == "temp":

        if (os.system(
                "python3 main.py -i ../vitals/temp -r ../vitals/temp/temp_rules.json -o ../vitals/temp/temp_mock.json")):
            return {401: "failed"}
        else:
            return {201: "temperature data generated successfully"}

    elif self == "bp":
        if (os.system(
                "python3 main.py -i ../vitals/bp -r ../vitals/bp/bp_rules.json -o ../vitals/bp/bp_mock.json")):
            return {401: "failed"}
        else:
            return {201: "bp data generated successfully"}
    elif self == "pulse":
        if (os.system(
                "python3 main.py -i ../vitals/pulse -r ../vitals/pulse/pulse_rules.json -o ../vitals/pulse/pulse_mock.json")):
            return {401: "failed"}
        else:
            return {201: "pulse data generated successfully"}
    else:
        return {401: "not Found"}


count_num = [0]

# def return_count(count):
#     count_num.append(count)
#     print("count_para", count)
#     print('igfsjkbkj', type(count))


# count_num=5


# print(run_command("temp"))
# .__path__
# print(os.system("cd /home/deep/Desktop/mock_data_generator-main/server/openapi_server/mock_data"))
