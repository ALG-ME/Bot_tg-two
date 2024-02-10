import telebot
import random

TOKEN = 'Тут должен быть токен'
bot = telebot.TeleBot(TOKEN)

quotes = {
    1: "Чем больше я узнаю, тем больше понимаю, насколько мало я знаю. - Сократ",
    2: "Жизнь — это то, что с тобой происходит, пока ты строишь планы. - Джон Леннон",
    3: "Лучший способ предсказать будущее — создать его. - Питер Друкер",
    4: "Великие умы обсуждают идеи, средние умы обсуждают события, мелкие умы обсуждают людей.  - Елеонора Рузвельт",
    5: "Победа без опасности равна победе без славы. - Пьер Корнейль",
    6: "Только те, кто смеются над собой, способны по-настоящему радоваться жизни. - Шарль Чаплин",
    7: "Лучший способ завершить что-то — начать делать это. - Дзижи Келлер",
    8: "Самое ценное — это время, которое вы уделяете другим. - Дэйл Карнеги",
    9: "Самое важное — это не перестать задавать вопросы. - Альберт Эйнштейн",
    10: "Истина не в том, чтобы иметь много друзей, а в том, чтобы иметь друзей, на которых можно положиться. - Аристотель",
    11: "Будьте изменением, которое вы хотели бы увидеть в мире. - Махатма Ганди",
    12: "Самое лучшее время начать что-то новое — это сейчас. - Кэтрин Паттерсон",
    13: "Великие дела часто начинаются с малых сделок. - Сократ",
    14: "Завтра — это мистическая страна, где пока что мы не жили. - Федор Достоевский",
    15: "Самое ценное — это время, которое вы уделяете другим. - Дэйл Карнеги"
}


# тут функция для удобства которая содержит приветствие
def send_greeting(message):
    bot.reply_to(message, 'Привет! Я бот с мотивационными цитатами. Отправь <code>/motivation</code>,  чтобы получить дозу мотивации.', parse_mode='html')


# Обработка команды motivation, random_key - переменная в которой выбирается рандомный ключ, random_quote - хранит сам ключ после рандомизации
@bot.message_handler(commands=['motivation'])
def send_motivation(message):
    random_key = random.choice(list(quotes.keys()))
    random_quote = quotes[random_key]
    bot.reply_to(message, f'''Мотивационная цитата для тебя:
{random_quote}''')


# обработка любого сообщения, и выдача приветствия из функции send_greeting
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    send_greeting(message)


# Инициализация запуска (Бесконечного)
bot.infinity_polling()

