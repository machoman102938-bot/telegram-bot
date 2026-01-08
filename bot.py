from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes

TOKEN = "8308405546:AAHnXJhC5p9T36rEMONklZMXNdDI0UvpwTE"

app = ApplicationBuilder().token(TOKEN).build()
app.run_polling()