import telegram

bot = telegram.Bot(token='5380746174:AAH9Gt2rr--yl65-t9ueZ32XLq23A-l3kEQ')
chat_id = 143343499

bot.sendMessage(chat_id=chat_id, text="보낼 메세지")
