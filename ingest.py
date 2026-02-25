import os
import requests
from dotenv import load_dotenv
import pandas as pd

#Load the secret key from .env file
load_dotenv()
NEWS_API_KEY=os.getenv('NEWS_API_KEY')

def fetch_gaming_news():
    print("Connecting to NewsAPI...")

    #Define the 'Order' (URL and parameters)
    url='https://newsapi.org/v2/everything'
    params={
        'q':'gaming OR playstation OR xbox OR nintendo',
        'language':'en',
        'sortBy':'publishedAt',
        'pageSize':20,
        'apiKey':NEWS_API_KEY  
    }

    # Send the request to the internet
    response=requests.get(url, params=params)

    if response.status_code==200:
        #Success! Extract the articles
        articles=response.json().get('articles', [])

        #Clean the data: We want only title and Source Name
        cleaned_data=[]
        for a in articles:
            cleaned_data.append({
                'title':a.get('title'),
                'source':a.get('source', {}).get('name'),
                'url':a.get('url')
            })

        #Turn it into a Table(DataFrame)
        df =pd.DataFrame(cleaned_data)
        df.to_csv('data/raw_headlines.csv',index=False)
        print(f"✅ Success! Saved {len(df)} headlines to data/raw_headlines.csv")

    else:
        print(f"❌ Failed to fetch news. Status Code: {response.status_code}")
        print(f"Response: {response.text}")

if __name__=="__main__":
    fetch_gaming_news() 