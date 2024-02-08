from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView
from src.errors.error_handler import handle_errors

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])

def create_tag():
    http_response = None
    try:
        tag_creator_view = TagCreatorView()
        http_request = HttpRequest(body=request.json)
        http_response = tag_creator_view.validate_and_create(http_request)
    except Exception as error:
        http_response = handle_errors(error)

    return jsonify(http_response.body), http_response.status_code
