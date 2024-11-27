# News-Final-Project

## Dataset
The dataset is hosted on the Hugging Face Datasets Hub and can be accessed using the following link: [Tech News Dataset](https://huggingface.co/datasets/adityaraju26/tech-news-data). More information regarding the code and dataset can be found below.

## Pitch
[Final Dataset Presentation Pitch](https://drive.google.com/file/d/1ZzWCyE-OdBvWk6slbjajR5n_h4eZjKPL/view?usp=sharing)

## Program File Definitions
- **.github/workflows**: Contains the GitHub Actions workflow file for automated dataset updates.
- **eda**: Contains the exploratory data analysis (EDA) scripts and visualizations along with the respective unit tests.
- **dataset.py**: Contains the main script to fetch news data from the MediaStack API, process it, and update the dataset on Hugging Face.
- **requirements.txt**: Contains the required packages for the project.
- **test_dataset.py**: Contains the unit tests for the dataset.py script.
- **power_analysis.py**: Contains the power analysis script to calculate the sample size for the dataset.

## Problem
Tech enthusiasts often keep up with the latest industry developments by reading blogs and articles from various news outlets. However, these resources are scattered across multiple websites, making it difficult to locate.

## Overview
This project fetches news data from the MediaStack API, processes it, and updates a dataset on Hugging Face. The goal of this dataset is to consolidate technology-related articles from various news sources into a single platform, allowing enthusiasts to quickly and easily find content relevant to their interests.

## Tool(s) to source the data
MediaStack API to obtain data across news outlets

## Prior Datasets
There ar no prior datasets containing the same information as this one. There are similar ones such as an [IEEE Science and Tech Dataset](https://ieee-dataport.org/documents/science-and-tech-news-dataset) and [Global News](https://www.kaggle.com/datasets/everydaycodings/global-news-dataset), but none exclusive to recent technology news.

## Power Analysis
To complete the power analysis and establish the sample size of the dataset, we need to determine the effect size, significance level, and power of the test. The following are the values chosen:
- **Effect Size**: 0.5
- **Significance Level**: 0.05
- **Power**: 0.8

The 0.5 effect size was chosen as there is no pilot data or prior data to pick a more accurate effect size. It represents a moderate difference.
The 0.05 significance level is the standard value used in hypothesis testing. Finally, the power was set to 0.8 to ensure that the test has a high probability of detecting an effect if it exists.

We use the TTestIndPower in the statsmodels library to calculate the sample size using the information above. The package performs a two-sample independent t-test.

Once we pass the values into the function, we get a sample size of 64. This means that we need at least 64 samples in our dataset to achieve a power of 0.8 with a significance level of 0.05 and an effect size of 0.5. However,
since there is a limitation of fetching exactly 25 results from the API, we will round this up to 75 which explains the number of values in the dataset.

## Ethics Statement
This project consolidates technology-related articles from different news articles into a single dataset to facilitate easy access to technology content. The following are the methods used to maintain high ethical standards:
- **Data Privacy**: The data collected and processed in this project is sourced from publicly available news articles via an API. No personal or sensitive data is being collected or stored.
- **Non-Bias**: This data source does not particularly target or favor any specific news outlet. The data is collected from various sources to provide a comprehensive view of technology-related articles.
- **Transparency**: Transparency is maintained in our data collection processing methods. The source of the data is through the MediaStack API and the methods used to process and analyze the data are documented accurately.
- **Accuracy**: The information collected and analysis performed is accurate and reliable. Efforts are made to ensure that data is processed correctly and the generated visualizations are based on accurate data.

## Exploratory Data Analysis
Exploratory Data Analysis (EDA) is performed on the dataset to gain insights into the data collected. The analysis done in this project includes the following:
- **Missing Values in Dataset**: A bar chart showing the number of articles from each news source. From seeing this, we can identify that TechCrunch has the most articles in the dataset while Hacker News has the least. This is important to understand so we can assess each outlet and see if we need to add more articles from a specific source.
- **Number of articles containing "AI" in the title or description**: With there being 75 articles in the dataset, it was surprising to see that all 75 articles contain the phrase. I was particularly interested in this since as of recent, AI has been on various social media and news platforms and the insight gained from this operation supports that idea.
- ![Distribution of Articles by Source](eda/article_distribution.png)
- ![Distribution of Articles by Author](eda/author_distribution.png)

## Features
- Fetch news data from MediaStack API
- Process and clean the data
- Update the dataset on Hugging Face Datasets Hub
- Perform exploratory data analysis (EDA) with visualizations

## Requirements
- Python 3.8+
- pandas~=2.0.3
- datasets~=3.1.0
- huggingface-hub~=0.26.2
- pytest~=8.3.3
- matplotlib~=3.7.1

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/adityaraju926/News-Final-Project.git
    cd News-Final-Project
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Set the environment variables:
    ```sh
    export HF_DATASET_REPO=your_dataset_repo
    export HF_ACCESS_TOKEN=your_huggingface_token
    ```

2. Run the main script to fetch and update the dataset:
    ```sh
    python dataset.py
    ```

3. Perform EDA:
    ```sh
    python eda.py
    ```

## Testing
Run the tests using `pytest`:
```sh
pytest