from re import T
import telebot
token = "5696753261:AAEEwkCdGvWC0ABbJvPIbqQkYAdet1JkeaY"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["horarioBrabo"])
def cronogramaBrabo(message):
    pass

@bot.message_handler(commands=["cronogramaBrabo"])
def horarioBrabo(message):
    print(message)
    cronograma = """
    Cronograma CC2P
    Data: dd/mm/yyyy
    Atv: 
    Arquitetura - 10/10
    Pesq. Ingles - 11/10
    Calculo - 12/10
    Arquitetura - 17/10
    Prod. textual - 19/10

    Provas:

    Ling. de prog 11/10 - Paradigma procedural (procedimentos e funções), pas"""
    bot.send_message(message.chat.id, cronograma) 
@bot.message_handler(commands=["cronogramaBrabo"])
def AdicionarNovaAtividade(menssage):
    pass

def verification(message):
    return True

@bot.message_handler(func=verification)
def test(message):
    warning_message = """
    que tal tentar um comando???????? :
    /cronogramaBrabo
    /horarioBrabo
    /AdicionarNovaAtividade"""
    bot.send_message(message.chat.id, warning_message  )

bot.polling()
