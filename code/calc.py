from telegram import Update 
from telegram.ext import ContextTypes

user_waiting_for_number={}
entered_num={}
entered_num["numbers"]=[]

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.message.from_user.id
    text = update.message.text.strip()

    
    if text == "/calc":
        user_waiting_for_number[uid] = True
        await update.message.reply_text("Enter a number:")
        
             
           
    if uid in user_waiting_for_number:
        if text.isdigit():
            num = entered_num["number"]
    else:
           await update.message.reply_text("❌ Please send a valid number.")
           del user_waiting_for_number[uid] 
    
        
            
    if uid in user_waiting_for_number and user_waiting_for_number[uid] is not None:
        await update.message.reply_text("Enter another number: ")
        
    if uid in user_waiting_for_number:
        if text.isdigit():
            num1=int(text)
            await update.message.reply_text(num + num1)
            
            del user_waiting_for_number[uid]  
                
    else:
        await update.message.reply_text("❌ Please send a valid number.")
        return 
             
        
