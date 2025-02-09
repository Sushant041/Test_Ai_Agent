import pandas as pd
import os

from groq import Groq

client = Groq(
    # This is the default and can be omitted
    api_key="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",
)

# Read the CSV file with tweets
def load_tweets(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df['Text'].tolist()  # Assuming 'tweet' column holds the tweet text

# Send tweets to OpenAI for analysis
def analyze_tweets_with_openai(tweets):
    responses = []
    for tweet in tweets:
        # Construct the prompt to send to OpenAI
        prompt = f"Analyse this tweet.\n{tweet}\nIs the market sentiment in the tweet bullish or bearish for the mentioned cryptocurrency($XRP and $BTC)? Is the tweet indicating a potential buy signal for the mentioned cryptocurrency? Should one buy or sell the mentioned cryptocurrency based on the tweet?"

        try:
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            # print(response.choices[0].message.content.strip())
            analysis = response.choices[0].message.content.strip()
            responses.append((tweet, analysis))
        except Exception as e:
            responses.append((tweet, f"Error: {str(e)}"))
    
    return responses

# Output the analysis results
def output_results(results):
    for tweet, analysis in results:
        print(f"Tweet: {tweet}")
        print(f"Analysis: {analysis}\n")
    
# Full process
def OpenAi_call():
    # Provide your CSV path
    csv_file_path = "crypto_tweets.csv"
    
    # Load tweets from CSV
    tweets = load_tweets(csv_file_path)

    # Analyze tweets using OpenAI
    results = analyze_tweets_with_openai(tweets)
    
    # Output results
    output_results(results)
