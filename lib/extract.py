from gc import collect
from bs4 import BeautifulSoup as bs 
import requests


class extract:

    def a_tags(soup,links):
        for link in soup.find_all('a'):
            if link in links or link == None:
                continue
            links.append(link.get('href'))
    
    def iframe_tags(soup,links):
        for link in soup.find_all('iframe'):
            if link in links or link == None:
                continue
            links.append(link.get('src'))
    
    def img_tags(soup,links):
        tags = ['src','data-src']
        for link in soup.find_all('img'):
            for tag in tags:
                if link in links or link == None:
                    continue
                links.append(link.get(tag))

    def script_tags(soup,links):
        for link in soup.find_all('script'):
            if link in links or link == None:
                continue
            links.append(link.get('src'))

    def get_links():
        file = open("source/source.txt","r")
        new_links = []
        links = file.readlines()
        for link in links:
            new_link = link.replace("\n","")
            new_links.append(new_link)
        return new_links

    def all_links():
        urls = extract.get_links()
        links = []
        links_control = []
        for url in urls:
            page = requests.get(url)
            data = page.text 
            soup = bs(data,"lxml")
            extract.a_tags(soup,links)
            extract.iframe_tags(soup,links)
            extract.img_tags(soup,links)
            extract.script_tags(soup,links)
            file = open("Links.txt","a+")
            for link in links:
                if link == None or link in links_control or link[-3:] == 'pdf':
                    continue
                if '/' in link and 'http' in link:
                    file.write(link+"\n")
                    links_control.append(link)
            file.close()

    def collect_source(url):
        links = []
        blogs_links=[]
        page = requests.get(url)
        data = page.text 
        soup = bs(data,"lxml")
        extract.a_tags(soup,links)       
        file = open("source/source.txt","a+")
        for link in links:
            text = "https://www.jotform.com/blog/"
            if link == None or link in blogs_links:
                continue
            if text in link:
                file.write(link+"\n")
                blogs_links.append(link)
        
        file.close()
