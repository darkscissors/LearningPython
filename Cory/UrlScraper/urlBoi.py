import requests #allows us to use the inter web
from bs4 import BeautifulSoup #html parser from python

def pageOpen():
    url = 'https://someonewhocares.org/hosts/' #change to access any url
    resp = requests.get(url) #store the contents of the url into a variable

    if resp.status_code == 200: #code 200 means everything went good in html
        print("Successfully opened web page")

        soup = BeautifulSoup(resp.text, 'html.parser')

        list = soup.find("div", {"class":"BODY"})

        for i in list.findAll('pre'): #find all looks for specific tags in html e.g. if you put 'p' would read all <p></p> tags
            print(i.text)
    else:
        print("Error code: ")
        print(resp.status_code)

pageOpen()
