import logging
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import time

# Налаштування логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Конфігурація
TOKEN = '7811848391:AAHYkDMvpr58N7fpTVQK6KiNlFxyo2malSU'  # Заміни на свій токен
gift_options = [0.0001, 0.1, 0.0002, 0.2, 0.5, 2]  # Варианти подарунків
user_data = {}  # Зберігання даних користувачів

# Час для отримання наступного подарунка в секундах (180 хвилин)
TIME_TO_WAIT = 180 * 60  

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Start command received")  # Логування команди start
    user_id = update.effective_chat.id
    if user_id not in user_data:
        user_data[user_id] = {'gifts': 0, 'last_opened': 0}
    
    await context.bot.send_photo(chat_id=user_id, photo=InputFile('background.webp'))
    await update.message.reply_text("Привіт! Ти можеш відкривати подарунки!")

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    # Додайте інші команди...

    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
