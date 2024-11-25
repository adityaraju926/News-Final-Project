import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from eda.eda import load_dataframe, main

def create_mock_dataframe():
    return pd.DataFrame({
        'title': ['AI in healthcare', 'AI in finance'],
        'description': ['AI is transforming healthcare', 'AI is transforming finance'],
        'source': ['Source1', 'Source2'],
        'author': ['Author1', 'Author2'],
        'image': ['image1', 'image2'],
        'category': ['category1', 'category2'],
        'language': ['en', 'en'],
        'country': ['US', 'US'],
        'published_at': ['2023-01-01', '2023-01-02']
    })

@pytest.fixture
def mock_env_and_dataset():
    with patch('eda.os.getenv') as mock_getenv, patch('eda.load_dataset') as mock_load_dataset:
        mock_getenv.return_value = 'mock_repo'
        mock_dataset = MagicMock()
        mock_dataset['train'].to_pandas.return_value = create_mock_dataframe()
        mock_load_dataset.return_value = mock_dataset
        yield

def test_load_dataframe(mock_env_and_dataset):
    df = load_dataframe()
    assert len(df) == 2
    assert 'title' in df.columns

@pytest.fixture
def mock_dataframe():
    with patch('eda.load_dataframe') as mock_load_dataframe:
        mock_load_dataframe.return_value = create_mock_dataframe()
        yield

def test_main(mock_dataframe):
    with patch('builtins.print') as mocked_print, patch('matplotlib.pyplot.show'):
        main()
        assert mocked_print.called