from bs4 import BeautifulSoup
import time
import datetime
import os
import requests


def pricepoint(table):
        for i in range(25):
            crypto = table.find("tr", class_="row false yf-paf8n5", id=i)
            crypto_percent_change = crypto.find_all("td", class_ = "cell tw-h-10 tw-py-0 yf-paf8n5")[4]
            span = crypto_percent_change.find_all("span")[1]
            name = crypto.find("td", class_ = "cell tw-h-10 tw-py-0 tw-text-left yf-paf8n5")
            coin = name.find("div", class_ = "yf-h8l7j7").string
            print(f"{coin:<20}: {span.string}")
            i +=1

def website(url):
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find(class_ = "body yf-paf8n5")
    return(table)
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    i = 0
    
    while True:   
        url = "https://finance.yahoo.com/markets/crypto/all/"
        now = datetime.datetime.now()
        current_time = now.time().replace(microsecond=0)
        clear_terminal() 
        print(current_time)
        print(f"iteration {i}")
        websites = website(url)
        pricepoint(websites)
        #cypo(websites)
        time.sleep(5) 
        i +=1


def cypo(table):
        crypto = table.find("tr", class_="row false yf-paf8n5", id=0)
        crypto_percent_change = crypto.find_all("td", class_ = "cell tw-h-10 tw-py-0 yf-paf8n5")[4]
        span = crypto_percent_change.find_all("span")[1]
        name = crypto.find("td", class_ = "cell tw-h-10 tw-py-0 tw-text-left yf-paf8n5")
        coin = name.find("div", class_ = "yf-h8l7j7").string
        print(f"{coin:<20}: {span.string}")
        return(span.string)
def cypo2(table):
        crypto = table.find("tr", class_="row false yf-paf8n5", id=0)
        crypto_percent_change = crypto.find_all("td", class_ = "cell tw-h-10 tw-py-0 yf-paf8n5")[4]
        span = crypto_percent_change.find_all("span")[1]
        name = crypto.find("td", class_ = "cell tw-h-10 tw-py-0 tw-text-left yf-paf8n5")
        coin = name.find("div", class_ = "yf-h8l7j7").string
        print(f"{coin:<20}: {span.string}")
        return(span.string)

def timer():
    url = "https://finance.yahoo.com/markets/crypto/all/"
    first = cypo(website(url))
    second = cypo2(website(url))
    start = time.time()
    while first == second:
        time.sleep(30)
        second = cypo(website(url))
    end = time.time()
    print(f"Time taken to update {end-start} seconds")
main()