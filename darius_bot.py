from telegram.ext import Updater, CommandHandler
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
import json
import logging

# Configurare log
logging.basicConfig(level=logging.INFO)

# Tokenul de la BotFather
TOKEN = "8149187014:AAF-qoPxJBEtzpp2_aRN0KT-omblZj_tELc"

# Citește cele mai recente date din fișierul JSON generat
import json

def get_latest_data():
    try:
        with open("latest_data.json", "r") as f:
            data = json.load(f)
            return (
                data.get("temperature"),
                data.get("humidity"),
                data.get("solar_radiation"),
                data.get("precipitation"),
                data.get("timestamp"),
            )
    except:
        return None, None, None, None, None



# Comanda /start
def start(update, context):
    update.message.reply_text(
        "Salut! Sunt Darius IOT Bot 🤖\n"
        "Comenzi disponibile:\n"
        "/temperature – temperatura actuală\n"
        "/humidity – umiditatea actuală\n"
        "/radiation – radiație solară\n"
        "/precipitation – precipitație\n"
        "/all – toate valorile disponibile\n"
    )
    print("CHAT_ID:", update.message.chat_id)

# Comanda /temperature
def temperature(update, context):
    temp, _, _, _, _ = get_latest_data()
    if temp is not None:
        update.message.reply_text(f"🌡️ Temperatură: {temp} °C")
    else:
        update.message.reply_text("❌ Nu există date despre temperatură.")

# Comanda /humidity
def humidity(update, context):
    _, hum, _, _, _ = get_latest_data()
    if hum is not None:
        update.message.reply_text(f"💧 Umiditate: {hum} %RH")
    else:
        update.message.reply_text("❌ Nu există date despre umiditate.")

# Comanda /radiation
def radiation(update, context):
    _, _, radiation, _, _ = get_latest_data()
    if radiation is not None:
        update.message.reply_text(f"☀️ Radiație solară: {radiation} W/m²")
    else:
        update.message.reply_text("❌ Nu există date despre radiația solară.")

# Comanda /precipitation
def precipitation(update, context):
    _, _, _, precipitation, _ = get_latest_data()
    if precipitation is not None:
        update.message.reply_text(f"🌧️ Precipitație: {precipitation} mm")
    else:
        update.message.reply_text("❌ Nu există date despre precipitație.")

# Comanda /all
def all_data(update, context):
    temp, hum, radiation, precipitation, timestamp = get_latest_data()
    if None not in (temp, hum, radiation, precipitation, timestamp):
        update.message.reply_text(
            f"📊 Toate valorile disponibile:\n"
            f"🕒 Timp: {timestamp}\n"
            f"🌡️ Temperatură: {temp} °C\n"
            f"💧 Umiditate: {hum} %RH\n"
            f"☀️ Radiație solară: {radiation} W/m²\n"
            f"🌧️ Precipitație: {precipitation} mm"
        )
    else:
        update.message.reply_text("❌ Nu există date complete în acest moment.")

# Alertă pentru temperatură
def check_temperature_alert(bot):
    temp, _, _, _, _ = get_latest_data()
    if temp is not None and temp > 30:
        bot.send_message(
            chat_id=8192607517,
            text=f"⚠️ ALERTĂ: Temperatura a depășit 30°C!\n🌡️ Temperatură actuală: {temp}°C"
        )

# Inițializare bot și programare alertă
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("temperature", temperature))
    dp.add_handler(CommandHandler("humidity", humidity))
    dp.add_handler(CommandHandler("radiation", radiation))
    dp.add_handler(CommandHandler("precipitation", precipitation))
    dp.add_handler(CommandHandler("all", all_data))

    # Pornire scheduler pentru alertă
    scheduler = BackgroundScheduler(timezone=utc)
    scheduler.add_job(lambda: check_temperature_alert(updater.bot), 'interval', seconds=60)
    scheduler.start()

    updater.start_polling()
    print("✅ Botul a pornit. Scrie /start în Telegram.")
    updater.idle()

if __name__ == '__main__':
    main()
