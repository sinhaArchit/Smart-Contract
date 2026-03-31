from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

TOKEN = "8781779621:AAF25lkln_dk4Qmk3vOu7EbwEHq3hwbm6bY"

# Your UPDATED file_ids
VIDEO_ID = "BAACAgUAAxkBAAMDacuzm4QVjgABRUNPpCGlJ-C5w_60AALtIwAC00BZVnVnU13tycxPOgQ"
AUDIO_ID = "CQACAgUAAxkBAAMIacu0FoNQy0ISsHKEp25_Gf6ZN3AAAvMcAAJca_FV5gIUaiEFKGo6BA"
APK_ID = "BQACAgUAAxkBAAMGacuz7vucSuKTXLT1fmTAg21REFYAAlAjAALTQFlWhBP9Kf9l2Ig6BA"

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    chat_id = user.id  # DM the user

    name = user.first_name

    # Send message
    await context.bot.send_message(chat_id=chat_id, text=f'''Hello dear {name}👋
Tumhari Join Request mil gayi hai ✅
Jaldi approve ho jayegi.

APK, Video aur Voice Guide niche diya hai 👇''')

    # Send files
    await context.bot.send_video(chat_id=chat_id, video=VIDEO_ID , caption='''👍 Full video watch karo 💥💥

🔗Link:
https://www.jaiclub01.com/#/register?invitationCode=24884129118''')

    await context.bot.send_document(chat_id=chat_id, document=APK_ID, caption='''👍 Full video watch karo 💥💥

Bro jaldi se hack INSTALL karo abhi only SURESHOT aa rha h is se pahle hack work na kare profit bna lo 🚀''')

    await context.bot.send_audio(chat_id=chat_id, audio=AUDIO_ID , caption='''PURA VOICE SUNO OR KARO💯''')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(ChatJoinRequestHandler(handle_join_request))

app.run_polling()