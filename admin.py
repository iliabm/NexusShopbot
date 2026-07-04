from telegram import Update
from telegram.ext import ContextTypes
import config
import database


async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != config.ADMIN_ID:
        await update.message.reply_text("❌ شما ادمین نیستید.")
        return

    orders = database.get_orders()

    if len(orders) == 0:
        await update.message.reply_text("📦 هنوز سفارشی ثبت نشده است.")
        return

    text = "📋 لیست سفارش‌ها\n\n"

    for order in orders:

        text += (
            f"🆔 سفارش: {order[0]}\n"
            f"👤 کاربر: {order[1]}\n"
            f"🛍 محصول: {order[2]}\n"
            f"📦 تعداد: {order[3]}\n"
            f"📌 وضعیت: {order[4]}\n\n"
        )

    await update.message.reply_text(text)


async def notify_admin(bot, user_id, product, quantity):

    text = (
        "🆕 سفارش جدید\n\n"
        f"👤 User ID : {user_id}\n"
        f"🛍 Product : {product}\n"
        f"📦 Quantity : {quantity}"
    )

    await bot.send_message(
        chat_id=config.ADMIN_ID,
        text=text
    )
