from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import languages
import config

def language_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🇮🇷 فارسی", callback_data="lang_fa"),
            InlineKeyboardButton("🇺🇸 English", callback_data="lang_en"),
        ]
    ])


def join_keyboard(lang="fa"):
    t = languages.TEXT[lang]

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                t["join_btn"],
                url=f"https://t.me/{config.CHANNEL_USERNAME.replace('@','')}"
            )
        ],
        [
            InlineKeyboardButton(
                t["joined"],
                callback_data="check_join"
            )
        ]
    ])


def main_menu(lang="fa"):

    t = languages.TEXT[lang]

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                t["stars"],
                callback_data="stars"
            )
        ],

        [
            InlineKeyboardButton(
                t["premium"],
                callback_data="premium"
            )
        ],

        [
            InlineKeyboardButton(
                t["pubg"],
                callback_data="pubg"
            )
        ],

        [
            InlineKeyboardButton(
                t["cod"],
                callback_data="cod"
            )
        ],

        [
            InlineKeyboardButton(
                t["support"],
                url=f"https://t.me/{config.SUPPORT_USERNAME.replace('@','')}"
            )
        ]

    ])# =========================
# Premium Menu
# =========================

def premium_menu():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "💎 3 Months",
                callback_data="buy_Premium 3 Months"
            )
        ],

        [
            InlineKeyboardButton(
                "💎 6 Months",
                callback_data="buy_Premium 6 Months"
            )
        ],

        [
            InlineKeyboardButton(
                "💎 12 Months",
                callback_data="buy_Premium 12 Months"
            )
        ],

        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back"
            )
        ]

    ])


# =========================
# Stars Menu
# =========================

def stars_menu():

    return InlineKeyboardMarkup([

        [InlineKeyboardButton("⭐ 50 Stars", callback_data="buy_50 Stars")],
        [InlineKeyboardButton("⭐ 100 Stars", callback_data="buy_100 Stars")],
        [InlineKeyboardButton("⭐ 250 Stars", callback_data="buy_250 Stars")],
        [InlineKeyboardButton("⭐ 500 Stars", callback_data="buy_500 Stars")],
        [InlineKeyboardButton("⭐ 1000 Stars", callback_data="buy_1000 Stars")],
        [InlineKeyboardButton("⭐ 2500 Stars", callback_data="buy_2500 Stars")],

        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back"
            )
        ]

    ])


# =========================
# PUBG Menu
# =========================

def pubg_menu():

    return InlineKeyboardMarkup([

        [InlineKeyboardButton("🎮 60 UC", callback_data="buy_60 UC")],
        [InlineKeyboardButton("🎮 325 UC", callback_data="buy_325 UC")],
        [InlineKeyboardButton("🎮 660 UC", callback_data="buy_660 UC")],
        [InlineKeyboardButton("🎮 1800 UC", callback_data="buy_1800 UC")],
        [InlineKeyboardButton("🎮 3850 UC", callback_data="buy_3850 UC")],
        [InlineKeyboardButton("🎮 8100 UC", callback_data="buy_8100 UC")],
        [InlineKeyboardButton("🎮 16200 UC", callback_data="buy_16200 UC")],
        [InlineKeyboardButton("🎮 24300 UC", callback_data="buy_24300 UC")],

        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back"
            )
        ]

    ])


# =========================
# COD Menu
# =========================

def cod_menu():

   
