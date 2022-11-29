
import connexion

from openapi_server.models.mockdata_create_post_request import MockdataCreatePostRequest  # noqa: E501

from openapi_server.run import run_command

from openapi_server.DB.main import db

from openapi_server.dtjfyku import UploadJsonFileToFirestore


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
    type = str(mockdata_create_post_request.vital_type)
    patientId=str(mockdata_create_post_request.patientId)
    res = run_command(type)
    try:
        if res[1] == 401:
            return "mockdata generator failed", 404
        if type == "patient":
            try:
                uploadjson = UploadJsonFileToFirestore('set', type,'/home/deep/Desktop/mock_data_generator-main/vitals/patient/patient_mock.json')
                uploadjson.upload()
                return res
            except:
                return "mockdata generator failed", 404
        res = res["FVNTu8vnH9QMLDH24CPGn7mm2In2"]
        collection = db.collection("Patient").document(patientId).collection(type).document().set(res[0][0])
        return res[0][0]
    except:
        return "Something went wrong", 404


def mockdata_get_get(vital_type,patientId):  # noqa: E501
    """mockdata_get_get

     # noqa: E501

    :param vital_type:
    :type vital_type: str

    :rtype: Union[MockdataCreatePost201Response, Tuple[MockdataCreatePost201Response, int], Tuple[MockdataCreatePost201Response, int, Dict[str, str]]
    """
    try:
        collection = db.collection("Patient").document(patientId).collection(vital_type).get().to_dict()
        return collection
    except:
        return {404: "vital not found"}
