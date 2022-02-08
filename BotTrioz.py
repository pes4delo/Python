from telebot import *


chave_api = "5149068146:AAGN_SU3t3MFpSWL1pLJSnJrzTI9gHx1TOY"

bot = telebot.TeleBot(chave_api)

@bot.message_handler(commands=["bot"])
def boto (mensagem):
    bot.send_message(mensagem.chat.id, "Diga?")

hora = datetime.now()

@bot.message_handler(commands=["call"])
def call (mensagem):
    bot.send_message(mensagem.chat.id, "Soube não?")

@bot.message_handler(commands=["robo"])
def robo (mensagem):
    bot.send_message(mensagem.chat.id, "Chora")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Vai la ver preguiçoso: https://time.is/pt_br/Italy"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Ditadura é errado")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "16/08 FERIADO MUNDIAL")

@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    bot.send_message(mensagem.chat.id, "Trade nao caraaaaa")

@bot.message_handler(commands=["opcao5"])
def opcao5(mensagem):
    bot.send_message(mensagem.chat.id, "3 METROS DE ALTURA")

@bot.message_handler(commands=["opcao6"])
def opcao6(mensagem):
    bot.send_message(mensagem.chat.id, "FAN DE HB20 TURBO REBAIXADO COM NEON E RODA ORBITAL")

@bot.message_handler(commands=["opcao7"])
def opcao7(mensagem):
    bot.send_message(mensagem.chat.id, "EMO GOTICO ROCKEIRO QUE ESCUTA OLIVIA RODRIGO E KELLY KEY")

@bot.message_handler(commands=["opcao8"])
def opcao8(mensagem):
    bot.send_message(mensagem.chat.id, "COMUNISTA E APRECIADOR DE NFT")

@bot.message_handler(commands=["opcao9"])
def opcao9(mensagem):
    bot.send_message(mensagem.chat.id, "MEIO METRO")

@bot.message_handler(commands=["opcao10"])
def opcao10(mensagem):
    bot.send_message(mensagem.chat.id, "CARA DOS CÓDIGOS")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Horario do Gui
     /opcao2 Saber sobre ditaduras
     /opcao3 Trioz Day
     /opcao4 Trade
     /opcao5 Dan
     /opcao6 Marcola
     /opcao7 Gabiru
     /opcao8 Ian
     /opcao9 Guizord
     /opcao10 RodRod
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()
