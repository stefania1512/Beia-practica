import telegram
from telegram.ext import Updater, CommandHandler
import requests


# Token-ul de acces pentru botul tău de Telegram
TOKEN = '6195458589:AAFTULq2Lv9KZDb1DGlZ-OxWflZ8Gtu0ouQ'


# Funcție pentru comanda /temperatura
def temperatura(update, context):
   # URL-ul pentru a obține datele meteorologice de la OpenWeatherMap
   url = 'https://api.openweathermap.org/data/2.5/weather '
   params = {
       'q': 'Bucharest,ro',  # Schimbă 'Bucharest,ro' cu orașul tău și codul țării
       'units': 'metric',    # Pentru temperaturi în grade Celsius
       'appid': 'f80ba330cc9f0b9b8be76410d81ff742'  # Înlocuiește cu cheia API OpenWeatherMap
   }


   # Trimite cererea GET pentru a obține datele meteorologice
   response = requests.get(url, params=params)
   data = response.json()


   if data['cod'] == 200:
       temperatura = data['main']['temp']
       update.message.reply_text(f'Temperatura în București este {temperatura} °C.')
   else:
       update.message.reply_text('Nu am putut obține datele meteorologice momentan.')


# Funcția principală pentru rularea botului
def main():
   updater = Updater(TOKEN, use_context=True)
   dp = updater.dispatcher


   # Adaugă handler pentru comanda /temperatura
   dp.add_handler(CommandHandler('temperatura', temperatura))


   # Pornirea botului
   updater.start_polling()
   updater.idle()


if __name__ == '__main__':
   main()
