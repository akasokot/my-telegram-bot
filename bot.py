from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import time

# Конфігурація
TOKEN = '7811848391:AAHYkDMvpr58N7fpTVQK6KiNlFxyo2malSU'  # Заміни на свій токен
gift_options = [0.0001, 0.1, 0.0002, 0.2, 0.5, 2]  # Варианти подарунків
user_data = {}  # Зберігання даних користувачів

# Час для отримання наступного подарунка в секундах (180 хвилин)
TIME_TO_WAIT = 180 * 60  

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_chat.id
    if user_id not in user_data:
        user_data[user_id] = {'gifts': 0, 'last_opened': 0}
    
    await context.bot.send_photo(chat_id=user_id, photo=InputFile('background.webp'))
    await update.message.reply_text("Привіт! Ти можеш відкривати подарунки!")

async def open_gifts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_chat.id
    current_time = time.time()
    user = user_data[user_id]

    if user['gifts'] < 5:
        gift = random.choice(gift_options)
        user['gifts'] += 1
        user['last_opened'] = current_time
        
        await context.bot.send_photo(chat_id=user_id, photo=InputFile('background.webp'))
        await update.message.reply_text(f"Ти відкрив подарунок: {gift} TON/NOT/NEWYEARS!")

    elif (current_time - user['last_opened']) >= TIME_TO_WAIT:
        gift = random.choice(gift_options)
        user['gifts'] += 1
        user['last_opened'] = current_time
        
        await context.bot.send_photo(chat_id=user_id, photo=InputFile('background.webp'))
        await update.message.reply_text(f"Ти відкрив додатковий подарунок: {gift} TON/NOT/NEWYEARS!")
    else:
        time_left = TIME_TO_WAIT - (current_time - user['last_opened'])
        minutes_left = time_left // 60
        
        await context.bot.send_photo(chat_id=user_id, photo=InputFile('background.webp'))
        await update.message.reply_text(f"Наступний подарунок можна відкрити через {minutes_left} хвилин.")

async def exchange(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Логіка обміну подарунків
    pass

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Логіка виводу TON/NOT
    pass

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("open", open_gifts))
    application.add_handler(CommandHandler("exchange", exchange))
    application.add_handler(CommandHandler("withdraw", withdraw))
    
    application.run_polling()

if __name__ == '__main__':
    main()
