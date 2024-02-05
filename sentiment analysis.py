from google.cloud import language_v1
import os
import pandas as pd

# Set the environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-account.json"

# Instantiates a client
client = language_v1.LanguageServiceClient()

def analyze_sentiment(text):
    # The text to analyze
    document = language_v1.types.Document(
        content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
    )

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    return sentiment

# Reviews data
reviews_data = [
    {
        'publishTime': '2023-11-12T19:48:55Z',
        'displayName': 'Taqiuddin Mohammed (Mo)',
        'originalText': 'The food was delicious n aromatic. Lamb Rogan josh was the best i ever had. Definitely recommend to try this.',
        'rating': 4
    },
    {
        'publishTime': '2023-02-19T02:34:14Z',
        'displayName': 'Jessica O',
        'originalText': 'Love me some Indian food and this place did not disappoint. Every single part of our meal was delicious, big portion sizes and lovely people to boot. Can’t recommend it enough!',
        'rating': 5
    },
    {
        'publishTime': '2023-12-01T23:34:03Z',
        'displayName': 'Sarah McLaren',
        'originalText': 'The best Indian food around! Delicious food, great value and amazing service. Locally owned small business with the kindest and most hospitable owner. Highly recommended.\nFlavours of India never disappoints :).',
        'rating': 5
    },
    {
        'publishTime': '2023-10-09T01:45:07Z',
        'displayName': 'Justin Petsinis',
        'originalText': 'A friend of mine brought home some curry chicken and rice. After a hour in the bag the food was still warm and delicious.',
        'rating': 5
    },
    {
        'publishTime': '2022-04-01T12:52:55Z',
        'displayName': 'Pradiptya Banerjee',
        'originalText': 'Tried for the first time, and have to say both the food and portion size were amazing! The Lamb Roganjosh stood out, as the meat was very tender… Overall absolutely great experience, will return soon!',
        'rating': 5
    }
]

# Create a dataframe
df = pd.DataFrame(reviews_data)

# Add columns for sentiment analysis
df['sentiment'] = df['originalText'].apply(lambda x: analyze_sentiment(x).score)
df['magnitude'] = df['originalText'].apply(lambda x: analyze_sentiment(x).magnitude)

# Display the dataframe
print(df)

# Save the DataFrame as a CSV file
df.to_csv("sentiment_analysis_results.csv", index=False)

# Compute average Sentiment and Magnitude
average_sentiment = df["sentiment"].mean()
average_magnitude = df["magnitude"].mean()

# Display the results
print("Average Sentiment:", average_sentiment)
print("Average Magnitude:", average_magnitude)