from telegram import Update 
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, from python 👋")

num=int(input("Enter a number"))
async def calc(update: Update,context: ContextTypes.Default_Types):
    await update.messsage.reply_text("Entered number is ",num)

