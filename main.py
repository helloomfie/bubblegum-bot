# main.py
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os
import re

# Load the bot token from .env file
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

async def handle_message(update, context):
    chat = update.effective_chat
    message = update.message
    text = message.text.lower()

    if message.reply_to_message and message.reply_to_message.from_user.username == 'Rick':
        await chat.send_message("i bought. can't resist a good gamble!")
    elif re.search(r'\bbubblegum\b', text):
        await message.reply_text("yes?")

def main():
    # Create application and pass bot token
    application = Application.builder().token(TOKEN).build()

    # Add message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    print("starting bot...")
    application.run_polling()

if __name__ == '__main__':
    main()
