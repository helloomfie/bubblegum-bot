# main.py
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os
import re
import logging
from datetime import datetime

# Set up logging
log_directory = "conversation_logs"
os.makedirs(log_directory, exist_ok=True)

# Create a log file with today's date
log_filename = os.path.join(log_directory, f"conversations_{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure logging
logging.basicConfig(
    filename=log_filename, 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Load the bot token from .env file
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

async def handle_message(update, context):
    chat = update.effective_chat
    message = update.message
    text = message.text.lower()
    
    # Log the incoming message
    logging.info(f"User {message.from_user.username} (ID: {message.from_user.id}) sent: {text}")
    
    # Respond whenever Rick talks
    if message.from_user.username and message.from_user.username.lower() == 'rick':
        response = "i bought. can't resist a good gamble!"
        await chat.send_message(response)
        logging.info(f"Bot responded to Rick: {response}")
    
    # Existing bubblegum response
    elif re.search(r'\bbubblegum\b', text):
        response = "yes?"
        await message.reply_text(response)
        logging.info(f"Bot responded: {response}")

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
