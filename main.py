
from telegram  import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from loger import user_ID, count_loger, user_input, count_result
from counter import count

TOKEN = ''

bot = Bot(TOKEN)   
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
start_calc = 0

def start(update:Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Вас привнетствует БОТ "КАЛЬКУЛЯТОР"\nВведите ваше выраженияе для вычисления:')
    context.bot.send_message(update.effective_chat.id, 'Например: 2500 * 0.5 - 4 + 2 * 3.15 - 10 / 7 * 10\nДелить на 0 нельзя, выражение после /0 будет исключено' )
    user_ID(update.effective_chat.id)
    return start_calc

def calc(update:Update, context: CallbackContext):
    data = update.message.text
    user_input(data)
    result = count(data)
    count_result(result)
    count_loger()
    context.bot.send_message(update.effective_chat.id, f"Oтвет:  {count(result)}") 

def bot_off(update:Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Работа окончена')
    return ConversationHandler.END

start_handler = CommandHandler('start', start)
calc_handler = MessageHandler(Filters.text, calc)
bot_off_handler = CommandHandler('off', bot_off)

conv_handler = ConversationHandler(
    entry_points=[start_handler], states={start_calc: [calc_handler]}, fallbacks=[bot_off_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
