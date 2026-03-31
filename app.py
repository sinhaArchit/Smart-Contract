from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes, CommandHandler

TOKEN = "8781779621:AAF25lkln_dk4Qmk3vOu7EbwEHq3hwbm6bY"

# Your file_ids
VIDEO_ID = "BAACAgUAAxkBAAMDacuzm4QVjgABRUNPpCGlJ-C5w_60AALtIwAC00BZVnVnU13tycxPOgQ"
AUDIO_ID = "CQACAgUAAxkBAAMIacu0FoNQy0ISsHKEp25_Gf6ZN3AAAvMcAAJca_FV5gIUaiEFKGo6BA"
APK_ID = "BQACAgUAAxkBAAMGacuz7vucSuKTXLT1fmTAg21REFYAAlAjAALTQFlWhBP9Kf9l2Ig6BA"

# 🔴 ADD YOUR ADMIN ID
ADMIN_ID = 7118492917

# ✅ MEMORY STORAGE
USERS = set()

def save_user(user_id):
    USERS.add(user_id)
    print("Saved user:", user_id)


# ✅ START COMMAND (register user)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    save_user(user_id)

    await update.message.reply_text("✅ You are registered!")


# ✅ BROADCAST
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    message = " ".join(context.args)

    if not message:
        await update.message.reply_text("❌ Usage: /broadcast your message")
        return

    success = 0
    failed = 0

    for user_id in USERS:
        try:
            await context.bot.send_message(chat_id=user_id, text=message)
            success += 1
        except Exception as e:
            print("Broadcast error:", e)
            failed += 1

    await update.message.reply_text(f"✅ Sent: {success}\n❌ Failed: {failed}")


# ================= YOUR ORIGINAL JOIN FLOW =================

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    chat_id = user.id
    name = user.first_name

    print("JOIN REQUEST RECEIVED:", name)

    # ✅ Save user
    save_user(chat_id)

    try:
        # Message
        await context.bot.send_message(
            chat_id=chat_id,
            text=f'''Hello dear {name}👋
Tumhari Join Request mil gayi hai ✅
Jaldi approve ho jayegi.

APK, Video aur Voice Guide niche diya hai 👇'''
        )

        # Video
        await context.bot.send_video(
            chat_id=chat_id,
            video=VIDEO_ID,
            caption='''👍 Full video watch karo 💥💥

🔗Link:
https://www.jaiclub01.com/#/register?invitationCode=24884129118'''
        )

        # APK
        await context.bot.send_document(
            chat_id=chat_id,
            document=APK_ID,
            caption='''👍 Full video watch karo 💥💥

Bro jaldi se hack INSTALL karo abhi only SURESHOT aa rha h is se pahle hack work na kare profit bna lo 🚀'''
        )

        # Audio
        await context.bot.send_audio(
            chat_id=chat_id,
            audio=AUDIO_ID,
            caption='''PURA VOICE SUNO OR KARO💯'''
        )

    except Exception as e:
        print("ERROR:", e)


# ================= APP =================

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("broadcast", broadcast))
app.add_handler(ChatJoinRequestHandler(handle_join_request))

app.run_polling()
