from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import time

# Конфігурація
TOKEN = 'AAHYkDMvpr58N7fpTVQK6KiNlFxyo2malSU'  # Заміни на свій токен
gift_options = [0.0001, 0.1, 0.0002, 0.2, 0.5, 2]  # Варианти подарунків
user_data = {}  # Зберігання даних користувачів

# Час для отримання наступного подарунка в секундах (180 хвилин)
TIME_TO_WAIT = 180 * 60  

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    if user_id not in user_data:
        user_data[user_id] = {'gifts': 0, 'last_opened': 0}
    update.message.reply_text("Привіт! Ти можеш відкривати подарунки!")

def open_gifts(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    current_time = time.time()
    user = user_data[user_id]

    # Перевірка, чи можна відкрити подарунок
    if user['gifts'] < 5:
        gift = random.choice(gift_options)
        user['gifts'] += 1
        user['last_opened'] = current_time
        update.message.reply_text(f"Ти відкрив подарунок: {gift} TON/NOT/NEWYEARS!")

    elif (current_time - user['last_opened']) >= TIME_TO_WAIT:
        # Додатковий подарунок через 3 години
        gift = random.choice(gift_options)
        user['gifts'] += 1
        user['last_opened'] = current_time
        update.message.reply_text(f"Ти відкрив додатковий подарунок: {gift} TON/NOT/NEWYEARS!")
    else:
        # Визначення часу, що залишився до наступного відкриття подарунка
        time_left = TIME_TO_WAIT - (current_time - user['last_opened'])
        minutes_left = time_left // 60
        update.message.reply_text(f"Наступний подарунок можна відкрити через {minutes_left} хвилин.")

def exchange(update: Update, context: CallbackContext) -> None:
    # Логіка обміну подарунків
    pass

def withdraw(update: Update, context: CallbackContext) -> None:
    # Логіка виводу TON/NOT
    pass

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("open", open_gifts))
    dispatcher.add_handler(CommandHandler("exchange", exchange))
    dispatcher.add_handler(CommandHandler("withdraw", withdraw))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
