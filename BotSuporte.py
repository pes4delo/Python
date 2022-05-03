from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("SUA-API-TELEGRAM",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Olá Senhor(a), Bem vindo ao suporte do sistema. Por gentileza, digite\
		/ajuda para ver todos os comandos disponiveis.")

def ajuda(update: Update, context: CallbackContext):
	update.message.reply_text("""Comandos disponiveis :
	------------------------------
	/link - Para obter o link de nosso sistema.
	------------------------------
	/resetarsenha -  Para reset de senhas expiradas.
	------------------------------
	/cadastrousuario - Para cadastro de novos usuários.
	------------------------------
	/cadastrofornecedor - Para cadastro de novos fornecedores. """)


def link_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Segue o link do sistema:\
		Link.com.br)")


def reset_senha(update, context):
    chat_id = update.message.chat_id
    document = open('ResetarSenha.docx', 'rb')
    context.bot.send_document(chat_id, document)


def cadastrar_fornecedor(update, context):
    chat_id = update.message.chat_id
    document = open('CadastroFornecedor.docx', 'rb')
    context.bot.send_document(chat_id, document)


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Desculpe '%s' não é um comando válido, digite /ajuda." % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Você digitou:, '%s', não entendi, por gentileza digitar /ajuda." % update.message.text)

def cadastrar_usuario(update, context):
    chat_id = update.message.chat_id
    document = open('CadastroUsuario.docx', 'rb')
    context.bot.send_document(chat_id, document)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('link', link_url))
updater.dispatcher.add_handler(CommandHandler('ajuda', ajuda))
updater.dispatcher.add_handler(CommandHandler('resetarsenha', reset_senha))
updater.dispatcher.add_handler(CommandHandler('cadastrousuario', cadastrar_usuario))
updater.dispatcher.add_handler(CommandHandler('cadastrofornecedor', cadastrar_fornecedor))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown))


updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
