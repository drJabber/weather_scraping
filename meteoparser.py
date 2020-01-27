import sys
import csv
import calendar
import requests
from urllib.parse import urlparse, parse_qs
from weather_data_model import WeatherData
from calendar import monthrange
from bs4 import BeautifulSoup

class MeteoParser:
    def parse(self, filename):
        towns=self.get_towns()
        with open(filename+'towns.csv','a') as f:
            fieldnames=['id','town']
            writer=csv.writer(f, dialect="excel", delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            writer.writerow(fieldnames)
            writer.writerows(towns.items())
            f.close()

        with open(filename+'weather.csv','a') as f:
            fieldnames=('town_id','year','month','day','hour','wind','wind_velocity','visibility','conditions','cloudiness',
                       'temperature','dew_point','relative_humidity','effective_temperature','solar_effective_temperature',
                       'comfortness','pressure','station_pressure','min_temperature','max_temperature','fallout','fallout_24','snow_cover')

            writer=csv.writer(f, dialect="excel", delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            writer.writerow(fieldnames)
            self.parse_region_weather(towns,writer)
            f.close()

    def get_towns(self):
        # return self.parse_region_towns(50)
        return self.get_certain_towns()
    
    def get_certain_towns(self):
        return {'28900':'Самара', '27330':'Ярославль', '34730':'Ростов-на-Дону', '26702':'Калининград'}

    
    def parse_region_towns(self,region_id):
        towns={}
        url=f'http://www.pogodaiklimat.ru/archive.php?id=ru&region={region_id}'
        page=requests.get(url)
        soup=BeautifulSoup(page.content,'lxml')
        cssquery='div.big-blue-billet__list-wrap div.big-blue-billet__list-container ul.big-blue-billet__list li.big-blue-billet__list_link a'
        rows=soup.select(cssquery)
        for row in rows:
            href=urlparse(row['href'])
            town_id=parse_qs(href.query)['id'][0]
            town=row.text
            towns[town_id]=town
        return towns   

    def parse_region_weather(self,towns,writer):
        for town_id,town in list(towns.items()):
            print(town)
            self.parse_town_weather(town_id,writer)

    def parse_town_weather(self,town_id,writer):
        for year in range(2011,2020):
            for month in range(12):
                print(year,' ',month)
                self.parse_period_weather(town_id,month,year,writer)

    def parse_period_weather(self, town_id, month, year,writer):
        wd, days=monthrange(year, month+1)
        url=f'http://www.pogodaiklimat.ru/weather.php?id={town_id}&bday=1&fday={days}&amonth={month+1}&ayear={year}&bot=2'
        page=requests.get(url)
        soup=BeautifulSoup(page.content,'lxml')
        rows=soup.select('div.archive-wrap div.archive-table div.archive-table-left-column table tr')
        content=soup.select('div.archive-wrap div.archive-table div.archive-table-wrap table tr')

        weather=list(zip(rows,content))
        for item in weather[1:]:
            data=WeatherData(town_id,year, month,item)
            data.write_to_csv(writer)

