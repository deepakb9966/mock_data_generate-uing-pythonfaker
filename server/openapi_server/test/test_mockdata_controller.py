# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.message_dto import MessageDto  # noqa: E501
from openapi_server.models.mockdata_temp_create_post201_response import MockdataTempCreatePost201Response  # noqa: E501
from openapi_server.models.mockdata_temp_create_post_request import MockdataTempCreatePostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestMockdataController(BaseTestCase):
    """MockdataController integration test stubs"""

    def test_mockdata_temp_create_post(self):
        """Test case for mockdata_temp_create_post

        
        """
        mockdata_temp_create_post_request = openapi_server.MockdataTempCreatePostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/Mockdata_temp/create',
            method='POST',
            headers=headers,
            data=json.dumps(mockdata_temp_create_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
