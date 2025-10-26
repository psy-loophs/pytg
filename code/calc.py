from telegram import Update 
from telegram.ext import ContextTypes

active_user={}
entered_num={}
entered_num["number1"]=[]
entered_num["number2"]=[]



async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.message.from_user.id
    text = update.message.text.strip()

    
    if text == "/calc":
        active_user[uid] = True
        await update.message.reply_text("Enter first number:")
        return
        
             
           
    if uid in active_user:
        if text.isdigit():
            num1 = int(text)
            entered_num["number1"].append(num1)
        else:
          await update.message.reply_text("❌ Please send a valid first number.")
          del active_user[uid]
          return
          
           
        
  
    if uid in active_user:
      await update.message.reply_text("Enter second number:")
      return
      
    if uid in active_user:
      if text.isdigit():
        num2 = int(text)
        entered_num["number2"].append(num2)
      else:
        await update.message.reply_text("❌ Please send a valid second number.")
        del active_user[uid] 
        return
      
      
       await update.message.reply_text(num1 + num2)
       del active_user[uid]
       return
    
        
        

   

   
   
