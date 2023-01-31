from email import header
from bs4 import BeautifulSoup
import requests
from csv import writer


url = "https://www.imobiliare.ro/vanzare-apartamente/bucuresti-ilfov/popesti-leordeni"


page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

list1 = soup.find_all('div', class_="col_descriere")
list2 = soup.find_all('div', class_="caracteristici_anuntspecial_wp")

for ad1 in list1:
    rooms = None
    area = None
    floor = None
    type = None
    location = None
         #get the price
    if(ad1.find('span', class_="pret-mare") == None):
        price = 'N/A'
    else:
        price = ad1.find('span', class_="pret-mare").text 

    aux = ((ad1.find('p', class_="location_txt").text).encode("utf-8"))
    location = (str(aux.strip()))   
 
     
    if( ad1.findChildren('strong') != None):
        multiInfo = ad1.findChildren('strong')
        for i in multiInfo:
            
            if(ad1.find('strong').text == 'o'):
                rooms = '0'
            else:
                rooms = multiInfo[0].text

            area = multiInfo[1].text
            floor = multiInfo[2].text

            try:
                type = multiInfo[3].text
            except IndexError:
                type = None        
    else:
        multiInfo = ['N/A','N/A','N/A','N/A', 'N/A']
    
    allInfo = [price,rooms,area,floor, type, location]
    print(location)
   