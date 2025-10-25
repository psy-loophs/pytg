import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from handle import register_handles

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
