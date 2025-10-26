from telegram import Update
from telegram.ext import ContextTypes

user_waiting_for_number = {}  # Tracks which number the user is entering
entered_num = {}              # Stores user numbers

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.message.from_user.id
    text = update.message.text.strip()

    # Start the calculation
    if text == "/calc":
        user_waiting_for_number[uid] = 1  # 1 = waiting for first number
        entered_num[uid] = []
        await update.message.reply_text("Enter the first number:")
        return

    # Check if user is in calculation flow
    if uid in user_waiting_for_number:
        if text.isdigit():
            num = int(text)
            entered_num[uid].append(num)
            
            if user_waiting_for_number[uid] == 1:
                user_waiting_for_number[uid] = 2
                await update.message.reply_text("Enter the second number:")
            elif user_waiting_for_number[uid] == 2:
                total = sum(entered_num[uid])
                await update.message.reply_text(f"The sum is: {total}")
                # Cleanup
                del user_waiting_for_number[uid]
                del entered_num[uid]
        else:
            await update.message.reply_text("❌ Please send a valid number.")
    else:
        # User not in calculation mode
        if text.startswith("/"):
            return  # Ignore other commands
        await update.message.reply_text("Send /calc to start a calculation.")
