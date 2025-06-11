import telebot
from telebot import types

# --- НАСТРОЙКИ ---
TOKEN = '7529240199:AAFu6u_9zXCynLb8g02FDsqQgLfMS3Zd3NM'
CHANNEL_ID = '@vertuu_crypto'  # Укажите ID вашего канала, например, @mychannel
# -----------------

bot = telebot.TeleBot(TOKEN)
user_language = {} # Словарь для хранения языка каждого пользователя

# --- ВСЕ ТЕКСТЫ БОТА ---
# Структура: 'ключ_сообщения': {'ru': 'Текст на русском', 'ua': 'Текст на українській', 'en': 'Text in English'}
texts = {
    'start_prompt': {
        'ru': ("Для использования этого бота, сначала подпишись на @vertuu_crypto🤝\n"
               "—————————————————————\n"
               "To use this bot, first subscribe to @vertuu_crypto🤝\n"
               "—————————————————————\n"
               "Для користування цим ботом, спершу підпишись на @vertuu_crypto🤝"),
        'ua': ("Для користування цим ботом, спершу підпишись на @vertuu_crypto🤝\n"
               "—————————————————————\n"
               "Для использования этого бота, сначала подпишись на @vertuu_crypto🤝\n"
               "—————————————————————\n"
               "To use this bot, first subscribe to @vertuu_crypto🤝"),
        'en': ("To use this bot, first subscribe to @vertuu_crypto🤝\n"
               "—————————————————————\n"
               "Для использования этого бота, сначала подпишись на @vertuu_crypto🤝\n"
               "—————————————————————\n"
               "Для користування цим ботом, спершу підпишись на @vertuu_crypto🤝")
    },
    'subscribe_button': {'ru': "Перейти в канал", 'ua': "Перейти в канал", 'en': "Go to Channel"},
    'check_button': {'ru': "Проверить ✅", 'ua': "Перевірити ✅", 'en': "Check ✅"},
    'subscribed_success': {
        'ru': "Вы успешно подписаны на канал! Давайте продолжим.",
        'ua': "Ви успішно підписані на канал! Давайте продовжимо.",
        'en': "You have successfully subscribed to the channel! Let's continue."
    },
    'not_subscribed': {'ru': "Вы не подписаны на канал.", 'ua': "Ви не підписані на канал.", 'en': "You are not subscribed to the channel."},
    'choose_language': {'ru': "Привіт! Оберіть мову:", 'ua': "Привіт! Оберіть мову:", 'en': "Hello! Choose your language:"},
    'language_selected': {
        'ru': "Вы выбрали язык: Русский\n\nВыберите, что вас интересует:\n👇🏻",
        'ua': "Ви обрали мову: Українська\n\nОберіть, що вас цікавить:\n👇🏻",
        'en': "You have selected language: English\n\nSelect what you are interested in:\n👇🏻"
    },
    'main_menu_prompt': {'ru': "Главное меню", 'ua': "Головне меню", 'en': "Main menu"},
    'menu_buttons': {
        'reklama': {'ru': "📢 Реклама", 'ua': "📢 Реклама", 'en': "📢 Advertising"},
        'kontakty': {'ru': "👤 Контакты", 'ua': "👤 Контакти", 'en': "👤 Contacts"},
        'otzivi': {'ru': "✍️ Отзывы", 'ua': "✍️ Відгуки", 'en': "✍️ Reviews"},
        'proekti': {'ru': "🚀 Проекты", 'ua': "🚀 Проекти", 'en': "🚀 Projects"},
        'ekosistema': {'ru': '🌍 Экосистема "Мир"', 'ua': '🌍 Екосистема "Мир"', 'en': '🌍 "Mir" Ecosystem'}
    },
    'responses': {
        'reklama': {
            'ru': ("Цены на рекламу:\n"
                   "@vertuu_accounts — пост от 30$.\n"
                   "@small_accounts — пост от 25$.\n"
                   "@ua_pubgm_store — пост от 30$.\n"
                   "@vertuu_rent — пост от 10$.\n"
                   "——————————————————\n"
                   "@pubgmMIR — пост от 15$.\n"
                   "@pubgmMIR_ads — пост от 1$.\n"
                   "@pubgmMIR_news — пост от 7$."),
            'ua': ("Ціни на рекламу:\n"
                   "@vertuu_accounts — пост від 30$.\n"
                   "@small_accounts — пост від 25$.\n"
                   "@ua_pubgm_store — пост від 30$.\n"
                   "@vertuu_rent — пост від 10$.\n"
                   "——————————————————\n"
                   "@pubgmMIR — пост від 15$.\n"
                   "@pubgmMIR_ads — пост від 1$.\n"
                   "@pubgmMIR_news — пост від 7$."),
            'en': ("Advertising prices:\n"
                   "@vertuu_accounts — post from $30.\n"
                   "@small_accounts — post from $25.\n"
                   "@ua_pubgm_store — post from $30.\n"
                   "@vertuu_rent — post from $10.\n"
                   "——————————————————\n"
                   "@pubgmMIR — post from $15.\n"
                   "@pubgmMIR_ads — post from $1.\n"
                   "@pubgmMIR_news — post from $7.")
        },
        'kontakty': {
            'ru': ("Официальные контакты:\n\n"
                   "1. @vrt484 – Я, мой личный контакт. Единственный телеграмм, других нет. Провожу сделки по продаже чего угодно ценой выше 5000₴(120$/11к₽). Также обращайтесь за покупкой личного аккаунта с гарантией или дешевой подписки Telegram Premium.\n\n"
                   "2. @vertuu_admin – мой помощник, гарант сделок до 5000₴(120$/11к₽) и обменов.\n\n"
                   "3. @uc_mir_admin – обращайтесь по покупки UC в рублях.\n\n"
                   "4. Магазин N1 UC SHOP:\n• @UC_SHOP_ADMIN – UC по ID, пп, жетоны спорткаров и т.д. (гривны).\n• @UC_LOGIN_ADMIN – донат по входу (гривны).\n\n"
                   "5. Магазин UA PUBGM STORE:\n• @vertuu_admin – чтобы выложить аккаунт на продажу, для связи с продавцом товара, проведения сделки, а также поможет подобрать нужный аккаунт.\n• @clans_trade – покупка/продажа кланов.\n\n"
                   "6. @SA_seller – для покупки личного аккаунта с гарантией, ценой до 300$.\n\n"
                   "7. @orenda_admin – взять аккаунт в аренду.\n\n"
                   "8. @cht_sup – главный по чату @UA_STORE_CHAT.\n\n"
                   "9. @vertuu_hacks_admin – для покупки читов.\n\n"
                   "10. @currency_exchanging – обменник валют, международные переводы, поможет вывести или купить крипту, продаст вирт номер, поставит за вас ставку.\n\n"
                   "11. Канал VERTUU HELP:\n• @vertuu_help – помощь с аккаунтом (рес/антирес, отвязка привязок и т.п.).\n• @vertuu_osint – пробив личных данных скамера и подобные услуги.\n\n"
                   "12. @cards_rent – ​​возьмет карту в аренду."),
            'ua': ("Офіційні контакти:\n\n"
                   "1. @vrt484 – Я, мій особистий контакт. Єдиний телеграм, інших немає. Проводжу угоди з продажу будь-чого ціною вище 5000₴(120$/11к₽). Також звертайтесь за покупкою особистого облікового запису з гарантією або дешевої підписки Telegram Premium.\n\n"
                   "2. @vertuu_admin – мій помічник, гарант угод до 5000₴(120$/11к₽) та обмінів.\n\n"
                   "3. @uc_mir_admin – звертайтесь щодо покупки UC в рублях.\n\n"
                   "4. Магазин N1 UC SHOP:\n• @UC_SHOP_ADMIN – UC за ID, пп, жетони спорткарів тощо (гривні).\n• @UC_LOGIN_ADMIN – донат за входом (гривні).\n\n"
                   "5. Магазин UA PUBGM STORE:\n• @vertuu_admin – щоб викласти обліковий запис на продаж, для зв'язку з продавцем товару, проведення угоди, а також допоможе підібрати потрібний обліковий запис.\n• @clans_trade – купівля/продаж кланів.\n\n"
                   "6. @SA_seller – для покупки особистого облікового запису з гарантією, ціною до 300$.\n\n"
                   "7. @orenda_admin – взяти обліковий запис в оренду.\n\n"
                   "8. @cht_sup – головний у чаті @UA_STORE_CHAT.\n\n"
                   "9. @vertuu_hacks_admin – для покупки читів.\n\n"
                   "10. @currency_exchanging – обмінник валют, міжнародні перекази, допоможе вивести чи купити крипту, продасть вірт номер, поставить за вас ставку.\n\n"
                   "11. Канал VERTUU HELP:\n• @vertuu_help – допомога з обліковим записом (рес/антирес, відв'язування прив'язок тощо).\n• @vertuu_osint – пробив особистих даних скамера та подібні послуги.\n\n"
                   "12. @cards_rent – ​​візьме картку в оренду."),
            'en': ("Official contacts:\n\n"
                   "1. @vrt484 – Me, my personal contact. The only Telegram account, no others. I conduct deals for selling anything priced above 5000 UAH ($120/11k RUB). Also, contact me for purchasing a personal account with a guarantee or a cheap Telegram Premium subscription.\n\n"
                   "2. @vertuu_admin – my assistant, guarantor for deals up to 5000 UAH ($120/11k RUB) and exchanges.\n\n"
                   "3. @uc_mir_admin – contact for purchasing UC in rubles.\n\n"
                   "4. N1 UC SHOP Store:\n• @UC_SHOP_ADMIN – UC by ID, pps, sports car tokens, etc. (hryvnia).\n• @UC_LOGIN_ADMIN – donation by login (hryvnia).\n\n"
                   "5. UA PUBGM STORE Store:\n• @vertuu_admin – to list an account for sale, to contact the seller, conduct a deal, and help select the right account.\n• @clans_trade – buying/selling clans.\n\n"
                   "6. @SA_seller – for purchasing a personal account with a guarantee, priced up to $300.\n\n"
                   "7. @orenda_admin – to rent an account.\n\n"
                   "8. @cht_sup – head of the @UA_STORE_CHAT.\n\n"
                   "9. @vertuu_hacks_admin – for purchasing cheats.\n\n"
                   "10. @currency_exchanging – currency exchanger, international transfers, helps to withdraw or buy crypto, sells virtual numbers, places bets for you.\n\n"
                   "11. VERTUU HELP Channel:\n• @vertuu_help – assistance with accounts (res/anti-res, unlinking, etc.).\n• @vertuu_osint – doxing of scammers and similar services.\n\n"
                   "12. @cards_rent – will rent a card.")
        },
        'otzivi': {
            'ru': ("Отдельные топ-кейсы:\n\n"
                   "• Самая большая сделка во всем СНГ:\nhttps://t.me/vertuu_accounts/3005\n\n"
                   "• Самая большая сделка в Украине:\nhttps://t.me/vertuu_accounts/2888\n\n"
                   "• Покупка аккаунта за 5000$:\nhttps://t.me/vidguky_ua/11343\n\n"
                   "• Единоразовая покупка 165000 UC по входу:\nhttps://t.me/vidguky_ua/11379\n"
                   "——————————————————\n"
                   "Всего свыше 35k отзывов, почитать их можно здесь:\nt.me/addlist/_w9B7KIq36c4NWUy"),
            'ua': ("Окремі топ-кейси:\n\n"
                   "• Найбільша угода у всьому СНД:\nhttps://t.me/vertuu_accounts/3005\n\n"
                   "• Найбільша угода в Україні:\nhttps://t.me/vertuu_accounts/2888\n\n"
                   "• Купівля акаунта за 5000$:\nhttps://t.me/vidguky_ua/11343\n\n"
                   "• Одноразова покупка 165000 UC за входом:\nhttps://t.me/vidguky_ua/11379\n"
                   "——————————————————\n"
                   "Всього понад 35k відгуків, почитати їх можна тут:\nt.me/addlist/_w9B7KIq36c4NWUy"),
            'en': ("Separate top cases:\n\n"
                   "• The largest deal in the entire CIS:\nhttps://t.me/vertuu_accounts/3005\n\n"
                   "• The largest deal in Ukraine:\nhttps://t.me/vertuu_accounts/2888\n\n"
                   "• Account purchase for $5000:\nhttps://t.me/vidguky_ua/11343\n\n"
                   "• One-time purchase of 165,000 UC via login:\nhttps://t.me/vidguky_ua/11379\n"
                   "——————————————————\n"
                   "Over 35k reviews in total, you can read them here:\nt.me/addlist/_w9B7KIq36c4NWUy")
        },
        'proekti': {
            'ru': ("Основные проекты:\n\n"
                   "1. @pubgmMIR_UC – магазин UC для снг пользователей.\n"
                   "2. @N1_UC_SHOP – магазин UC для пользователей с Украины.\n"
                   "3. @VERTUU_ACCOUNTS – продажа личных аккаунтов С ГАРАНТИЕЙ!\n"
                   "4. @SMALL_ACCOUNTS – продажа личных аккаунтов С ГАРАНТИЕЙ, но ценовая категория до 300$.\n"
                   "5. @VERTUU_RENT – аренда жирных и редких аккаунтов.\n"
                   "6. @VERTUUHACKS – магазин читов.\n"
                   "7. @SCAMMERS_SPAWN – скам-база, где постим айди рес-аккаунтом, а так же контакты мошенников.\n"
                   "8. @VERTUU_ACCOUNT_HELP – обслуживание аккаунта (рес/антирес, бан/разбан и тд. тп.) + OSINT-услуги по типу пробива данных, защиты от пробива и т.д.\n"
                   "9. @VERTUU_PREMIUM – магазин дешевых подписок Telegram Premium.\n"
                   "10. @EXCHANGERIN – обменник валют, поможет купить/продать крипту, продаст вирт номер или же поставит на вас ставку.\n"
                   "11. @VERTUU_CRYPTO – личный канал о крипте, интересные советы, проекты и тд.\n"
                   "12. @UA_PUBGM_STORE – магазин аккаунтов (публичных), можно выложить на продажу любой цифровой товар.\n"
                   "13. @UA_STORE_CHAT – чат магазина аккаунтов (публичных).\n"
                   "14. @TOURNAMENTS_PM – турниры Pubg Mobile (пока афк).\n"
                   "15. @UA_TDM_PLATFORM – тдм-турниры, новости из мира TDM и т.д (афк)."),
            'ua': ("Основні проекти:\n\n"
                   "1. @pubgmMIR_UC – магазин UC для користувачів СНД.\n"
                   "2. @N1_UC_SHOP – магазин UC для користувачів з України.\n"
                   "3. @VERTUU_ACCOUNTS – продаж особистих акаунтів З ГАРАНТІЄЮ!\n"
                   "4. @SMALL_ACCOUNTS – продаж особистих акаунтів З ГАРАНТІЄЮ, але цінова категорія до 300$.\n"
                   "5. @VERTUU_RENT – оренда жирних та рідкісних акаунтів.\n"
                   "6. @VERTUUHACKS – магазин читів.\n"
                   "7. @SCAMMERS_SPAWN – скам-база, де постимо айді рес-акаунтів, а також контакти шахраїв.\n"
                   "8. @VERTUU_ACCOUNT_HELP – обслуговування акаунта (рес/антирес, бан/розбан і т.д.) + OSINT-послуги типу пробиву даних, захисту від пробиву і т.д.\n"
                   "9. @VERTUU_PREMIUM – магазин дешевих підписок Telegram Premium.\n"
                   "10. @EXCHANGERIN – обмінник валют, допоможе купити/продати крипту, продасть вірт номер або ж поставить за вас ставку.\n"
                   "11. @VERTUU_CRYPTO – особистий канал про крипту, цікаві поради, проекти і т.д.\n"
                   "12. @UA_PUBGM_STORE – магазин акаунтів (публічних), можна виставити на продаж будь-який цифровой товар.\n"
                   "13. @UA_STORE_CHAT – чат магазину акаунтів (публічних).\n"
                   "14. @TOURNAMENTS_PM – турніри Pubg Mobile (поки афк).\n"
                   "15. @UA_TDM_PLATFORM – тдм-турніри, новини зі світу TDM і т.д (афк)."),
            'en': ("Main projects:\n\n"
                   "1. @pubgmMIR_UC – UC store for CIS users.\n"
                   "2. @N1_UC_SHOP – UC store for users from Ukraine.\n"
                   "3. @VERTUU_ACCOUNTS – sale of personal accounts WITH A GUARANTEE!\n"
                   "4. @SMALL_ACCOUNTS – sale of personal accounts WITH A GUARANTEE, but price category up to $300.\n"
                   "5. @VERTUU_RENT – rental of premium and rare accounts.\n"
                   "6. @VERTUUHACKS – cheat store.\n"
                   "7. @SCAMMERS_SPAWN – scam database, where we post IDs of res-accounts, as well as contacts of scammers.\n"
                   "8. @VERTUU_ACCOUNT_HELP – account maintenance (res/anti-res, ban/unban, etc.) + OSINT services like doxing, protection against doxing, etc.\n"
                   "9. @VERTUU_PREMIUM – store for cheap Telegram Premium subscriptions.\n"
                   "10. @EXCHANGERIN – currency exchanger, will help buy/sell crypto, sell a virtual number or place a bet for you.\n"
                   "11. @VERTUU_CRYPTO – personal channel about crypto, interesting tips, projects, etc.\n"
                   "12. @UA_PUBGM_STORE – account store (public), you can list any digital product for sale.\n"
                   "13. @UA_STORE_CHAT – chat for the public account store.\n"
                   "14. @TOURNAMENTS_PM – Pubg Mobile tournaments (currently afk).\n"
                   "15. @UA_TDM_PLATFORM – TDM tournaments, news from the TDM world, etc. (afk).")
        },
        'ekosistema': {
            'ru': ("Экосистема «Мир»:\n\n"
                   "1. @pubgmMIR_UC – магазин UC, нацеленный на снг аудиторию.\n"
                   "2. @pubgmMIR – самый большой развлекательный канал тематики Pubg Mobile в СНГ.\n"
                   "3. @pubgmMIR_news – новостной канал тематики Pubg Mobile.\n"
                   "4. @pubgmMIR_ads – канал тематики объявлений Pubg Mobile.\n"
                   "5. @mirPUBGM_CHAT – чат канала «Мир Pubg Mobile»."),
            'ua': ("Екосистема «Мир»:\n\n"
                   "1. @pubgmMIR_UC – магазин UC, націлений на снд аудиторію.\n"
                   "2. @pubgmMIR – найбільший розважальний канал тематики Pubg Mobile в СНД.\n"
                   "3. @pubgmMIR_news – новинний канал тематики Pubg Mobile.\n"
                   "4. @pubgmMIR_ads – канал тематики оголошень Pubg Mobile.\n"
                   "5. @mirPUBGM_CHAT – чат каналу «Мир Pubg Mobile»."),
            'en': ("The 'Mir' Ecosystem:\n\n"
                   "1. @pubgmMIR_UC – UC store aimed at the CIS audience.\n"
                   "2. @pubgmMIR – the largest entertainment channel on the Pubg Mobile theme in the CIS.\n"
                   "3. @pubgmMIR_news – news channel on the Pubg Mobile theme.\n"
                   "4. @pubgmMIR_ads – channel for Pubg Mobile announcements.\n"
                   "5. @mirPUBGM_CHAT – chat for the 'Mir Pubg Mobile' channel.")
        }
    }
}

# --- ФУНКЦИИ БОТА ---

def get_text(key, lang='ru'):
    """Получает ПРОСТОЙ текст из словаря texts на нужном языке."""
    return texts.get(key, {}).get(lang, f"NO_TEXT_FOR_{key}")

def check_subscription(user_id):
    """Проверяет, подписан ли пользователь на канал."""
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False

@bot.message_handler(commands=['start'])
def start(message):
    """Обработчик команды /start."""
    user_id = message.from_user.id
    if check_subscription(user_id):
        send_language_selection(message.chat.id)
    else:
        lang = 'ru' # Язык по умолчанию для первого сообщения
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(get_text('subscribe_button', lang), url=f"http://t.me/{CHANNEL_ID.lstrip('@')}"))
        markup.add(types.InlineKeyboardButton(get_text('check_button', lang), callback_data='check_subscription'))
        bot.send_message(message.chat.id, get_text('start_prompt', lang), reply_markup=markup)

def send_language_selection(chat_id):
    """Отправляет кнопки выбора языка с флагами."""
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(
        types.InlineKeyboardButton("🇬🇧 English", callback_data='lang_en'),
        types.InlineKeyboardButton("🇺🇦 Українська", callback_data='lang_ua'),
        types.InlineKeyboardButton("🇷🇺 Русский", callback_data='lang_ru')
    )
    bot.send_message(chat_id, get_text('choose_language'), reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'check_subscription')
def handle_check_subscription(call):
    """Обрабатывает нажатие на кнопку 'Проверить подписку'."""
    user_id = call.from_user.id
    lang = user_language.get(call.message.chat.id, 'ru')
    
    if check_subscription(user_id):
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=get_text('subscribed_success', lang))
        send_language_selection(call.message.chat.id)
    else:
        bot.answer_callback_query(call.id, get_text('not_subscribed', lang), show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def handle_language_selection(call):
    """Обрабатывает выбор языка."""
    lang_code = call.data.split('_')[1]
    user_language[call.message.chat.id] = lang_code
    
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, get_text('language_selected', lang_code))
    send_main_menu(call.message.chat.id, lang_code)

def send_main_menu(chat_id, lang):
    """Отправляет главное меню с кнопками на выбранном языке."""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    menu_buttons_dict = texts['menu_buttons']
    
    buttons = [
        menu_buttons_dict['reklama'][lang],
        menu_buttons_dict['kontakty'][lang],
        menu_buttons_dict['otzivi'][lang],
        menu_buttons_dict['proekti'][lang],
        menu_buttons_dict['ekosistema'][lang]
    ]
    markup.add(*buttons)
    bot.send_message(chat_id, get_text('main_menu_prompt', lang), reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    """Обрабатывает нажатия на кнопки главного меню."""
    chat_id = message.chat.id
    lang = user_language.get(chat_id, 'ru')
    
    menu_buttons_lang = {key: value[lang] for key, value in texts['menu_buttons'].items()}
    
    if message.text == menu_buttons_lang['reklama']:
        bot.send_message(chat_id, texts['responses']['reklama'][lang])
    elif message.text == menu_buttons_lang['kontakty']:
        bot.send_message(chat_id, texts['responses']['kontakty'][lang])
    elif message.text == menu_buttons_lang['otzivi']:
        bot.send_message(chat_id, texts['responses']['otzivi'][lang], disable_web_page_preview=True)
    elif message.text == menu_buttons_lang['proekti']:
        bot.send_message(chat_id, texts['responses']['proekti'][lang])
    elif message.text == menu_buttons_lang['ekosistema']:
        bot.send_message(chat_id, texts['responses']['ekosistema'][lang])


if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)