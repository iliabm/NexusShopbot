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

    ])
