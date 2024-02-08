from src.errors.error_handler import handle_errors
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.views.http_types.http_response import HttpResponse

def test_handle_server_error():
    mock_error = Exception("test error")
    response = handle_errors(mock_error)
    assert isinstance(response, HttpResponse)
    assert response.status_code == 500
    assert response.body["errors"][0]["title"] == "Server error"
    assert response.body["errors"][0]["detail"] == "test error"

def test_handle_http_unprocessable_entity_error():
    mock_error = HttpUnprocessableEntityError("test error")
    response = handle_errors(mock_error)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 422
    assert response.body["errors"][0]["title"] == "UnprocessableEntity"
    assert response.body["errors"][0]["detail"] == "test error"
