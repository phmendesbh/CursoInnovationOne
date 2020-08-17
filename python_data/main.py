import requests
from bs4 import BeautifulSoup
import json

res = requests.get('https://blog.bhguitar.com.br/')
res.encoding = 'utf-8' #formatar caracteres de acentuação

soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find_all(class_='post-entry')
#print(len(posts))
#print(posts[0])
#find_all encontra várias ocorrencias
#find pega o primeiro que achar

all_post = []
for post in posts:
    info = post.find(class_='post-entry__content')
    title = info.h2.text
    preview = info.p.text
    author = info.find(class_='author').text
    date = info.time['datetime']
    all_post.append(
        { 
            'title':title,
            'preview':preview,
            'author': author,
            'date': date
        })

print(all_post)
with open('posts.json', 'w') as json_file:
    json.dump(all_post, json_file, indent=3, ensure_ascii=False)