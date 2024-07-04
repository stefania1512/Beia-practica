from telegram.ext import Application, CommandHandler, CallbackContext
import requests
from typing import Final
from telegram import Update

# Token-ul de acces pentru botul tău de Telegram
TOKEN = '6195458589:AAFTULq2Lv9KZDb1DGlZ-OxWflZ8Gtu0ouQ'
BOT_USERNAME: Final = '@StefIonBot'

# Funcția pentru comanda /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Salut! Sunt un bot de Telegram! Type /temperature to get the current temperature.")

# Funcția pentru comanda /temperature
async def get_temperature(update: Update, context: CallbackContext) -> None:
    city = "Bucuresti"
    url = f"https://wttr.in/{city.replace(' ', '+')}?format=%t"

    # Trimite cererea GET pentru a obține datele meteorologice
    response = requests.get(url)

    if response.status_code == 200:
        temperatura = response.text.strip()
        await update.message.reply_text(f'Temperatura în {city} este {temperatura}')
    else:
        await update.message.reply_text('Nu am putut obține datele meteorologice momentan.')

# Funcția principală pentru rularea botului
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("temperature", get_temperature))

    app.run_polling()

if __name__ == '__main__':
    main()
