import requests
from api_objects.get_news_api import GetNewsApi

def get_top_headline_news(q):
    get_news_api = GetNewsApi(requests.Session())
    response = get_news_api.get_top_headlines(q=q)
    return response

if __name__ == "__main__":
    print(get_top_headline_news(q="Trump"))
