# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ml_app import MLApp


async def test_get_ml_app_by_name(client):
    """Test case for get_ml_app_by_name

    Get ML application by name
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mlapp/{appname}'.format(appname='appname_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_ml_app(client):
    """Test case for update_ml_app

    Updated app
    """
    body = {
  "appname" : "PlantClassificator",
  "entrypoint" : "plant_classificator",
  "methods" : "[\"predict\",\"train\"]",
  "contact" : "jane.doe@example.com"
}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/mlapp/{appname}'.format(appname='appname_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

