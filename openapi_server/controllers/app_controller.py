"""

Main code.

Gets the ML application and Updates it.

"""

from aiohttp import web

from openapi_server.models.ml_app import MLApp


async def get_ml_app_by_name(request: web.Request, appname) -> web.Response:
    """
    Get ML application by name.

    Some description of the operation. You can use &#x60;markdown&#x60; here.

    :param appname: The name that needs to be fetched
    :type appname: str

    """
    return web.Response(status=200)


async def update_ml_app(request: web.Request, appname, body) -> web.Response:
    """
    Update app.

    Update ML application by name.

    :param appname: The name that needs to be updated
    :type appname: str
    :param body: Updated user object
    :type body: dict | bytes

    """
    body = MLApp.from_dict(body)
    return web.Response(status=200)
