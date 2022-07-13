from bs4 import BeautifulSoup
import requests

url = 'https://anitrendz.net/charts/top-anime/'
output = open("Trending_Anime_RankList.txt","w", encoding='utf-8')
result = requests.get(url)
website = BeautifulSoup(result.text, 'lxml')

trending = website.find(class_="at-main-chart-entries")
title = trending.find_all(class_="entry-title")
rank = 1
for titles in title:
    output.write(str(rank) + "\t" + titles.text.strip() + "\n")
    rank +=1