import json

import azure.functions as func

from config_loader import get_setting


def json_response(payload: dict, status_code: int = 200) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps(payload),
        status_code=status_code,
        mimetype="application/json"
    )


def main(req: func.HttpRequest) -> func.HttpResponse:
    greeting = get_setting("HTTP_GREETING", "Hello")
    name = req.params.get('name')

    if not name:
        try:
            req_body = req.get_json()
            name = req_body.get('name') if isinstance(req_body, dict) else None
        except ValueError:
            name = None

    if not name:
        name = "Maneesh"

    return json_response(
        {
            "message": f"{greeting}, {name}!",
            "name": name
        }
    )
