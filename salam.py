import datetime as dt 
import requests 
 
DATABASE = { 
 'Влад': 'Самара', 
 'Максад': 'Москва', 
 'Умед': 'Душанбе', 
 'Алексей': 'Москва', 
 'Дима': 'Самара', 
 'Камилла': 'Варшава', 
 'Шера': 'Бостон', 
 'Парвина': 'Берлин', 
 'Глэдис': 'Майами', 
 'Мухаммад': 'Пекин' 
} 
 
UTC_OFFSET = { 
 'Москва': 3, 
 'Санкт-Петербург': 3, 
 'Новосибирск': 7, 
 'Екатеринбург': 5, 
 'Нижний Новгород': 3, 
 'Казань': 3, 
 'Челябинск': 5, 
 'Омск': 6, 
 'Самара': 4, 
 'Ростов-на-Дону': 3, 
 'Уфа': 5, 
 'Бостон': -4, 
 'Берлин': 2, 
 'Пекин': 8, 
 'Варшава': 2, 
 'Краснодар': 3, 
 'Майами': -4, 
 'Душанбе': 5 
} 
 
print('Привет, Я Саламчик')
print('Мой Создатель Пронин Иujhm')
def format_count_friends(count_friends): 
 if count_friends == 1: 
     return f'1 друг' 
 elif 2 <= count_friends <= 4: 
     return f'{count_friends} друга' 
 else: 
     return f'{count_friends} друзей' 
 
 
def what_time(city): 
     offset = UTC_OFFSET[city] 
     city_time = dt.datetime.utcnow() +        dt.timedelta(hours=offset) 
     f_time = city_time.strftime("%H:%M") 
     return f_time 
 
 
def what_weather(city): 
     url = f'http://wttr.in/{city}' 
     weather_parameters = { 
         'format': 2, 
         'M': '' 
     } 
     try: 
         response = requests.get(url,    params=weather_parameters) 
     except requests.ConnectionError: 
          return '<сетевая ошибка>' 
     if response.status_code == 200: 
          return response.text 
     else: 
          return '<ошибка на сервере погоды>' 
 
 
def process_salamchik(query): 
     if query == 'сколько у меня друзей?': 
         count = len(DATABASE) 
         return f'У тебя {format_count_friends(count)}.' 
     elif query == 'кто все мои друзья?': 
         friends_string = ', '.join(DATABASE) 
         return f'Твои друзья: {friends_string}' 
     elif query == 'где все мои друзья?': 
         unique_cities = set(DATABASE.values()) 
         cities_string = ', '.join(unique_cities) 
         return f'Твои друзья в городах: {cities_string}' 
     else: 
         return '<неизвестный запрос>' 
 
 
def process_friend(name, query): 
     if name in DATABASE: 
         city = DATABASE[name] 
         if query == 'ты где?': 
             return f'{name} в городе {city}' 
         elif query == 'который час?': 
             if city not in UTC_OFFSET: 
                 return f'<не могу определить время в городе {city}>' 
             time = what_time(city) 
             return f'Там сейчас {time}' 
         elif query == 'как погода?': 
             weather_friend = what_weather(city) 
             return weather_friend 
 
         else: 
             return '<неизвестный запрос>' 
     else: 
         return f'У тебя нет друга по имени {name}' 
 
 
def process_query(query): 
     elements = query.split(', ') 
     if elements[0] == 'Саламчик': 
         return process_salamchik(elements[1]) 
     else: 
         return process_friend(elements[0], elements[1]) 
 
 
def runner(): 
 queries = [ 
 'Саламчик, сколько у меня друзей?', 
 'Саламчик, кто все мои друзья?', 
 'Саламчик, где все мои друзья?', 
 'Саламчик, кто виноват?', 
 'Дима, ты где?', 
 'Умед, что делать?', 
 'Умед, ты где?', 
 'Дима, который час?', 
 'Умед, который час?', 
 'Камилла, который час?', 
 'Глэдис, который час?', 
 'Умед, как погода?', 
 'Дима, как погода?', 
 'Шера, как погода?' 
 ] 
 for query in queries: 
     print(query, '-', process_query(query)) 
 
 
runner()
