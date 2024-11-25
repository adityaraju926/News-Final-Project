import pytest
import json
import pandas as pd
from unittest.mock import patch, MagicMock
from dataset import fetch_news_data, create_dataframe

# Mock data for testing
mock_json_data = {
    "data": [
        {"title": "Tech News 1", "description": "Description 1"},
        {"title": "Tech News 2", "description": "Description 2"}
    ]
}

@pytest.fixture
def mock_http_response():
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(mock_json_data).encode('utf-8')
    return mock_response

def test_fetch_news_data(mock_http_response):
    with patch('http.client.HTTPConnection') as mock_http_conn:
        mock_conn_instance = mock_http_conn.return_value
        mock_conn_instance.getresponse.return_value = mock_http_response

        result = fetch_news_data()
        assert result == mock_json_data

def test_create_dataframe():
    df = create_dataframe(mock_json_data)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert list(df.columns) == ["title", "description"]

def test_create_dataframe_key_error():
    result = create_dataframe({})
    assert result is None