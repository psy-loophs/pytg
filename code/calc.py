from telegram import Update 
from telegram.ext import ContextTypes

num=0
async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Enter a number: ")
return num

async def handle_calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.isdigit():
        num = int(text)
        await update.message.reply_text(f"You entered {num}.")
    else:
        await update.message.reply_text("❌ Please send a valid number.")
      

