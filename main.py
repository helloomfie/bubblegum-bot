from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os
import re
import logging
from datetime import datetime

log_directory = "conversation_logs"
os.makedirs(log_directory, exist_ok=True)

log_filename = os.path.join(log_directory, f"conversations_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=log_filename, 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

async def handle_message(update, context):
    chat = update.effective_chat
    message = update.message
    text = message.text.lower()
    
    logging.info(f"User {message.from_user.username} (ID: {message.from_user.id}) sent: {text}")
    
    if message.from_user.username and message.from_user.username.lower() == 'rick':
        response = "i bought. can't resist a good gamble!"
        await chat.send_message(response)
        logging.info(f"Bot responded to Rick: {response}")
    
    elif re.search(r'\bbubblegum\b', text):
        response = "yes?"
        await message.reply_text(response)
        logging.info(f"Bot responded: {response}")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("starting bot...")
    application.run_polling()

if __name__ == '__main__':
    main()
