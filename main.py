from telegram.ext import Application, CommandHandler, MessageHandler, filters
from token import BOT_TOKEN
import random
import requests
# python-telegram-bot


async def start(update, context):
    await update.message.reply_text("Здравствуйте, добро пожаловать")


async def chat(update, context):
    pass


app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
app.run_polling()
