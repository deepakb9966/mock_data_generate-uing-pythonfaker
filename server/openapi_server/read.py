import json

bp_data = open('/workspaces/mock_data_generate-uing-pythonfaker/vitals/bp/bp_mock.json')
pulse_data = open('/workspaces/mock_data_generate-uing-pythonfaker/vitals/pulse/pulse_mock.json')
temp_data = open('/workspaces/mock_data_generate-uing-pythonfaker/vitals/temp/temp_mock.json')


# Iterating through the json
# list
data_temp = json.load(temp_data)
data_bp = json.load(bp_data)
data_pulse = json.load(pulse_data)

def get_data(vital):
    if vital == "temp":
        return data_temp
    elif vital == "pulse":
        return data_pulse
    elif vital == "bp":
        return data_bp
    else:
        return 0
