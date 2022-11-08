from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

def get_html(request):
    sku = request.GET.get('sku')
    url = f"https://www.leroymerlin.pl/szukaj.html?q={sku}&sprawdz=true"
    soup = get_soup(url)
    return HttpResponse(soup)

def get_name_sku_from_website_LM(sku):
    
    link = f"https://www.leroymerlin.pl/szukaj.html?q={sku}&sprawdz=true"
    name_of_product_and_sku =get_name_sku_of_product(link)
    print('!!!!!!!!!!!!!!!!!!',sku)
    
    return(name_of_product_and_sku)
    #eturn(sku)

def get_soup(url):
    print('url---',url)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
    r = requests.get(url, headers=headers)
  
    if r == None:
        return None
    else:
        soup = BeautifulSoup(r.text, 'lxml')
    return soup



def get_name_sku_of_product(url):
    soup = get_soup(url)
    print(soup)
    name_of_product = soup.find('div', class_="product-description").find('div',class_="product-title" ).find('h1').string
    sku = int(soup.find('div', class_="product-description").find('div', class_="ref-number").find('span').string)
    resolt = {"name_of_product":name_of_product, "sku":sku}
    #print (resolt) 
    return(resolt)