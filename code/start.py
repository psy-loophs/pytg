from telegram import Update 
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    uid = update.message.from_user.id  
    if uid in user_waiting_for_number:
        del user_waiting_for_number[uid]
        
    await update.message.reply_text("Hello, from python 👋")


