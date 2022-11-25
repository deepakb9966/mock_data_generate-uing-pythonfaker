import connexion

from openapi_server.models.mockdata_create_post_request import MockdataCreatePostRequest  # noqa: E501

from openapi_server.run import run_command

from openapi_server.DB.main import db
import json


# from openapi_server.DB.min import ref


def mockdata_create_post(mockdata_create_post_request=None):  # noqa: E501
    """mockdata_create_post

     # noqa: E501

    :param mockdata_create_post_request: 
    :type mockdata_create_post_request: dict | bytes

    :rtype: Union[MockdataCreatePost201Response, Tuple[MockdataCreatePost201Response, int], Tuple[MockdataCreatePost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        mockdata_create_post_request = MockdataCreatePostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    type = mockdata_create_post_request.vital_type
    res = run_command(type)
    # print(res[1])
    try:
        if res[1] == 401:
            return "mockdata generator failed",401
        collection = db.collection('programmer_details')
        t = collection.document().set(res[0][0])
        return res[0][0]
    except:
        return "Something went wrong", 401


def mockdata_get_get(vital_type):  # noqa: E501
    """mockdata_get_get

     # noqa: E501

    :param vital_type: 
    :type vital_type: str

    :rtype: Union[MockdataCreatePost201Response, Tuple[MockdataCreatePost201Response, int], Tuple[MockdataCreatePost201Response, int, Dict[str, str]]
    """
    import json

    bp_data = open('/vitals/bp/bp_mock.json')
    pulse_data = open('/vitals/pulse/pulse_mock.json')
    temp_data = open('/vitals/temp/temp_mock.json')
    data_temp = json.load(temp_data)
    data_bp = json.load(bp_data)
    data_pulse = json.load(pulse_data)
    if vital_type == "temp":
        # ref.set(file_contents)
        return data_temp['FVNTu8vnH9QMLDH24CPGn7mm2In2']
    elif vital_type == "pulse":
        return data_pulse['FVNTu8vnH9QMLDH24CPGn7mm2In2']
    elif vital_type == "bp":
        return data_bp['FVNTu8vnH9QMLDH24CPGn7mm2In2']

    return {401: "user not found"}
