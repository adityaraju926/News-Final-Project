import http.client
import json
import urllib.parse
import pandas as pd
import os
from datasets import Dataset, load_dataset
from huggingface_hub import HfFolder

def fetch_news_data():
    conn = http.client.HTTPConnection('api.mediastack.com')
    params = urllib.parse.urlencode({
        'access_key': 'ACCESS_KEY',
        'categories': 'technology',
        'sort': 'published_desc',
        'countries': 'us',
        'languages': 'en',
    })
    conn.request('GET', '/v1/news?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode('utf-8'))

def print_pretty_json(json_data):
    print(json.dumps(json_data, indent=4))

def create_dataframe(json_data):
    if 'data' in json_data:
        return pd.DataFrame(json_data['data'])
    else:
        print("Key 'data' not found in the response")
        return None

def update_huggingface_dataset(df):
    dataset_repo = os.getenv('HF_DATASET_REPO')
    hf_token = os.getenv('HF_ACCESS_TOKEN')
    HfFolder.save_token(hf_token)

    try:
        existing_dataset = load_dataset(dataset_repo)
        existing_df = existing_dataset['train'].to_pandas()
        updated_df = pd.concat([existing_df, df], ignore_index=True)
        updated_dataset = Dataset.from_pandas(updated_df)
        print("Dataset loaded and updated successfully")
    except Exception as e:
        updated_dataset = Dataset.from_pandas(df)
        print(f"Dataset not found, creating a new one: {e}")

    updated_dataset.push_to_hub(dataset_repo, token=hf_token)

def main():
    json_data = fetch_news_data()
    print_pretty_json(json_data)
    df = create_dataframe(json_data)
    if df is not None:
        print(df)
        update_huggingface_dataset(df)

if __name__ == "__main__":
    main()