import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Налаштування логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Конфігурація
TOKEN = '7811848391:AAHYkDMvpr58N7fpTVQK6KiNlFxyo2malSU'  # Заміни на свій токен

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привіт!")  # Відповідь бота

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Додаємо обробник команди /start
    application.add_handler(CommandHandler("start", start))

    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
