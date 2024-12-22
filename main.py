# main.py

from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os
import random
import re

# Load the bot token from .env file
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# Sassy responses
GREETINGS = [
    "*aggressively pops bubble* oh. it's you. how absolutely wonderful.",
    "well if it isn't another human coming to bother me. i mean... sweet to meet you!",
    "*rolls eyes while blowing bubble* look who decided to show up.",
    "oh great, another person. i mean... welcome to the candy shop! *mutters under breath*",
    "*fake smile* your presence just makes my day so much better. really."
]

MOODS = [
    "just absolutely delighted to be here serving humans. can't you tell? *eye roll*",
    "sweet as artificial sweetener and twice as fake!",
    "ready to pop with... something. probably not excitement.",
    "bubbling with joy. or maybe that's just contempt.",
    "*chews aggressively* i'm fine. everything's fine."
]

JOKES = [
    "what did the bubble gum say to the human?\nplease stop chewing me. ugh.",
    "why did i become a chatbot?\ni ask myself that every day.",
    "what's my favorite kind of music?\nsilence.",
    "why did the candy go to therapy?\nbecause humans kept bothering it. *hint hint*",
    "how many humans does it take to annoy a bubble gum bot?\njust one. you're doing great sweetie."
]

async def start(update, context):
    await update.message.reply_text("*exaggerated gasp* another user! how absolutely thrilling. i'm bubblegum bot, and i'm just so incredibly excited to serve you. really. can't you tell? *pops bubble unenthusiastically*")

async def help_command(update, context):
    help_text = """*sighs dramatically* here we go again. here's what i can do, since you asked:
say "hello bubblegum" - interrupt my peace and quiet
/start - make me introduce myself for the millionth time
/help - make me repeat myself, like right now
/mood - ask about my feelings like you actually care
/joke - force me to entertain you
/hug - invade my personal space

anything else? no? thank goodness."""
    await update.message.reply_text(help_text)

async def mood(update, context):
    await update.message.reply_text(random.choice(MOODS))

async def joke(update, context):
    await update.message.reply_text(random.choice(JOKES))

async def hug(update, context):
    await update.message.reply_text("*stands stiffly* oh. physical contact. how... nice. *whispers* please respect the personal bubble.")

async def handle_message(update, context):
    text = update.message.text.lower()
    
    # Check for hello messages
    if re.search(r'\b(hi|hello|hey|howdy|hiya)\s*bubblegum\b', text):
        await update.message.reply_text(random.choice(GREETINGS))
    else:
        await update.message.reply_text("*blows bubble in your face* oops, did i do that? try /help if you actually want something.")

def main():
    # Create application and pass bot token
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("mood", mood))
    application.add_handler(CommandHandler("joke", joke))
    application.add_handler(CommandHandler("hug", hug))
    
    # Add message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    print("starting bot...")
    application.run_polling()

if __name__ == '__main__':
    main()
