from telegram import Update 
from telegram.ext import ContextTypes

user_waiting_for_number={}

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.message.from_user.id
    text = update.message.text.strip()

    
        
        
        
        
        
        
        


    if text == "/calc":
        user_waiting_for_number[uid] = True
        await update.message.reply_text("Enter a number:")
        return
    if uid in user_waiting_for_number:
        if text.startswith("/") and not text.startswith("/calc"):
          del user_waiting_for_number[uid]  
          return
          
           
    if uid in user_waiting_for_number:
        if text.isdigit():
            num = int(text)
            await update.message.reply_text(f"You entered {num}. ✅")
            del user_waiting_for_number[uid]  
        else:
            await update.message.reply_text("❌ Please send a valid number.")
            user_waiting_for_number[uid] = True
            return 
            
        
                
            
       
    
