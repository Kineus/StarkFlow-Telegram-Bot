from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
from dotenv import load_dotenv
import os 
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Replace this with the link to your mini app
MINI_APP_URL = "https://t.me/starkflowbot/Starkmine"

async def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    
    keyboard = [
        [InlineKeyboardButton("Play This Game", url=MINI_APP_URL)],  # Open mini app
        [InlineKeyboardButton("Help", callback_data='help')],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_message(chat_id, text="Welcome! Play the game below:", reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    
    if query.data == 'help':
        await context.bot.answer_callback_query(query.id, text="Help message: How to play the game...")

async def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_error_handler(error)
    application.run_polling()

if __name__ == '__main__':
    main()
