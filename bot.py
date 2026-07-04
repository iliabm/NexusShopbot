from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

import config
import database
import keyboards
import languages
import admin


# =========================
# Check Join
# =========================

async def is_joined(bot, user_id):

    try:

        member = await bot.get_chat_member(
            config.CHANNEL_USERNAME,
            user_id
        )

        return member.status in [
            "member",
            "administrator",
            "owner"
        ]

    except:

        return False


# =========================
# /start
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    database.add_user(user.id)

    await update.message.reply_text(

        "🌍 لطفاً زبان خود را انتخاب کنید\n\nPlease choose your language",

        reply_markup=keyboards.language_keyboard()

    )


# =========================
# Buttons
# =========================

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    user = query.from_user    # =========================
    # Language Selection
    # =========================

    if query.data == "lang_fa":

        joined = await is_joined(context.bot, user.id)

        if not joined:

            await query.message.edit_text(
                languages.TEXT["fa"]["join"],
                reply_markup=keyboards.join_keyboard("fa")
            )

            return

        await query.message.edit_text(
            languages.TEXT["fa"]["welcome"],
            reply_markup=keyboards.main_menu("fa")
        )

        return

    if query.data == "lang_en":

        joined = await is_joined(context.bot, user.id)

        if not joined:

            await query.message.edit_text(
                languages.TEXT["en"]["join"],
                reply_markup=keyboards.join_keyboard("en")
            )

            return

        await query.message.edit_text(
            languages.TEXT["en"]["welcome"],
            reply_markup=keyboards.main_menu("en")
        )

        return

    # =========================
    # Check Join Button
    # =========================

    if query.data == "check_join":

        joined = await is_joined(context.bot, user.id)

        if not joined:

            await query.answer(
                "❌ ابتدا عضو کانال شوید.",
                show_alert=True
            )

            return

        await query.message.edit_text(
            languages.TEXT["fa"]["welcome"],
            reply_markup=keyboards.main_menu("fa")
        )

        return    # =========================
    # Main Menu
    # =========================

    if query.data == "premium":

        await query.message.edit_text(

            "💎 Telegram Premium\n\n"
            "یکی از پلن‌ها را انتخاب کنید:",

            reply_markup=keyboards.premium_menu()

        )

        return


    if query.data == "stars":

        await query.message.edit_text(

            "⭐ Telegram Stars\n\n"
            "تعداد استار مورد نظر را انتخاب کنید:",

            reply_markup=keyboards.stars_menu()

        )

        return


    if query.data == "pubg":

        await query.message.edit_text(

            "🎮 PUBG UC\n\n"
            "پکیج مورد نظر را انتخاب کنید:",

            reply_markup=keyboards.pubg_menu()

        )

        return


    if query.data == "cod":

        await query.message.edit_text(

            "🎯 Call Of Duty CP\n\n"
            "پکیج مورد نظر را انتخاب کنید:",

            reply_markup=keyboards.cod_menu()

        )

        return    # =========================
    # Payment
    # =========================

    if query.data.startswith("buy_"):

        product = query.data.replace("buy_", "")

        text = f"""
✅ سفارش شما ثبت شد.

🛒 محصول:
{product}

━━━━━━━━━━━━━━

💳 شماره کارت:

{config.CARD_NUMBER}

👤 صاحب کارت:

{config.CARD_OWNER}

━━━━━━━━━━━━━━

📩 بعد از پرداخت،
رسید پرداخت را برای پشتیبانی ارسال کنید.

👨‍💻 پشتیبانی:

{config.SUPPORT_USERNAME}
"""

        database.add_order(
            user.id,
            product
        )

        await admin.send_order(
            context.bot,
            user,
            product
        )

        await query.message.edit_text(text)

        return    # =========================
    # Buy Products
    # =========================

    if query.data.startswith("buy_"):

        product = query.data.replace("buy_", "")

        database.add_order(
            user.id,
            product
        )

        await admin.send_order(
            context.bot,
            user,
            product
        )

        text = f"""
✅ سفارش شما ثبت شد.

━━━━━━━━━━━━━━

🛒 محصول:

{product}

━━━━━━━━━━━━━━

💳 شماره کارت:

{config.CARD_NUMBER}

👤 صاحب کارت:

{config.CARD_OWNER}

━━━━━━━━━━━━━━

📩 بعد از پرداخت،
رسید را برای پشتیبانی ارسال کنید.

{config.SUPPORT_USERNAME}
"""

        await query.message.edit_text(text)

        return    # =========================
    # Back To Main Menu
    # =========================

    if query.data == "back":

        lang = database.get_user_language(user.id)

        await query.message.edit_text(
            languages.TEXT[lang]["welcome"],
            reply_markup=keyboards.main_menu(lang)
        )

        return# =========================
# Run Bot
# =========================

app = Application.builder().token(config.BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("admin", admin.admin_panel))
app.add_handler(CommandHandler("orders", admin.orders))
app.add_handler(CallbackQueryHandler(buttons))

print("🚀 Nexus Shop Bot Started")

app.run_polling()
      
  
