from email import header
from fileinput import filename
from operator import mul
from bs4 import BeautifulSoup
import requests
from csv import writer

#arrayLink = ['https://www.imobiliare.ro/vanzare-apartamente/bucuresti-ilfov/popesti-leordeni'] Apartamente popesti-leordeni
arrayLink = ['https://www.imobiliare.ro/vanzare-case-vile/bucuresti-ilfov/popesti-leordeni']   # Vile popesti-leordeni

def extractorX(url, pageName):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    adList = soup.find_all('div', class_="col_descriere")
    
    f = open(pageName,'w' , encoding= 'utf8', newline='')
    theWriter = writer(f)
    header = ['Price','Rooms','Area','Floor', 'TotalArea','Location']
    theWriter.writerow(header)
    
    for ad in adList:
        rooms = None
        area = None
        totalArea = None
        floor = None
        #type = None
        location = None  
        #get the price
        if(ad.find('span', class_="pret-mare") == None):
            price = 'N/A'
        else:
            price = ad.find('span', class_="pret-mare").text 
        
        if( ad.findChildren('strong') != None):
            multiInfo = ad.findChildren('strong')
            for i in multiInfo:
            
                if(ad.find('strong').text == 'o'):
                    rooms = '0'
                else:
                    rooms = multiInfo[0].text

                try:
                    area = multiInfo[1].text
                except IndexError:
                    area = None
                
                try:
                    floor = multiInfo[2].text
                except IndexError:
                    floor = None 

                try:
                    totalArea = multiInfo[3].text
                except IndexError:
                    totalArea = None        
        else:
            multiInfo = ['N/A','N/A','N/A','N/A','N/A']

        aux = ((ad.find('p', class_="location_txt").text).encode("utf-8"))
        location = (str(aux.strip()))
        
        allInfo = [price,rooms,area,floor, totalArea, location]
        print(allInfo)
        theWriter.writerow(allInfo)     

    return f   



def linkGen(limit):
    auxArray = [] 
    count = 2
    while count < limit:
        #auxArray.append('https://www.imobiliare.ro/vanzare-apartamente/bucuresti-ilfov/popesti-leordeni?pagina=' + str(count)) Aprtamente popesti
        auxArray.append('https://www.imobiliare.ro/vanzare-case-vile/bucuresti-ilfov/popesti-leordeni?pagina=' + str(count)) # Vile popesti
        count= count + 1 
        if(count == limit):
            break
    return auxArray 

arrayLink = arrayLink + (linkGen(11)) #Replace value whenever you use a new link, No. of pages
print(arrayLink)

pages = []

def genPages(limitPages):
    i = 1
    auxPages = []
    while (i < limitPages):
        auxPages.append('page' + str(i) + '.csv')
        i += 1
        if(i == limitPages):
            break
    return auxPages

pages = pages + (genPages(29))

for i in range (len(arrayLink)):  
    extractorX(arrayLink[i], pages[i]) 


        

