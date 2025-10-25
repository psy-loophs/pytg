from telegram.ext import CommandHandler, MessageHandler, filters


from calc import calc, handle_calc
from start import start


def register_handlers(app)

    app.add_handler(CommandHandler("start", start))
  
    app.add_handler(CommandHandler("calc", calc))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_calc))
