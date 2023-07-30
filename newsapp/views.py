from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key='acf267b65b0c4f388ca3a398d62ab4f6')
    top = newsapi.get_top_headlines(sources='bbc-news')
    my_articles = top['articles']
    news = []
    desc = []
    img = []
    for i in range(len(my_articles)):
        f = my_articles[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        myList = zip(news, desc, img)
    return render(request, 'index.html', context={'mylist':myList})