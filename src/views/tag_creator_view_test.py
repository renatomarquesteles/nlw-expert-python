from unittest.mock import patch
from src.controllers.tag_creator_controller import TagCreatorController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.tag_creator_view import TagCreatorView

@patch.object(TagCreatorController, 'create')
def test_validate_and_create(mock_create):
    mock_product_code = "123"
    mock_request = HttpRequest(body={ "product_code": mock_product_code })
    mock_create.return_value = {
        "data": {
            "type": "Tag Image",
            "count": 1,
            "path": f'tags/{mock_product_code}.png'
        }
    }
    tag_creator_view = TagCreatorView()
    result = tag_creator_view.validate_and_create(mock_request)

    assert isinstance(result, HttpResponse)
    assert result.status_code == 200
    assert result.body == {
        "data": {
            "type": "Tag Image",
            "count": 1,
            "path": f'tags/{mock_product_code}.png'
        }
    }
