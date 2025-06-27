# import telebot
# from telebot import types

# # --- НАСТРОЙКИ ---
# TOKEN = '7529240199:AAFu6u_9zXCynLb8g02FDsqQgLfMS3Zd3NM'
# CHANNEL_ID = '@vertuu_crypto'  # Укажите ID вашего канала, например, @mychannel
# # -----------------

# bot = telebot.TeleBot(TOKEN)
# user_language = {} # Словарь для хранения языка каждого пользователя

# # --- ВСЕ ТЕКСТЫ БОТА ---
# # Структура: 'ключ_сообщения': {'ru': 'Текст на русском', 'ua': 'Текст на українській', 'en': 'Text in English'}
# texts = {
#     'start_prompt': {
#         'ru': ("Для использования этого бота, сначала подпишись на @vertuu_crypto🤝\n"
#                "—————————————————————\n"
#                "To use this bot, first subscribe to @vertuu_crypto🤝\n"
#                "—————————————————————\n"
#                "Для користування цим ботом, спершу підпишись на @vertuu_crypto🤝"),
#         'ua': ("Для користування цим ботом, спершу підпишись на @vertuu_crypto🤝\n"
#                "—————————————————————\n"
#                "Для использования этого бота, сначала подпишись на @vertuu_crypto🤝\n"
#                "—————————————————————\n"
#                "To use this bot, first subscribe to @vertuu_crypto🤝"),
#         'en': ("To use this bot, first subscribe to @vertuu_crypto🤝\n"
#                "—————————————————————\n"
#                "Для использования этого бота, сначала подпишись на @vertuu_crypto🤝\n"
#                "—————————————————————\n"
#                "Для користування цим ботом, спершу підпишись на @vertuu_crypto🤝")
#     },
#     'subscribe_button': {'ru': "Перейти в канал", 'ua': "Перейти в канал", 'en': "Go to Channel"},
#     'check_button': {'ru': "Проверить ✅", 'ua': "Перевірити ✅", 'en': "Check ✅"},
#     'subscribed_success': {
#         'ru': "Вы успешно подписаны на канал! Давайте продолжим.",
#         'ua': "Ви успішно підписані на канал! Давайте продовжимо.",
#         'en': "You have successfully subscribed to the channel! Let's continue."
#     },
#     'not_subscribed': {'ru': "Вы не подписаны на канал.", 'ua': "Ви не підписані на канал.", 'en': "You are not subscribed to the channel."},
#     'choose_language': {'ru': "Привіт! Оберіть мову:", 'ua': "Привіт! Оберіть мову:", 'en': "Hello! Choose your language:"},
#     'language_selected': {
#         'ru': "Вы выбрали язык: Русский\n\nВыберите, что вас интересует:\n👇🏻",
#         'ua': "Ви обрали мову: Українська\n\nОберіть, що вас цікавить:\n👇🏻",
#         'en': "You have selected language: English\n\nSelect what you are interested in:\n👇🏻"
#     },
#     'main_menu_prompt': {'ru': "Главное меню", 'ua': "Головне меню", 'en': "Main menu"},
#     'menu_buttons': {
#         'reklama': {'ru': "📢 Реклама", 'ua': "📢 Реклама", 'en': "📢 Advertising"},
#         'kontakty': {'ru': "👤 Контакты", 'ua': "👤 Контакти", 'en': "👤 Contacts"},
#         'otzivi': {'ru': "✍️ Отзывы", 'ua': "✍️ Відгуки", 'en': "✍️ Reviews"},
#         'proekti': {'ru': "🚀 Проекты", 'ua': "🚀 Проекти", 'en': "🚀 Projects"},
#         'ekosistema': {'ru': '🌍 Экосистема "Мир"', 'ua': '🌍 Екосистема "Мир"', 'en': '🌍 "Mir" Ecosystem'}
#     },
#     'responses': {
#         'reklama': {
#             'ru': ("Цены на рекламу:\n"
#                    "@vertuu_accounts — пост от 30$.\n"
#                    "@small_accounts — пост от 25$.\n"
#                    "@ua_pubgm_store — пост от 30$.\n"
#                    "@vertuu_rent — пост от 10$.\n"
#                    "——————————————————\n"
#                    "@pubgmMIR — пост от 15$.\n"
#                    "@pubgmMIR_ads — пост от 1$.\n"
#                    "@pubgmMIR_news — пост от 7$."),
#             'ua': ("Ціни на рекламу:\n"
#                    "@vertuu_accounts — пост від 30$.\n"
#                    "@small_accounts — пост від 25$.\n"
#                    "@ua_pubgm_store — пост від 30$.\n"
#                    "@vertuu_rent — пост від 10$.\n"
#                    "——————————————————\n"
#                    "@pubgmMIR — пост від 15$.\n"
#                    "@pubgmMIR_ads — пост від 1$.\n"
#                    "@pubgmMIR_news — пост від 7$."),
#             'en': ("Advertising prices:\n"
#                    "@vertuu_accounts — post from $30.\n"
#                    "@small_accounts — post from $25.\n"
#                    "@ua_pubgm_store — post from $30.\n"
#                    "@vertuu_rent — post from $10.\n"
#                    "——————————————————\n"
#                    "@pubgmMIR — post from $15.\n"
#                    "@pubgmMIR_ads — post from $1.\n"
#                    "@pubgmMIR_news — post from $7.")
#         },
#         'kontakty': {
#             'ru': ("Официальные контакты:\n\n"
#                    "1. @vrt484 – Я, мой личный контакт. Единственный телеграмм, других нет. Провожу сделки по продаже чего угодно ценой выше 5000₴(120$/11к₽). Также обращайтесь за покупкой личного аккаунта с гарантией или дешевой подписки Telegram Premium.\n\n"
#                    "2. @vertuu_admin – мой помощник, гарант сделок до 5000₴(120$/11к₽) и обменов.\n\n"
#                    "3. @uc_mir_admin – обращайтесь по покупки UC в рублях.\n\n"
#                    "4. Магазин N1 UC SHOP:\n• @UC_SHOP_ADMIN – UC по ID, пп, жетоны спорткаров и т.д. (гривны).\n• @UC_LOGIN_ADMIN – донат по входу (гривны).\n\n"
#                    "5. Магазин UA PUBGM STORE:\n• @vertuu_admin – чтобы выложить аккаунт на продажу, для связи с продавцом товара, проведения сделки, а также поможет подобрать нужный аккаунт.\n• @clans_trade – покупка/продажа кланов.\n\n"
#                    "6. @SA_seller – для покупки личного аккаунта с гарантией, ценой до 300$.\n\n"
#                    "7. @orenda_admin – взять аккаунт в аренду.\n\n"
#                    "8. @cht_sup – главный по чату @UA_STORE_CHAT.\n\n"
#                    "9. @vertuu_hacks_admin – для покупки читов.\n\n"
#                    "10. @currency_exchanging – обменник валют, международные переводы, поможет вывести или купить крипту, продаст вирт номер, поставит за вас ставку.\n\n"
#                    "11. Канал VERTUU HELP:\n• @vertuu_help – помощь с аккаунтом (рес/антирес, отвязка привязок и т.п.).\n• @vertuu_osint – пробив личных данных скамера и подобные услуги.\n\n"
#                    "12. @cards_rent – ​​возьмет карту в аренду."),
#             'ua': ("Офіційні контакти:\n\n"
#                    "1. @vrt484 – Я, мій особистий контакт. Єдиний телеграм, інших немає. Проводжу угоди з продажу будь-чого ціною вище 5000₴(120$/11к₽). Також звертайтесь за покупкою особистого облікового запису з гарантією або дешевої підписки Telegram Premium.\n\n"
#                    "2. @vertuu_admin – мій помічник, гарант угод до 5000₴(120$/11к₽) та обмінів.\n\n"
#                    "3. @uc_mir_admin – звертайтесь щодо покупки UC в рублях.\n\n"
#                    "4. Магазин N1 UC SHOP:\n• @UC_SHOP_ADMIN – UC за ID, пп, жетони спорткарів тощо (гривні).\n• @UC_LOGIN_ADMIN – донат за входом (гривні).\n\n"
#                    "5. Магазин UA PUBGM STORE:\n• @vertuu_admin – щоб викласти обліковий запис на продаж, для зв'язку з продавцем товару, проведення угоди, а також допоможе підібрати потрібний обліковий запис.\n• @clans_trade – купівля/продаж кланів.\n\n"
#                    "6. @SA_seller – для покупки особистого облікового запису з гарантією, ціною до 300$.\n\n"
#                    "7. @orenda_admin – взяти обліковий запис в оренду.\n\n"
#                    "8. @cht_sup – головний у чаті @UA_STORE_CHAT.\n\n"
#                    "9. @vertuu_hacks_admin – для покупки читів.\n\n"
#                    "10. @currency_exchanging – обмінник валют, міжнародні перекази, допоможе вивести чи купити крипту, продасть вірт номер, поставить за вас ставку.\n\n"
#                    "11. Канал VERTUU HELP:\n• @vertuu_help – допомога з обліковим записом (рес/антирес, відв'язування прив'язок тощо).\n• @vertuu_osint – пробив особистих даних скамера та подібні послуги.\n\n"
#                    "12. @cards_rent – ​​візьме картку в оренду."),
#             'en': ("Official contacts:\n\n"
#                    "1. @vrt484 – Me, my personal contact. The only Telegram account, no others. I conduct deals for selling anything priced above 5000 UAH ($120/11k RUB). Also, contact me for purchasing a personal account with a guarantee or a cheap Telegram Premium subscription.\n\n"
#                    "2. @vertuu_admin – my assistant, guarantor for deals up to 5000 UAH ($120/11k RUB) and exchanges.\n\n"
#                    "3. @uc_mir_admin – contact for purchasing UC in rubles.\n\n"
#                    "4. N1 UC SHOP Store:\n• @UC_SHOP_ADMIN – UC by ID, pps, sports car tokens, etc. (hryvnia).\n• @UC_LOGIN_ADMIN – donation by login (hryvnia).\n\n"
#                    "5. UA PUBGM STORE Store:\n• @vertuu_admin – to list an account for sale, to contact the seller, conduct a deal, and help select the right account.\n• @clans_trade – buying/selling clans.\n\n"
#                    "6. @SA_seller – for purchasing a personal account with a guarantee, priced up to $300.\n\n"
#                    "7. @orenda_admin – to rent an account.\n\n"
#                    "8. @cht_sup – head of the @UA_STORE_CHAT.\n\n"
#                    "9. @vertuu_hacks_admin – for purchasing cheats.\n\n"
#                    "10. @currency_exchanging – currency exchanger, international transfers, helps to withdraw or buy crypto, sells virtual numbers, places bets for you.\n\n"
#                    "11. VERTUU HELP Channel:\n• @vertuu_help – assistance with accounts (res/anti-res, unlinking, etc.).\n• @vertuu_osint – doxing of scammers and similar services.\n\n"
#                    "12. @cards_rent – will rent a card.")
#         },
#         'otzivi': {
#             'ru': ("Отдельные топ-кейсы:\n\n"
#                    "• Самая большая сделка во всем СНГ:\nhttps://t.me/vertuu_accounts/3005\n\n"
#                    "• Самая большая сделка в Украине:\nhttps://t.me/vertuu_accounts/2888\n\n"
#                    "• Покупка аккаунта за 5000$:\nhttps://t.me/vidguky_ua/11343\n\n"
#                    "• Единоразовая покупка 165000 UC по входу:\nhttps://t.me/vidguky_ua/11379\n"
#                    "——————————————————\n"
#                    "Всего свыше 35k отзывов, почитать их можно здесь:\nt.me/addlist/_w9B7KIq36c4NWUy"),
#             'ua': ("Окремі топ-кейси:\n\n"
#                    "• Найбільша угода у всьому СНД:\nhttps://t.me/vertuu_accounts/3005\n\n"
#                    "• Найбільша угода в Україні:\nhttps://t.me/vertuu_accounts/2888\n\n"
#                    "• Купівля акаунта за 5000$:\nhttps://t.me/vidguky_ua/11343\n\n"
#                    "• Одноразова покупка 165000 UC за входом:\nhttps://t.me/vidguky_ua/11379\n"
#                    "——————————————————\n"
#                    "Всього понад 35k відгуків, почитати їх можна тут:\nt.me/addlist/_w9B7KIq36c4NWUy"),
#             'en': ("Separate top cases:\n\n"
#                    "• The largest deal in the entire CIS:\nhttps://t.me/vertuu_accounts/3005\n\n"
#                    "• The largest deal in Ukraine:\nhttps://t.me/vertuu_accounts/2888\n\n"
#                    "• Account purchase for $5000:\nhttps://t.me/vidguky_ua/11343\n\n"
#                    "• One-time purchase of 165,000 UC via login:\nhttps://t.me/vidguky_ua/11379\n"
#                    "——————————————————\n"
#                    "Over 35k reviews in total, you can read them here:\nt.me/addlist/_w9B7KIq36c4NWUy")
#         },
#         'proekti': {
#             'ru': ("Основные проекты:\n\n"
#                    "1. @pubgmMIR_UC – магазин UC для снг пользователей.\n"
#                    "2. @N1_UC_SHOP – магазин UC для пользователей с Украины.\n"
#                    "3. @VERTUU_ACCOUNTS – продажа личных аккаунтов С ГАРАНТИЕЙ!\n"
#                    "4. @SMALL_ACCOUNTS – продажа личных аккаунтов С ГАРАНТИЕЙ, но ценовая категория до 300$.\n"
#                    "5. @VERTUU_RENT – аренда жирных и редких аккаунтов.\n"
#                    "6. @VERTUUHACKS – магазин читов.\n"
#                    "7. @SCAMMERS_SPAWN – скам-база, где постим айди рес-аккаунтом, а так же контакты мошенников.\n"
#                    "8. @VERTUU_ACCOUNT_HELP – обслуживание аккаунта (рес/антирес, бан/разбан и тд. тп.) + OSINT-услуги по типу пробива данных, защиты от пробива и т.д.\n"
#                    "9. @VERTUU_PREMIUM – магазин дешевых подписок Telegram Premium.\n"
#                    "10. @EXCHANGERIN – обменник валют, поможет купить/продать крипту, продаст вирт номер или же поставит на вас ставку.\n"
#                    "11. @VERTUU_CRYPTO – личный канал о крипте, интересные советы, проекты и тд.\n"
#                    "12. @UA_PUBGM_STORE – магазин аккаунтов (публичных), можно выложить на продажу любой цифровой товар.\n"
#                    "13. @UA_STORE_CHAT – чат магазина аккаунтов (публичных).\n"
#                    "14. @TOURNAMENTS_PM – турниры Pubg Mobile (пока афк).\n"
#                    "15. @UA_TDM_PLATFORM – тдм-турниры, новости из мира TDM и т.д (афк)."),
#             'ua': ("Основні проекти:\n\n"
#                    "1. @pubgmMIR_UC – магазин UC для користувачів СНД.\n"
#                    "2. @N1_UC_SHOP – магазин UC для користувачів з України.\n"
#                    "3. @VERTUU_ACCOUNTS – продаж особистих акаунтів З ГАРАНТІЄЮ!\n"
#                    "4. @SMALL_ACCOUNTS – продаж особистих акаунтів З ГАРАНТІЄЮ, але цінова категорія до 300$.\n"
#                    "5. @VERTUU_RENT – оренда жирних та рідкісних акаунтів.\n"
#                    "6. @VERTUUHACKS – магазин читів.\n"
#                    "7. @SCAMMERS_SPAWN – скам-база, де постимо айді рес-акаунтів, а також контакти шахраїв.\n"
#                    "8. @VERTUU_ACCOUNT_HELP – обслуговування акаунта (рес/антирес, бан/розбан і т.д.) + OSINT-послуги типу пробиву даних, захисту від пробиву і т.д.\n"
#                    "9. @VERTUU_PREMIUM – магазин дешевих підписок Telegram Premium.\n"
#                    "10. @EXCHANGERIN – обмінник валют, допоможе купити/продати крипту, продасть вірт номер або ж поставить за вас ставку.\n"
#                    "11. @VERTUU_CRYPTO – особистий канал про крипту, цікаві поради, проекти і т.д.\n"
#                    "12. @UA_PUBGM_STORE – магазин акаунтів (публічних), можна виставити на продаж будь-який цифровой товар.\n"
#                    "13. @UA_STORE_CHAT – чат магазину акаунтів (публічних).\n"
#                    "14. @TOURNAMENTS_PM – турніри Pubg Mobile (поки афк).\n"
#                    "15. @UA_TDM_PLATFORM – тдм-турніри, новини зі світу TDM і т.д (афк)."),
#             'en': ("Main projects:\n\n"
#                    "1. @pubgmMIR_UC – UC store for CIS users.\n"
#                    "2. @N1_UC_SHOP – UC store for users from Ukraine.\n"
#                    "3. @VERTUU_ACCOUNTS – sale of personal accounts WITH A GUARANTEE!\n"
#                    "4. @SMALL_ACCOUNTS – sale of personal accounts WITH A GUARANTEE, but price category up to $300.\n"
#                    "5. @VERTUU_RENT – rental of premium and rare accounts.\n"
#                    "6. @VERTUUHACKS – cheat store.\n"
#                    "7. @SCAMMERS_SPAWN – scam database, where we post IDs of res-accounts, as well as contacts of scammers.\n"
#                    "8. @VERTUU_ACCOUNT_HELP – account maintenance (res/anti-res, ban/unban, etc.) + OSINT services like doxing, protection against doxing, etc.\n"
#                    "9. @VERTUU_PREMIUM – store for cheap Telegram Premium subscriptions.\n"
#                    "10. @EXCHANGERIN – currency exchanger, will help buy/sell crypto, sell a virtual number or place a bet for you.\n"
#                    "11. @VERTUU_CRYPTO – personal channel about crypto, interesting tips, projects, etc.\n"
#                    "12. @UA_PUBGM_STORE – account store (public), you can list any digital product for sale.\n"
#                    "13. @UA_STORE_CHAT – chat for the public account store.\n"
#                    "14. @TOURNAMENTS_PM – Pubg Mobile tournaments (currently afk).\n"
#                    "15. @UA_TDM_PLATFORM – TDM tournaments, news from the TDM world, etc. (afk).")
#         },
#         'ekosistema': {
#             'ru': ("Экосистема «Мир»:\n\n"
#                    "1. @pubgmMIR_UC – магазин UC, нацеленный на снг аудиторию.\n"
#                    "2. @pubgmMIR – самый большой развлекательный канал тематики Pubg Mobile в СНГ.\n"
#                    "3. @pubgmMIR_news – новостной канал тематики Pubg Mobile.\n"
#                    "4. @pubgmMIR_ads – канал тематики объявлений Pubg Mobile.\n"
#                    "5. @mirPUBGM_CHAT – чат канала «Мир Pubg Mobile»."),
#             'ua': ("Екосистема «Мир»:\n\n"
#                    "1. @pubgmMIR_UC – магазин UC, націлений на снд аудиторію.\n"
#                    "2. @pubgmMIR – найбільший розважальний канал тематики Pubg Mobile в СНД.\n"
#                    "3. @pubgmMIR_news – новинний канал тематики Pubg Mobile.\n"
#                    "4. @pubgmMIR_ads – канал тематики оголошень Pubg Mobile.\n"
#                    "5. @mirPUBGM_CHAT – чат каналу «Мир Pubg Mobile»."),
#             'en': ("The 'Mir' Ecosystem:\n\n"
#                    "1. @pubgmMIR_UC – UC store aimed at the CIS audience.\n"
#                    "2. @pubgmMIR – the largest entertainment channel on the Pubg Mobile theme in the CIS.\n"
#                    "3. @pubgmMIR_news – news channel on the Pubg Mobile theme.\n"
#                    "4. @pubgmMIR_ads – channel for Pubg Mobile announcements.\n"
#                    "5. @mirPUBGM_CHAT – chat for the 'Mir Pubg Mobile' channel.")
#         }
#     }
# }

# # --- ФУНКЦИИ БОТА ---

# def get_text(key, lang='ru'):
#     """Получает ПРОСТОЙ текст из словаря texts на нужном языке."""
#     return texts.get(key, {}).get(lang, f"NO_TEXT_FOR_{key}")

# def check_subscription(user_id):
#     """Проверяет, подписан ли пользователь на канал."""
#     try:
#         member = bot.get_chat_member(CHANNEL_ID, user_id)
#         return member.status in ['member', 'administrator', 'creator']
#     except Exception as e:
#         print(f"Error checking subscription: {e}")
#         return False

# @bot.message_handler(commands=['start'])
# def start(message):
#     """Обработчик команды /start."""
#     user_id = message.from_user.id
#     if check_subscription(user_id):
#         send_language_selection(message.chat.id)
#     else:
#         lang = 'ru' # Язык по умолчанию для первого сообщения
#         markup = types.InlineKeyboardMarkup()
#         markup.add(types.InlineKeyboardButton(get_text('subscribe_button', lang), url=f"http://t.me/{CHANNEL_ID.lstrip('@')}"))
#         markup.add(types.InlineKeyboardButton(get_text('check_button', lang), callback_data='check_subscription'))
#         bot.send_message(message.chat.id, get_text('start_prompt', lang), reply_markup=markup)

# def send_language_selection(chat_id):
#     """Отправляет кнопки выбора языка с флагами."""
#     markup = types.InlineKeyboardMarkup(row_width=3)
#     markup.add(
#         types.InlineKeyboardButton("🇬🇧 English", callback_data='lang_en'),
#         types.InlineKeyboardButton("🇺🇦 Українська", callback_data='lang_ua'),
#         types.InlineKeyboardButton("🇷🇺 Русский", callback_data='lang_ru')
#     )
#     bot.send_message(chat_id, get_text('choose_language'), reply_markup=markup)

# @bot.callback_query_handler(func=lambda call: call.data == 'check_subscription')
# def handle_check_subscription(call):
#     """Обрабатывает нажатие на кнопку 'Проверить подписку'."""
#     user_id = call.from_user.id
#     lang = user_language.get(call.message.chat.id, 'ru')
    
#     if check_subscription(user_id):
#         bot.answer_callback_query(call.id)
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=get_text('subscribed_success', lang))
#         send_language_selection(call.message.chat.id)
#     else:
#         bot.answer_callback_query(call.id, get_text('not_subscribed', lang), show_alert=True)

# @bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
# def handle_language_selection(call):
#     """Обрабатывает выбор языка."""
#     lang_code = call.data.split('_')[1]
#     user_language[call.message.chat.id] = lang_code
    
#     bot.answer_callback_query(call.id)
#     bot.delete_message(call.message.chat.id, call.message.message_id)
#     bot.send_message(call.message.chat.id, get_text('language_selected', lang_code))
#     send_main_menu(call.message.chat.id, lang_code)

# def send_main_menu(chat_id, lang):
#     """Отправляет главное меню с кнопками на выбранном языке."""
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
#     menu_buttons_dict = texts['menu_buttons']
    
#     buttons = [
#         menu_buttons_dict['reklama'][lang],
#         menu_buttons_dict['kontakty'][lang],
#         menu_buttons_dict['otzivi'][lang],
#         menu_buttons_dict['proekti'][lang],
#         menu_buttons_dict['ekosistema'][lang]
#     ]
#     markup.add(*buttons)
#     bot.send_message(chat_id, get_text('main_menu_prompt', lang), reply_markup=markup)

# @bot.message_handler(func=lambda message: True)
# def handle_text(message):
#     """Обрабатывает нажатия на кнопки главного меню."""
#     chat_id = message.chat.id
#     lang = user_language.get(chat_id, 'ru')
    
#     menu_buttons_lang = {key: value[lang] for key, value in texts['menu_buttons'].items()}
    
#     if message.text == menu_buttons_lang['reklama']:
#         bot.send_message(chat_id, texts['responses']['reklama'][lang])
#     elif message.text == menu_buttons_lang['kontakty']:
#         bot.send_message(chat_id, texts['responses']['kontakty'][lang])
#     elif message.text == menu_buttons_lang['otzivi']:
#         bot.send_message(chat_id, texts['responses']['otzivi'][lang], disable_web_page_preview=True)
#     elif message.text == menu_buttons_lang['proekti']:
#         bot.send_message(chat_id, texts['responses']['proekti'][lang])
#     elif message.text == menu_buttons_lang['ekosistema']:
#         bot.send_message(chat_id, texts['responses']['ekosistema'][lang])


# if __name__ == '__main__':
#     print("Бот запущен...")
#     bot.polling(none_stop=True)




import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.constants import ParseMode
import sqlite3

TOKEN = '7529240199:AAFu6u_9zXCynLb8g02FDsqQgLfMS3Zd3NM'  # <-- твій токен

# Логування
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Список адмінів (встав свій Telegram ID сюди)
ADMIN_IDS = [747846636, 585870031]  # Заміни 123456789 на свій ID

# Підключаємо базу та створюємо таблицю, якщо нема
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY
    )
''')
conn.commit()

TEXTS = {
    'ua': {
        'start': (
            "Вітаю вас у цьому боті, у ньому можна детальніше дізнатись про мене та мої проекти. "
            "Також, що важливо, звірити чи є та чи інша людина учасником моєї команди, чи лише прикидається аби витягти з вас кошти.\n\n"
            "Тут ви знайдете усі необхідні посилання та інформацію, сміливо переходьте по кнопкам нижче😁"
        ),
        'about': (
            "<b>Про мене</b>\n\n"
            "Мій телеграм: @vrt484 / @vertuu. <b>ЖОДНИХ ІНШИХ.</b> Так, є ще адміни, але у них інші нікнейми, аватарки та й знайти їх можна в розділі «Контакти співробітників».\n"
            "Все інше – фейки, які роблять схожі юзери, де відмінна одна лиш цифра чи буква, які роблять фейкові канали та ботів, аби бути максимально схожими, видають себе за мене та найобують людей. Обережно!\n\n"
            "Я біля 4 років в медійному полі, починав з нуля нулем, першими проектами були @ua_pubgm_store та @ua_store_chat, які і досі актуальні але сильно менше. За ці роки став з рівня нн-гаранта одним з найкращих як в Україні, так і по снд. Один з перших в країні, і вважаю себе одним із ключових людей, що створили український пабг-ринок в цілому, до мене тут було 1-2 персонажі, і то продавали в рублях і російською, на російську аудиторію, один з них і досі продовжує. Наразі трішки відійшов від \"гаранства\", і займаюсь тим, що приносить більше грошей. Ще досі проводжу угоди, але рідше, лише більші. До 5000₴ поставив адміна вже як 2 роки, @vertuu_admin.\n\n"
            "Я цікава особистість, підприємець по пабгу, крипто-ентузіаст, просто чувак за яким прикольно слідкувати.\n\n"
            "Переважно веду свої проекти українською і для українців, на відміну від 95% усіх опонентів, цим втрачаю великий шмат аудиторії, звісно ж, але це принципово. Популяризую українську та про-українську позицію. Молодь має розуміти, що в ігровій сфері можна вести канал рідною мовою, і при цьому бути успішним. Так, трохи важче, але можна:) І це насправді працює, я надав приклад десяткам, а може й сотням людей, що розпочали своє діло українською в телеграмі, ну або як мінімум розпочали, що теж непогано)"
        ),
        'projects': (
            "<b>Мої канали-проекти</b>\n\n"
            "1. Зараз мене найлегше знайти в каналі @vertuu_crypto, найбільш актуально через телеграм-подарунки та тему заробітку в цілому. Строчу туди по 20 постів на день.\n\n"
            "2. @vertuu_accounts – також основний канал, в якому часто пишу свої думки, але головна його мета – продаж моїх особистих pubgm-акаунтів з гарантією від відновлення, зазвичай пожиттєвою, що робить мене тут унікальним.\n\n"
            "3. @n1_uc_shop – для усіх, хто хоче вигідно і безпечно купити UC / популярність / суперкар / Х-костюм / голоси для будинку тощо. Реально дешево. Швидко та якісно. Ну а головне безпечно + таким чином підтримуєте мене монетою, самі ж економлячи.\n\n"
            "4. @vertuu_rent – НАЙДЕШЕВША, реально найдешевша оренда люксових, рідкісних, жирних пабг-акаунтів. Здаю лише свої, відповідно і ціни тримаємо вигідні, адже не треба додатково платити власникам акаунтів. За смішні 100 гривень можете зняти на день акаунт ціною в 100 тисяч🙂\n\n"
            "5. Не так давно створив новий, але дуже функціональний магазин – @n1_tele_shop. Там можна дешево за гривні купити: телеграм-зірки, телеграм-преміум, криптовалюту TON(зараз дуже актуально). Також можна замовити пошук NFT під замовлення, продати свої подарунки тощо. Коротше дуже круто все.\n\n"
            "6. @small_accounts – продаж акаунтів до 400$ ціною від моїх адмінів. Всі вони безпечні та з гарантією від відновлення. Також адмінам можна продати свій акаунт в тій ціновій категорії, звісно якщо він безпечний та вигідний для перепродажу.\n\n"
            "7. @vertuu_tiktok – покупка/продаж TikTok-акаунтів. Можете виставити свій на продаж / продати адміну чи наприклад придбати якийсь ак вигідно. Реально вигідно!\n\n"
            "8. @ua_pubgm_store – мій перший канал, в ньому можете викласти свій пабг-акаунт на продаж / придбати. Але всі аки публічні, гарантій від відновлення нема. Є гарантія, що покупка пройде точно безпечно.\n\n"
            "9. @ua_store_chat – та ж сама функціональність, але це чат. Ну і в ньому не тільки пабг наразі, там різні люди продають своїм товари чи послуги, гаранти я або @vertuu_admin.\n\n"
            "10. @vertuu_boost – якщо чесно не сильно актуально, замволень багато не маємо. Але людина є, працює добре, бустить швидко, якісно, без чітів, і дешево. В рази дешевше ніж якісь стрімери наприклад. А гарантія від мене надійна.\n\n"
            "11. @vertuuhacks – проект продається😁 Хто зацікавлений – пишіть, ціна не висока.\n\n"
            "12. @tournaments_pm – праки, кастомки, турніри. Поки на паузі, але час від часу запускаєм заново, іноді нові формати, зі стрімами наприклад, з хорошими призами. Крч варто уваги, проведення робиться на рівні.\n\n"
            "13. @scammers_spawn – скам-база, в якій постимо айді рес-акаунтів, юзери скамерів тощо. Була попередня, в 10 разів більша, тг її зніс за те, що розповсюджувались паспорти, номери телефонів скамерів. Хоч вони скамери, але таке розповсюджувати в телаграмі заборонено. Наразі не сильно активна база, але думаю поновим.\n\n"
            "14. @exchangerin – чисто канал собі існує, трафік туди не жену. Канал обмінника валют, за цією послугою пишіть @currency_exchanging, безпечний і вигідний, правда іноді не дуже швидкий. Суми в тисячі доларів міняти можна без страху зате.\n\n"
            "15. @vertuu_account_help – теж пережиток минулого, там адміна більше нема, за всім послугами пишіть до мене, точніше актуальна там наразі послуга лише знос 3-6 + допомогти з ресом я вам також можу."
        ),
        'contacts': (
            "<b>Контакти співробітників</b>\n\n"
            "1. Передусім я, мій єдиний контакт – @vrt484(@vertuu) – гарант угод від 5000₴😁 Всі інші, хто роблять схожу сторінку – фейки.\n\n"
            "2. @vertuu_admin – гарант угод до 5000₴ та обмінів. +до нього звертайтесь за викладенням акаунта на продаж чи купівлею з каналу @ua_pubgm_store.\n\n"
            "3. @currency_exchanging – мій обмінник валют. Допоможе з переказом / виводом тощо.\n\n"
            "4. @uc_shop_admin – купівля UC по айді / популярності / жетонів на авто чи костюм-Х, голосів для будинку тощо.\n\n"
            "5. @uc_login_admin – купівля UC по QR(по входу). Це значно дешевше за донат по айді і так само швидко та безпечно.\n\n"
            "6. @tele_shop_admin – контакт для купівлі зірок, Telegram Premium, TON, нфт-подарунків, накруту тощо.\n\n"
            "7. @sa_seller – для купівлі акаунтів з гарантією, ціною до 400$. Також можете продати йому свій по терміновій ціні, але лише безпечний, особистий.\n\n"
            "8. @smaller_sa – для купівлі акаунтів з гарантією, ціною до 100$. Також можете продати йому свій, в цьому ж ціновому діапазоні, безпечний, за який можете ручатися.\n\n"
            "9. @clans_trade – купівля/продаж кланів.\n\n"
            "10. @vertuu_tt_admin – контакт для купівлі/продажу TikTok-акаунтів.\n\n"
            "11. @vertuu_boost_admin – адмін, що бустить ранги/досягнення.\n\n"
            "12. @cards_rent – для здачі вашої картки в оренду. Це вигідно та безпечно. Ризик є. Іноді картка може заблокуватись.\n\n"
            "13. @vertuu_hacks_admin – контакт для купівлі стороннього пз, відповідає часто дуже довго, обслуговування з усіх адмінів напевне найгірше."
        ),
        'reviews': (
            "<b>Відгуки</b>\n\n"
            "Усього понад 40k відгуків, почитати їх можна тут:\n"
            "<a href='https://t.me/addlist/EnRkVgV2VHg2OTky'>➡️ Папка з відгуками</a>\n\n"
            "Окремі великі кейси:\n"
            "(Продажі акаунтів за пару тисяч баксів не додаю, бо то вже майже щоденна подія)\n\n"
            "• Найбільша угода у всьому снд-просторі:\n<a href='https://t.me/vertuu_accounts/3005'>🔗 Подивитись</a>\n\n"
            "• Найбільша угода в Україні(до того):\n<a href='https://t.me/vertuu_accounts/2888'>🔗 Подивитись</a>\n\n"
            "• Покупка акаунта за 5000$:\n<a href='https://t.me/vidguky_ua/11343'>🔗 Подивитись</a>\n\n"
            "• Єдиноразова покупка 500000UC (5000$) по входу:\n<a href='https://t.me/n1_uc_shop/4084'>🔗 Подивитись</a>\n\n"
            "• Єдиноразова покупка 165000UC (1700$) по входу:\n<a href='https://t.me/vidguky_ua/11379'>🔗 Подивитись</a>\n\n"
            "• Людина продала мені Plush Pepe за 4500$ на довірі:\n<a href='https://t.me/vertuu_crypto/5718'>🔗 Подивитись</a>\n\n"
            "• Людина купила у мене Durov’s Cap за 2000$ на довірі:\n<a href='https://t.me/vertuu_crypto/5036'>🔗 Подивитись</a>"
        ),
        "ad": (
        "Реклама продається майже усюди, ціни варіюються відносно предмету реклами та способу рекламування.\n\n"
        "За рекламою у @vertuu_accounts та @vertuu_crypto – пишіть особисто мені, @vrt484\n\n"
        "За рекламою у @small_accounts пишіть @sa_seller або @smaller_sa\n\n"
        "За рекламою у @vertuu_rent пишіть @orenda_admin\n\n"
        "В принципі усе логічно — за рекламою у певному каналі просто пишете адміну того ж каналу, "
        "уточнюйте ціну та домовляєтесь."
    ),
        'buttons': {
            'about': "Про мене",
            'projects': "Мої канали-проекти",
            'contacts': "Контакти співробітників",
            'reviews': "Відгуки",
            'ad': "Реклама",
            'back': "⬅️ Назад в меню"
        }
    },
    'ru': {
        'start': (
            "Приветствую вас в этом боте, в нем можно подробнее узнать обо мне и моих проектах. "
            "Также, что важно, сверить, является ли тот или иной человек участником моей команды, или только притворяется, чтобы вытянуть из вас средства.\n\n"
            "Здесь вы найдете все необходимые ссылки и информацию, смело переходите по кнопкам ниже😁"
        ),
        'about': (
            "<b>Обо мне</b>\n\n"
            "Мой телеграм: @vrt484 / @vertuu. <b>НИКАКИХ ДРУГИХ.</b> Да, есть еще админы, но у них другие никнеймы, аватарки и найти их можно в разделе «Контакты сотрудников».\n"
            "Все остальное – фейки, которые делают похожие юзеры, где отличается одна лишь цифра или буква, которые делают фейковые каналы и ботов, чтобы быть максимально похожими, выдают себя за меня и обманывают людей. Осторожно!\n\n"
            "Я около 4 лет в медийном поле, начинал с нуля, первыми проектами были @ua_pubgm_store и @ua_store_chat, которые до сих пор актуальны, но значительно меньше. За эти годы стал с уровня нн-гаранта одним из лучших как в Украине, так и в СНГ. Один из первых в стране, и считаю себя одним из ключевых людей, создавших украинский пабг-рынок в целом, до меня здесь было 1-2 персонажа, и то продавали в рублях и на русском, на российскую аудиторию, один из них до сих пор продолжает. Сейчас немного отошел от \"гарантства\", и занимаюсь тем, что приносит больше денег. Все еще провожу сделки, но реже, только более крупные. До 5000₴ поставил админа уже как 2 года, @vertuu_admin.\n\n"
            "Я интересная личность, предприниматель по пабгу, крипто-энтузиаст, просто чувак за которым прикольно следить.\n\n"
            "Преимущественно веду свои проекты на украинском и для украинцев, в отличие от 95% всех оппонентов, этим теряю большой кусок аудитории, конечно, но это принципиально. Популяризирую украинский и про-украинскую позицию. Молодежь должна понимать, что в игровой сфере можно вести канал на родном языке, и при этом быть успешным. Да, немного сложнее, но можно:) И это на самом деле работает, я подал пример десяткам, а может и сотням людей, которые начали свое дело на украинском в телеграме, ну или как минимум начали, что тоже неплохо)"
        ),
        'projects': (
            "<b>Мои каналы-проекты</b>\n\n"
            "1. Сейчас меня легче всего найти в канале @vertuu_crypto, наиболее актуально из-за телеграм-подарков и темы заработка в целом. Строчу туда по 20 постов в день.\n\n"
            "2. @vertuu_accounts – также основной канал, в котором часто пишу свои мысли, но главная его цель – продажа моих личных pubgm-аккаунтов с гарантией от восстановления, обычно пожизненной, что делает меня здесь уникальным.\n\n"
            "3. @n1_uc_shop – для всех, кто хочет выгодно и безопасно купить UC / популярность / суперкар / Х-костюм / голоса для дома и т.д. Реально дешево. Быстро и качественно. Ну а главное безопасно + таким образом поддерживаете меня монетой, сами же экономя.\n\n"
            "4. @vertuu_rent – САМАЯ ДЕШЕВАЯ, реально самая дешевая аренда люксовых, редких, жирных пабг-аккаунтов. Сдаю только свои, соответственно и цены держим выгодные, ведь не надо дополнительно платить владельцам аккаунтов. За смешные 100 гривен можете снять на день аккаунт ценой в 100 тысяч🙂\n\n"
            "5. Не так давно создал новый, но очень функциональный магазин – @n1_tele_shop. Там можно дешево за гривны купить: телеграм-звезды, телеграм-премиум, криптовалюту TON(сейчас очень актуально). Также можно заказать поиск NFT под заказ, продать свои подарки и т.д. Короче очень круто все.\n\n"
            "6. @small_accounts – продажа аккаунтов до 400$ ценой от моих админов. Все они безопасны и с гарантией от восстановления. Также админам можно продать свой аккаунт в той ценовой категории, конечно если он безопасен и выгоден для перепродажи.\n\n"
            "7. @vertuu_tiktok – покупка/продажа TikTok-аккаунтов. Можете выставить свой на продажу / продать админу или например приобрести какой-то акк выгодно. Реально выгодно!\n\n"
            "8. @ua_pubgm_store – мой первый канал, в нем можете выложить свой пабг-аккаунт на продажу / приобрести. Но все акки публичные, гарантий от восстановления нет. Есть гарантия, что покупка пройдет точно безопасно.\n\n"
            "9. @ua_store_chat – та же функциональность, но это чат. Ну и в нем не только пабг сейчас, там разные люди продают свои товары или услуги, гаранты я или @vertuu_admin.\n\n"
            "10. @vertuu_boost – если честно не сильно актуально, заказов много не имеем. Но человек есть, работает хорошо, бустит быстро, качественно, без читов, и дешево. В разы дешевле чем какие-то стримеры например. А гарантия от меня надежная.\n\n"
            "11. @vertuuhacks – проект продается😁 Кто заинтересован – пишите, цена не высокая.\n\n"
            "12. @tournaments_pm – праки, кастомки, турниры. Пока на паузе, но время от времени запускаем заново, иногда новые форматы, со стримами например, с хорошими призами. Короче стоит внимания, проведение делается на уровне.\n\n"
            "13. @scammers_spawn – скам-база, в которой постим айди рес-аккаунтов, юзеры скамеров и т.д. Была предыдущая, в 10 раз больше, тг ее снес за то, что распространялись паспорта, номера телефонов скамеров. Хоть они скамеры, но такое распространять в телеграме запрещено. Сейчас не сильно активная база, но думаю возобновим.\n\n"
            "14. @exchangerin – чисто канал себе существует, трафик туда не гоню. Канал обменника валют, по этой услуге пишите @currency_exchanging, безопасный и выгодный, правда иногда не очень быстрый. Суммы в тысячи долларов менять можно без страха зато.\n\n"
            "15. @vertuu_account_help – тоже пережиток прошлого, там админа больше нет, по всем услугам пишите ко мне, точнее актуальна там сейчас услуга только снос 3-6 + помочь с ресом я вам также могу."
        ),
        'contacts': (
            "<b>Контакты сотрудников</b>\n\n"
            "1. Прежде всего я, мой единственный контакт – @vrt484(@vertuu) – гарант сделок от 5000₴😁 Все остальные, кто делают похожую страницу – фейки.\n\n"
            "2. @vertuu_admin – гарант сделок до 5000₴ и обменов. +к нему обращайтесь за выставлением аккаунта на продажу или покупкой с канала @ua_pubgm_store.\n\n"
            "3. @currency_exchanging – мой обменник валют. Поможет с переводом / выводом и т.д.\n\n"
            "4. @uc_shop_admin – покупка UC по айди / популярности / жетонов на авто или костюм-Х, голосов для дома и т.д.\n\n"
            "5. @uc_login_admin – покупка UC по QR(по входу). Это значительно дешевле доната по айди и так же быстро и безопасно.\n\n"
            "6. @tele_shop_admin – контакт для покупки звезд, Telegram Premium, TON, нфт-подарков, накрутки и т.д.\n\n"
            "7. @sa_seller – для покупки аккаунтов с гарантией, ценой до 400$. Также можете продать ему свой по срочной цене, но только безопасный, личный.\n\n"
            "8. @smaller_sa – для покупки аккаунтов с гарантией, ценой до 100$. Также можете продать ему свой, в этом же ценовом диапазоне, безопасный, за который можете ручаться.\n\n"
            "9. @clans_trade – покупка/продажа кланов.\n\n"
            "10. @vertuu_tt_admin – контакт для покупки/продажи TikTok-аккаунтов.\n\n"
            "11. @vertuu_boost_admin – админ, который бустит ранги/достижения.\n\n"
            "12. @cards_rent – для сдачи вашей карты в аренду. Это выгодно и безопасно. Риск есть. Иногда карта может заблокироваться.\n\n"
            "13. @vertuu_hacks_admin – контакт для покупки стороннего ПО, отвечает часто очень долго, обслуживание из всех админов наверное худшее."
        ),
        'reviews': (
            "<b>Отзывы</b>\n\n"
            "Всего более 40k отзывов, почитать их можно здесь:\n"
            "<a href='https://t.me/addlist/EnRkVgV2VHg2OTky'>➡️ Папка с отзывами</a>\n\n"
            "Отдельные крупные кейсы:\n"
            "(Продажи аккаунтов за пару тысяч баксов не добавляю, потому что это уже почти ежедневное событие)\n\n"
            "• Крупнейшая сделка во всем снг-пространстве:\n<a href='https://t.me/vertuu_accounts/3005'>🔗 Посмотреть</a>\n\n"
            "• Крупнейшая сделка в Украине(до этого):\n<a href='https://t.me/vertuu_accounts/2888'>🔗 Посмотреть</a>\n\n"
            "• Покупка аккаунта за 5000$:\n<a href='https://t.me/vidguky_ua/11343'>🔗 Посмотреть</a>\n\n"
            "• Единоразовая покупка 500000UC (5000$) по входу:\n<a href='https://t.me/n1_uc_shop/4084'>🔗 Посмотреть</a>\n\n"
            "• Единоразовая покупка 165000UC (1700$) по входу:\n<a href='https://t.me/vidguky_ua/11379'>🔗 Посмотреть</a>\n\n"
            "• Человек продал мне Plush Pepe за 4500$ на доверии:\n<a href='https://t.me/vertuu_crypto/5718'>🔗 Посмотреть</a>\n\n"
            "• Человек купил у меня Durov’s Cap за 2000$ на доверии:\n<a href='https://t.me/vertuu_crypto/5036'>🔗 Посмотреть</a>"
        ),
        "ad": (
        "Реклама размещается почти везде, цены варьируются в зависимости от предмета рекламы и способа продвижения.\n\n"
        "По поводу рекламы в @vertuu_accounts и @vertuu_crypto — пишите лично мне, @vrt484\n\n"
        "По поводу рекламы в @small_accounts — пишите @sa_seller или @smaller_san\n"
        "По поводу рекламы в @vertuu_rent — пишите @orenda_admin\n\n"
        "В целом всё логично — если хотите разместить рекламу в каком-то канале, просто напишите администратору этого  канала"
        "уточните цену и договоритесь."
    ),
        'buttons': {
            'about': "Обо мне",
            'projects': "Мои каналы-проекты",
            'contacts': "Контакты сотрудников",
            'reviews': "Отзывы",
            'ad': "Реклама",
            'back': "⬅️ Назад в меню"
        }
    },
    'en': {
        'start': (
            "Welcome to this bot. Here you can learn more about me and my projects. "
            "Also, importantly, you can verify if a person is a member of my team or just pretending to be, to get money from you.\n\n"
            "Here you will find all the necessary links and information. Feel free to navigate using the buttons below😁"
        ),
        'about': (
            "<b>About me</b>\n\n"
            "My Telegram: @vrt484 / @vertuu. <b>NO OTHERS.</b> Yes, there are admins, but they have different nicknames, avatars, and you can find them in the 'Staff Contacts' section.\n"
            "Everything else is a fake, created by users with similar usernames where only one digit or letter is different. They create fake channels and bots to look as similar as possible, impersonate me, and scam people. Be careful!\n\n"
            "I've been in the media space for about 4 years, starting from scratch. My first projects were @ua_pubgm_store and @ua_store_chat, which are still active but much less so. Over these years, I've grown from a no-name middleman to one of the best in both Ukraine and the CIS region. I was one of the first in the country, and I consider myself one of the key figures who created the Ukrainian PUBG market as a whole. Before me, there were only 1-2 people, and they sold in rubles and Russian, targeting a Russian audience; one of them still does. Currently, I've stepped back a bit from being a 'middleman' and am focusing on what brings in more money. I still conduct deals, but less frequently and only larger ones. For deals up to 5000 UAH, I've had an admin, @vertuu_admin, for 2 years now.\n\n"
            "I'm an interesting person, a PUBG entrepreneur, a crypto enthusiast, and just a cool guy to follow.\n\n"
            "I primarily run my projects in Ukrainian and for Ukrainians, unlike 95% of my opponents. This means I lose a large part of the audience, of course, but it's a matter of principle. I promote the Ukrainian language and a pro-Ukrainian stance. Young people need to understand that you can run a channel in your native language in the gaming sphere and still be successful. Yes, it's a bit harder, but it's possible :) And it really works; I've set an example for dozens, maybe even hundreds of people who started their own business in Ukrainian on Telegram, or at least started, which is also good.)"
        ),
        'projects': (
            "<b>My Channel-Projects</b>\n\n"
            "1. Right now, the easiest way to find me is on the @vertuu_crypto channel, which is most relevant due to Telegram gifts and the general topic of earning money. I post there about 20 times a day.\n\n"
            "2. @vertuu_accounts – also a main channel where I often share my thoughts, but its main purpose is selling my personal PUBG Mobile accounts with a guarantee against recovery, usually a lifetime one, which makes me unique here.\n\n"
            "3. @n1_uc_shop – for everyone who wants to buy UC / popularity / supercars / X-suits / house votes, etc., profitably and safely. Really cheap. Fast and high-quality. And most importantly, it's safe + you support me financially while saving money yourself.\n\n"
            "4. @vertuu_rent – THE CHEAPEST, really the cheapest rental of luxury, rare, stacked PUBG accounts. I only rent out my own, so the prices are kept favorable since there's no need to pay extra to account owners. For a ridiculous 100 UAH, you can rent an account worth 100,000 for a day🙂\n\n"
            "5. Not long ago, I created a new but very functional shop – @n1_tele_shop. There you can buy Telegram Stars, Telegram Premium, TON cryptocurrency (very relevant now) cheaply for UAH. You can also order a search for NFTs, sell your gifts, etc. In short, everything is very cool.\n\n"
            "6. @small_accounts – selling accounts up to $400 from my admins. All are safe and come with a guarantee against recovery. You can also sell your account in that price range to the admins, provided it's safe and profitable for resale.\n\n"
            "7. @vertuu_tiktok – buying/selling TikTok accounts. You can list yours for sale / sell it to an admin or buy an account at a great price. Really great!\n\n"
            "8. @ua_pubgm_store – my first channel, where you can list your PUBG account for sale / purchase one. But all accounts are public, with no guarantee against recovery. There is a guarantee that the purchase will be completely safe.\n\n"
            "9. @ua_store_chat – same functionality, but it's a chat. And it's not just for PUBG now; different people sell their goods or services there, with me or @vertuu_admin as guarantors.\n\n"
            "10. @vertuu_boost – honestly, not very relevant, we don't have many orders. But there is a person who works well, boosts quickly, with high quality, without cheats, and cheaply. Much cheaper than some streamers, for example. And the guarantee from me is reliable.\n\n"
            "11. @vertuuhacks – the project is for sale😁 If interested, write to me, the price is not high.\n\n"
            "12. @tournaments_pm – scrims, custom rooms, tournaments. Currently on pause, but we restart it from time to time, sometimes with new formats, like with streams and good prizes. Worth checking out, the organization is top-notch.\n\n"
            "13. @scammers_spawn – a scammer database where we post IDs of recovered accounts, scammer usernames, etc. There was a previous one, 10 times larger, which Telegram took down for distributing scammers' passports and phone numbers. Even though they are scammers, distributing such information is forbidden on Telegram. The base is not very active right now, but I think we'll revive it.\n\n"
            "14. @exchangerin – the channel just exists, I don't drive traffic to it. It's a currency exchange channel; for this service, write to @currency_exchanging. It's safe and profitable, though sometimes not very fast. But you can exchange thousands of dollars without fear.\n\n"
            "15. @vertuu_account_help – another relic of the past, there's no admin there anymore. For all services, write to me. More precisely, the only relevant service there now is 3-6 device removal + I can also help you with account recovery."
        ),
        'contacts': (
            "<b>Staff Contacts</b>\n\n"
            "1. First and foremost, me. My only contact is @vrt484(@vertuu) – guarantor for deals over 5000 UAH😁 Anyone else with a similar page is a fake.\n\n"
            "2. @vertuu_admin – guarantor for deals up to 5000 UAH and exchanges. Also, contact him for listing an account for sale or buying from the @ua_pubgm_store channel.\n\n"
            "3. @currency_exchanging – my currency exchanger. Helps with transfers / withdrawals, etc.\n\n"
            "4. @uc_shop_admin – for buying UC by ID / popularity / tokens for cars or X-suits, house votes, etc.\n\n"
            "5. @uc_login_admin – for buying UC via QR code (login). This is significantly cheaper than donating by ID and is just as fast and safe.\n\n"
            "6. @tele_shop_admin – contact for buying Stars, Telegram Premium, TON, NFT gifts, boosting, etc.\n\n"
            "7. @sa_seller – for buying accounts with a guarantee, priced up to $400. You can also sell him your account at an urgent price, but only if it's safe and personal.\n\n"
            "8. @smaller_sa – for buying accounts with a guarantee, priced up to $100. You can also sell him yours in the same price range, as long as it's safe and you can vouch for it.\n\n"
            "9. @clans_trade – buying/selling clans.\n\n"
            "10. @vertuu_tt_admin – contact for buying/selling TikTok accounts.\n\n"
            "11. @vertuu_boost_admin – admin who boosts ranks/achievements.\n\n"
            "12. @cards_rent – for renting out your card. It's profitable and safe. There is a risk. Sometimes the card can be blocked.\n\n"
            "13. @vertuu_hacks_admin – contact for buying third-party software, often responds very slowly, probably the worst service among all admins."
        ),
        'reviews': (
            "<b>Reviews</b>\n\n"
            "Over 40k reviews in total, you can read them here:\n"
            "<a href='https://t.me/addlist/EnRkVgV2VHg2OTky'>➡️ Reviews Folder</a>\n\n"
            "Major individual cases:\n"
            "(I don't add account sales for a couple of thousand bucks, as that's almost a daily occurrence)\n\n"
            "• The largest deal in the entire CIS space:\n<a href='https://t.me/vertuu_accounts/3005'>🔗 View</a>\n\n"
            "• The largest deal in Ukraine (before that):\n<a href='https://t.me/vertuu_accounts/2888'>🔗 View</a>\n\n"
            "• Account purchase for $5000:\n<a href='https://t.me/vidguky_ua/11343'>🔗 View</a>\n\n"
            "• One-time purchase of 500,000 UC ($5000) via login:\n<a href='https://t.me/n1_uc_shop/4084'>🔗 View</a>\n\n"
            "• One-time purchase of 165,000 UC ($1700) via login:\n<a href='https://t.me/vidguky_ua/11379'>🔗 View</a>\n\n"
            "• A person sold me a Plush Pepe for $4500 on trust:\n<a href='https://t.me/vertuu_crypto/5718'>🔗 View</a>\n\n"
            "• A person bought a Durov’s Cap from me for $2000 on trust:\n<a href='https://t.me/vertuu_crypto/5036'>🔗 View</a>"
        ),
        "ad": (
        "Advertising is available almost everywhere, and prices vary depending on the subject and promotion method.\n\n"
        "For advertising in @vertuu_accounts and @vertuu_crypto — contact me directly at @vrt484\n\n"
        "For advertising in @small_accounts — contact @sa_seller or @smaller_sa\n"
        "For advertising in @vertuu_rent — contact @orenda_admin\n\n"
        "It's all pretty straightforward — if you want to advertise in a specific channel, just message the admin of that channel, ask about the price,"
        " and make arrangements."
    ),
        'buttons': {
            'about': "About me",
            'projects': "My Channels-Projects",
            'contacts': "Staff Contacts",
            'reviews': "Reviews",
            'ad': "Advertising",
            'back': "⬅️ Back to menu"
        }
    }
}

# Зберігаємо обрану мову для кожного користувача.
# Увага: дані будуть втрачені при перезапуску бота.
# Для постійного зберігання краще використовувати базу даних (напр. SQLite).
user_languages = {}

def get_language_keyboard():
    keyboard = [
        [InlineKeyboardButton("🇺🇦 Українська", callback_data='lang_ua')],
        [InlineKeyboardButton("🇷🇺 Русский", callback_data='lang_ru')],
        [InlineKeyboardButton("🇬🇧 English", callback_data='lang_en')],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_main_menu_keyboard(lang: str):
    buttons = TEXTS[lang]['buttons']
    keyboard = [
        [InlineKeyboardButton(buttons['about'], callback_data='about')],
        [InlineKeyboardButton(buttons['projects'], callback_data='projects')],
        [InlineKeyboardButton(buttons['contacts'], callback_data='contacts')],
        [InlineKeyboardButton(buttons['reviews'], callback_data='reviews')],
        [InlineKeyboardButton(buttons['ad'], callback_data='ad')],
    ]
    return InlineKeyboardMarkup(keyboard)

async def add_user_to_db(user_id: int):
    try:
        cursor.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', (user_id,))
        conn.commit()
    except Exception as e:
        logger.error(f"Помилка додавання користувача в БД: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    await add_user_to_db(user_id)  # Додаємо користувача в базу при старті

    await update.message.reply_text(
        "Будь ласка, оберіть мову / Пожалуйста, выберите язык / Please select a language:",
        reply_markup=get_language_keyboard()
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    data = query.data

    # Додаємо користувача в базу і тут (на випадок, якщо користувач не стартував з /start)
    await add_user_to_db(user_id)

    if data.startswith('lang_'):
        lang = data.split('_')[1]
        user_languages[user_id] = lang
        keyboard = get_main_menu_keyboard(lang)
        await query.edit_message_text(
            text=TEXTS[lang]['start'],
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True
        )
        return

    lang = user_languages.get(user_id, 'ua')
    back_button_text = TEXTS[lang]['buttons']['back']
    back_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(back_button_text, callback_data='main_menu')]])

    if data == 'main_menu':
        keyboard = get_main_menu_keyboard(lang)
        await query.edit_message_text(
            text=TEXTS[lang]['start'],
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True
        )
    elif data in TEXTS[lang]:
        await query.edit_message_text(
            text=TEXTS[lang][data],
            reply_markup=back_keyboard,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True
        )

# Новий хендлер для /members
async def members(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("У тебе немає доступу до цієї команди.")
        return

    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    await update.message.reply_text(f"Кількість користувачів бота: {count}")

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("members", members))  # Додаємо команду /members
    application.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущений...")
    application.run_polling()

if __name__ == "__main__":
    main()