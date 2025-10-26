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
            num1 = int(text)
            entered_num["number"].append(num1)
    else:
           await update.message.reply_text("❌ Please send a valid number.")
           del user_waiting_for_number[uid] 
    
        
            
    if user_waiting_for_number[uid] is not None:
        await update.message.reply_text("Enter another number: ")
        
    if uid in user_waiting_for_number:
        if text.isdigit():
            num2=int(text)
            entered_num["number"].append(num2)
            await update.message.reply_text(num1 + num2)
            del user_waiting_for_number[uid]  
            
    else:
        await update.message.reply_text("❌ Please send a valid number.")
        return 
             
        
