import pandas as pd
from transformers import pipeline
import os

def run_sentiment_analysis():
    print('--Starting AI Sentiment Analysis--')

    #1 Check if the raw data file exists
    input_file='data/raw_headlines.csv'
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found. Run ingest.py first!")
        return
    
    #2 Load the data
    df = pd.read_csv(input_file)
    if df.empty:
        print("❌ Error: No data in csv file")
        return
    
    #3 Load the AI model (This is the 'Inference' part)
    # We use 'distilbert-base-uncased-finetuned-sst-2-english' 
    # It is fast and accurate for sentiment.
    print("Loading AI model...")
    classifier = pipeline('sentiment-analysis',model='distilbert-base-uncased-finetuned-sst-2-english')

    #4 Run the headlines through the AI
    # We take the 'title' column and convert it to a list
    titles = df['title'].tolist()

    print(f'Analyzing {len(titles)} headlines...')
    results = classifier(titles)

    #5 Extract results and add them to DataFrame
    # Results look like: [{'label': 'POSITIVE', 'score': 0.99}, ...]
    df['sentiment'] = [r['label'] for r in results]
    df['confidence'] = [round(r['score'],4) for r in results]

    #6 Save the results to a new CSV
    output_file='data/analyzed_headlines.csv'
    df.to_csv(output_file,index=False)

    print(f'✅ Analysis complete! Saved results to {output_file}')

    #Sneak Peak of results
    print('\n--- Sample Results ---')
    print(df[['title','sentiment','confidence']].head())

if __name__=="__main__":
    run_sentiment_analysis()