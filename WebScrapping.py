import csv
from bs4 import BeautifulSoup
import requests
from collections import namedtuple
import random as rd
import datetime as dt
today = dt.date.today()
fp = open('Articulos.csv', 'x')
fp.close()
file = open("Articulos.csv", 'a', newline='')
write = csv.writer(file)
write.writerow(['Tipo', 'Fecha', 'Servicio', 'Marca', 'Nombre', 'Precio_original', 'Precio_promo'])
#MercadoLibre
#Celulares
url = 'https://listado.mercadolibre.com.mx/telefonos#D[A:telefonos]'
Articulo = namedtuple('Articulo', 'Tipo fecha servicio marca nombre precio_original precio_promo')
lista_articulos = []
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')
articulos_mercadolibre = html_soup.find_all('li' ,class_='ui-search-layout__item')
for articulo in articulos_mercadolibre:
        try:
            fecha = today.strftime("%B %d, %Y")
            servicio = html_soup.find(class_='nav-logo').get_text()[:20]
            marca = articulo.find('p', class_='ui-search-official-store-label ui-search-item__group__element ui-search-color--GRAY').get_text().replace('por ', '')
            nombre = articulo.find('h2', class_='ui-search-item__title').get_text()
            precio_original = articulo.find('span', class_ = 'andes-money-amount__fraction').get_text() + '.' + articulo.find('span', class_='andes-money-amount__cents andes-money-amount__cents--superscript-16').get_text()
            precio_promo = articulo.find(class_='ui-search-price__second-line').find('span', class_='andes-money-amount__fraction').get_text()
            print(fecha, servicio, marca, nombre, precio_original, precio_promo, end='\n\n\n')
            lista_articulos.append(Articulo('Celular', fecha, servicio, marca, nombre, precio_original, precio_promo))
        except AttributeError:
            pass

#Laptops

url = 'https://listado.mercadolibre.com.mx/laptops#D[A:laptops]'
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')
articulos_mercadolibre = html_soup.find_all('li' ,class_='ui-search-layout__item')
for articulo in articulos_mercadolibre:
        try:
            fecha = today.strftime("%B %d, %Y")
            servicio = html_soup.find(class_='nav-logo').get_text()[:20]
            marca = articulo.find('p', class_='ui-search-official-store-label ui-search-item__group__element ui-search-color--GRAY').get_text().replace('por ', '')
            nombre = articulo.find('h2', class_='ui-search-item__title').get_text()
            precio_original = articulo.find('span', class_ = 'andes-money-amount__fraction').get_text() + '.' + articulo.find('span', class_='andes-money-amount__cents andes-money-amount__cents--superscript-16').get_text()
            precio_promo = articulo.find(class_='ui-search-price__second-line').find('span', class_='andes-money-amount__fraction').get_text()
            print(fecha, servicio, marca, nombre, precio_original, precio_promo, end='\n\n\n')
            lista_articulos.append(Articulo('Laptop', fecha, servicio, marca, nombre, precio_original, precio_promo))
        except AttributeError:
            pass

#Tablets

url = 'https://listado.mercadolibre.com.mx/tablets#D[A:tablets]'
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')
articulos_mercadolibre = html_soup.find_all('li' ,class_='ui-search-layout__item')
for articulo in articulos_mercadolibre:
        try:
            fecha = today.strftime("%B %d, %Y")
            servicio = html_soup.find(class_='nav-logo').get_text()[:20]
            marca = articulo.find('p', class_='ui-search-official-store-label ui-search-item__group__element ui-search-color--GRAY').get_text().replace('por ', '')
            nombre = articulo.find('h2', class_='ui-search-item__title').get_text()
            precio_original = articulo.find('span', class_ = 'andes-money-amount__fraction').get_text() + '.' + articulo.find('span', class_='andes-money-amount__cents andes-money-amount__cents--superscript-16').get_text()
            precio_promo = articulo.find(class_='ui-search-price__second-line').find('span', class_='andes-money-amount__fraction').get_text()
            print(fecha, servicio, marca, nombre, precio_original, precio_promo, end='\n\n\n')
            lista_articulos.append(Articulo('Tablets', fecha, servicio, marca, nombre, precio_original, precio_promo))
        except AttributeError:
            pass

#AliExpress
#Celulares
url = 'https://es.aliexpress.com/w/wholesale-celulares.html?spm=a2g0o.best.search.0'
Articulo = namedtuple('Articulo', 'Tipo fecha servicio marca nombre precio_original precio_promo')
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')
articulos_AliExpress = html_soup.find_all('div' ,class_='list--gallery--C2f2tvm search-item-card-wrapper-gallery')
for articulo in articulos_AliExpress:
        try:
            fecha = today.strftime("%B %d, %Y")
            nombre = articulo.find('h1', class_='multi--titleText--nXeOvyr').get_text()
            precio_original = articulo.find('div', class_ = 'multi--price-sale--U-S0jtj').get_text().replace('MXN$', '')
            print(fecha, nombre, precio_original, end='\n\n\n')
            lista_articulos.append(Articulo('Celular', fecha, 'AliExpress', 'N/P', nombre, precio_original, 'N/P'))
        except AttributeError:
            pass

#Laptops
url = 'https://es.aliexpress.com/w/wholesale-Laptops.html?spm=a2g0o.productlist.search.0'
Articulo = namedtuple('Articulo', 'Tipo fecha servicio marca nombre precio_original precio_promo')
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')
articulos_AliExpress = html_soup.find_all('div' ,class_='list--gallery--C2f2tvm search-item-card-wrapper-gallery')
for articulo in articulos_AliExpress:
        try:
            fecha = today.strftime("%B %d, %Y")
            nombre = articulo.find('h1', class_='multi--titleText--nXeOvyr').get_text()
            precio_original = articulo.find('div', class_ = 'multi--price-sale--U-S0jtj').get_text().replace('MXN$', '')
            print(fecha, nombre, precio_original, end='\n\n\n')
            lista_articulos.append(Articulo('Laptop', fecha, 'AliExpress', 'N/P', nombre, precio_original, 'N/P'))
        except AttributeError:
            pass

#Tablets

url = 'https://es.aliexpress.com/w/wholesale-tablets.html?spm=a2g0o.productlist.search.0'
Articulo = namedtuple('Articulo', 'Tipo fecha servicio marca nombre precio_original precio_promo')
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')
articulos_AliExpress = html_soup.find_all('div' ,class_='list--gallery--C2f2tvm search-item-card-wrapper-gallery')
for articulo in articulos_AliExpress:
        try:
            fecha = today.strftime("%B %d, %Y")
            nombre = articulo.find('h1', class_='multi--titleText--nXeOvyr').get_text()
            precio_original = articulo.find('div', class_ = 'multi--price-sale--U-S0jtj').get_text().replace('MXN$', '')
            print(fecha, nombre, precio_original, end='\n\n\n')
            lista_articulos.append(Articulo('Tablet', fecha, 'AliExpress', 'N/P', nombre, precio_original, 'N/P'))
        except AttributeError:
            pass

file = open("Articulos.csv", 'a', newline='')
write = csv.writer(file)
for i in lista_articulos:
    write.writerow([i[0],i[1],i[2], i[3], i[4], i[5], i[6]])
file.close()

