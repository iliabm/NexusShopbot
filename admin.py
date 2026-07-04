from telegram import Update
from telegram.ext import ContextTypes
import database
import config


async def send_order(bot, user, product):

    text = f"""
🛒 سفارش جدید

👤 نام:
{user.full_name}

🆔 آیدی:
{user.id}

📛 یوزرنیم:
@{user.username if user.username else "ندارد"}

📦 محصول:
{product}
"""

    await bot.send_message(
        chat_id=config.ADMIN_ID,
        text=text
    )


async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != config.ADMIN_ID:

        await update.message.reply_text("⛔ دسترسی ندارید.")
        return

    users = database.get_user_count()
    orders = database.get_order_count()

    text = f"""
👨‍💻 پنل مدیریت Nexus

━━━━━━━━━━━━━━

👥 تعداد کاربران:
{users}

📦 تعداد سفارش‌ها:
{orders}

━━━━━━━━━━━━━━

برای مشاهده سفارش‌ها:

/orders
"""

    await update.message.reply_text(text)


async def orders(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != config.ADMIN_ID:
        return

    data = database.get_orders()

    if not data:

        await update.message.reply_text("📭 هنوز سفارشی ثبت نشده.")
        return

    text = "📦 لیست سفارش‌ها\n\n"

    for order in data:

        text += (
            f"🆔 {order[0]}\n"
            f"
