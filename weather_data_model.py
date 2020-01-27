from datetime import datetime,timedelta

class WeatherData:
    town_id=0
    year=0
    month=0
    day=0
    hour=0
###
# Ветер - указаны скорость ветра в м/с - средняя за 10 мин, порывы в срок и между сроками (в фигурных скобках) и направление, откуда дует ветер: С - северный,
#СВ - северо-восточный, В - восточный, ЮВ - юго-восточный, Ю - южный, ЮЗ - юго-западный, З - западный, СЗ - северо-западный.    
    wind=''
    wind_velocity=''

###
# Видимость - горизонтальная дальность видимости в метрах или километрах. При видимости от 1 до 10 км при отсутствии осадков обычно наблюдается дымка, 
# при ухудшении видимости до 1 км и менее - туман. В сухую погоду видимость может ухудшаться дымом, пылью или мглою.
    visibility=''

###
# Явления - указаны атмосферные явления, наблюдавшиеся в срок или в последний час перед сроком; фигурными скобками обозначены явления, наблюдавшиеся между сроками 
# (за 1-3 часа до срока); квадратными скобками обозначены град или гололедные отложения с указанием их диаметра в мм.
    conditions=''

###
# Облачность - указаны через наклонную черту общая и нижняя облачность в баллах и высота нижней границы облаков в метрах; квадратными скобками обозначены формы облаков: 
# Ci - перистые, Cs - перисто-слоистые, Cc - перисто-кучевые, Ac - высококучевые, As - высокослоистые, Sc - слоисто-кучевые, Ns - слоисто-дождевые, Cu - кучевые, 
# Cb - кучево-дождевые. Подробнее классификацию облаков см. в Атласе облаков (PDF).
    cloudiness=''

###
# T - Температура воздуха - температура, измеренная на высоте 2 м над землей.
    temperature=''

###
# Td - Температура точки росы - температура, при понижении до которой содержащийся в воздухе водяной пар достигнет насыщения.
    dew_point=''

###
# f - Относительная влажность воздуха - влажноcть воздуха, измеренная на высоте 2 м над землей.
    relative_humidity=''

###
# Te - Эффективная температура - температура, которую ощущает одетый по сезону человек в тени. Характеристика душности погоды. 
# При расчете учитывается влияние влажности воздуха и скорости ветра на теплоощущения человека.
    effective_temperature=''

###
# Tes - Эффективная температура на солнце - температура, которую ощущает человек, с поправкой на солнечный нагрев. Характеристика знойности погоды. 
# Зависит от высоты солнца над горизонтом, облачности и скорости ветра. Ночью, в пасмурную погоду, а также при ветре 12 м/с и более поправка равна нулю.
    solar_effective_temperature=''

###
# комфортность
    comfortness=''

###
# P - Атмосферное давление - приведенное к уровню моря атмосферное давление.
    pressure=''

###
# Po - Атмосферное давление - измеренное на уровне метеостанции атмосферное давление.
    station_pressure=''

###
# Tmin - Минимальная температура - минимум температуры воздуха на высоте 2 м над землей.
    min_temperature=''

###
# Tmax - Максимальная температура - максимум температуры воздуха на высоте 2 м над землей.
    max_temperature=''

###
# R - Количество осадков - Количество выпавших осадков за период времени, мм. 
# При наведении курсора мыши на число - период времени, за который выпало указанное количество осадков.                    
    fallout=''

###
# R24 - Количество осадков - Количество выпавших осадков за 24 часа, мм.
    fallout_24=''

###
# S - Снежный покров - Высота снежного покрова, см. При наведении курсора мыши на число - состояние снежного покрова и степень покрытия местности в баллах.
    snow_cover=''

    def __init__(self, town_id,year, month, weather_item):
        row=weather_item[0]
        content=weather_item[1]

        self.town_id=town_id

        
        row_items=row.select('td')
        content_items=content.select('td')
        # print(content_items)
        hour0=int(row_items[0].text)
        day0=int(row_items[1].text.split('.')[0])

        # print('before ',datetime(year,month+1,day0,hour0))
        measure_time=datetime(year,month+1,day0,hour0)+timedelta(hours=3)
        # print('after ',measure_time)
        self.year=measure_time.year
        self.month=measure_time.month
        self.day=measure_time.day
        self.hour=measure_time.hour

        self.wind=content_items[0].text
        self.wind_velocity=content_items[1].text
        self.visibility=content_items[2].text
        self.conditions=content_items[3].text
        self.cloudiness=content_items[4].text
        self.temperature=content_items[5].text
        self.dew_point=content_items[6].text
        self.relative_humidity=content_items[7].text
        self.effective_temperature=content_items[8].text
        self.solar_effective_temperature=content_items[9].text
        self.comfortness=content_items[10].text
        self.pressure=content_items[11].text
        self.station_pressure=content_items[12].text
        self.min_temperature=content_items[13].text
        self.max_temperature=content_items[14].text
        self.fallout=content_items[15].text
        self.fallout_24=content_items[16].text
        self.snow_cover=content_items[17].text

    def write_to_csv(self,writer):
        row=[self.town_id,self.year,self.month,self.day,self.hour,
             self.wind,self.wind_velocity,self.visibility,self.conditions,self.cloudiness,
             self.temperature,self.dew_point,self.relative_humidity,self.effective_temperature,
             self.solar_effective_temperature,self.comfortness,self.pressure,self.station_pressure,
             self.min_temperature,self.fallout,self.fallout_24,self.snow_cover]
        writer.writerow(row)


