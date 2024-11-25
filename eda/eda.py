from datasets import load_dataset
import os
import matplotlib.pyplot as plt

def load_dataframe():
    dataset_repo = os.getenv('HF_DATASET_REPO')
    dataset = load_dataset(dataset_repo)
    df = dataset['train'].to_pandas()
    return df

def main():
    df = load_dataframe()

    # Remove specified columns
    columns_to_remove = ['image', 'category', 'language', 'country', 'published_at']
    df.drop(columns=columns_to_remove, inplace=True)

    # Print the modified DataFrame
    print(df)

    # Descriptive statistics
    print("\nDescriptive Statistics:")
    print(df.describe(include='all'))

    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Analyze and visualize the distribution of articles by source
    source_counts = df['source'].value_counts()
    print("\nDistribution of Articles by Source:")
    print(source_counts)
    plt.figure(figsize=(10, 6))
    source_counts.plot(kind='bar', title='Distribution of Articles by Source')
    plt.xlabel('Source')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Analyze and visualize the distribution of articles by author
    author_counts = df['author'].value_counts()
    print("\nDistribution of Articles by Author:")
    print(author_counts)
    plt.figure(figsize=(10, 6))
    author_counts.plot(kind='bar', title='Distribution of Articles by Author')
    plt.xlabel('Author')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Count the number of titles or descriptions containing "AI"
    ai_in_titles = df['title'].str.contains('AI', case=False, na=False).sum()
    ai_in_descriptions = df['description'].str.contains('AI', case=False, na=False).sum()
    total_ai_mentions = ai_in_titles + ai_in_descriptions
    print(f"\nNumber of article titles or descriptions containing 'AI': {total_ai_mentions}")

if __name__ == "__main__":
    main()