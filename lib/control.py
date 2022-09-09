import requests 


class Control:
    
    def control_url(url):
        try : 
            r = requests.get(url,allow_redirects=False)
            response_code = r.status_code
            match int(str(response_code)[0]):
                case 2:
                    pass
                case 3:
                    Control.control_3xx_code(url)
                case 4:
                    if response_code != 403:
                        Control.write_file(url)
                case 5:
                    Control.write_file(url)
                case _:
                    pass   
        except:
            if 'http' in url[:7]:
                Control.write_file(url)


    def control_3xx_code(url):
        response = requests.get(url, allow_redirects=False)
        new_url =  response.headers['Location']
        Control.control_url(new_url)

    def write_file(url):
        file = open("Broken_Links.txt","a+")
        file.write(url+"\n")
        file.close()

    def get_links():
        file = open("Links.txt","r")
        new_links = []
        links = file.readlines()
        for link in links:
            new_link = link.replace("\n","")
            new_links.append(new_link)
        return new_links

# url = "http://goo.gl/NZek5"
# Control.control_url(url)

