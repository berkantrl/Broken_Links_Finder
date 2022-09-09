from lib.control import Control
from lib.extract import extract
from concurrent.futures import ThreadPoolExecutor
import pyfiglet
import json 
import requests

def main():
    ascii_banner = pyfiglet.figlet_format("     BROKEN   LİNKS \n         FİNDER        ")
    print(ascii_banner)
    urls = []
    with open("config.json") as json_data_file:
        data = json.load(json_data_file)
    for i in data:
        if data[i].lower() == 'on':
            page = 1
            while True:
                url = f"{i}/?page={page}"
                r = requests.get(url,allow_redirects=False)
                if r.status_code==301 or r.status_code == 404:
                    break
                urls.append(url)
                page = page + 1
    for url in urls:
        extract.collect_source(url)
    extract.all_links()
    print("[*]All links Collected.")
    links = Control.get_links()
    with ThreadPoolExecutor(max_workers=8) as executor:
	    executor.map(Control.control_url, links)
    


main() 
print("[!]Broken Links saved in Broken_Links.txt")
