from pip._vendor import requests
from telegram.error import BadRequest
from telegram.ext import Updater
from telegram.ext import CommandHandler
import owoify
import json
from pydub import AudioSegment
import pylab
import wave
from zalgo_text import zalgo

updater = Updater(token='insert your bot token', use_context=True)
dispatcher = updater.dispatcher


# Commands
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="*Hi! I'm running on transistors c:*\n\n"
                                                                    "What can I do?\n"
                                                                    "Type /help to see the available commands",
                             parse_mode='markdown')


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="/trans - Documentation on transsexualism\n"
                                                                    "/owo - Wepwy to a message to OwOifi it\n"
                                                                    "/zalgo - Reply to a message "
                                                                    "to e̛͚n͔͜t́́e̽͜r̸͜ t̢͚h̰ͭẽ͝ V̵̱O̸̞I̡̟Ḏ́\n"
                                                                    "/doggo - Send a random doggo\n"
                                                                    "/spectral - Make a spectral analysis "
                                                                    "of an audio file")


def trans(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://bit.ly/34D6YDC")


def owo(update, context):
    try:
        message = update.message.reply_to_message.text
        context.bot.send_message(chat_id=update.effective_chat.id, text=owoify.owoify(message),
                                 reply_to_message_id=update.message.reply_to_message.message_id)
    except AttributeError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please reply to a text message")
    except TypeError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please reply to a text message")


def zalgos(update, context):
    try:
        message = update.message.reply_to_message.text
        context.bot.send_message(chat_id=update.effective_chat.id, text=zalgo.zalgo().zalgofy(message),
                                 reply_to_message_id=update.message.reply_to_message.message_id)
    except AttributeError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please reply to a text message")
    except TypeError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please reply to a text message")


def doggo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="(❍ᴥ❍ʋ)")

    # retrieve image from source
    f = r"https://random.dog/woof.json"
    page = requests.get(f)
    data = json.loads(page.text)

    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=data["url"])


def spectral(update, context):
    try:
        message = update.message.reply_to_message.audio.get_file()
        message.download("audio.file")
        sound = AudioSegment.from_file("D:\Documents\Python\TransHandyBot/audio.file")
        sound = sound.set_channels(1)
        sound.export("audiomono.wav", format="wav")

        def graph_spectrogram(wav_file):
            sound_info, frame_rate = get_wav_info(wav_file)
            pylab.figure(num=None, figsize=(10, 5), dpi=300)
            pylab.subplot(111)
            pylab.title('Spectral Analysis')
            pylab.specgram(sound_info, Fs=frame_rate, cmap='inferno', scale_by_freq=get_wav_info(wav_file), NFFT=2048)
            pylab.savefig('spectrogram.png', dpi=300)

        def get_wav_info(wav_file):
            wav = wave.open(wav_file, 'r')
            frames = wav.readframes(-1)
            sound_info = pylab.fromstring(frames, 'int16')
            frame_rate = wav.getframerate()
            wav.close()
            return sound_info, frame_rate
    except BadRequest:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="File is too big. Max size: 20MB",
                                 reply_to_message_id=update.message.reply_to_message.message_id)
    except AttributeError:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Please reply to a valid audio file")

    graph_spectrogram('audiomono.wav')
    context.bot.sendPhoto(chat_id=update.effective_chat.id,
                          reply_to_message_id=update.message.reply_to_message.message_id,
                          photo=open('spectrogram.png', 'rb'))


# cmd handlers
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
trans_handler = CommandHandler('trans', trans)
owo_handler = CommandHandler('owo', owo)
doggo_handler = CommandHandler('doggo', doggo)
spectral_handler = CommandHandler('spectral', spectral)
zalgo_handler = CommandHandler('zalgo', zalgos)

# cmd dispatchers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(trans_handler)
dispatcher.add_handler(owo_handler)
dispatcher.add_handler(doggo_handler)
dispatcher.add_handler(spectral_handler)
dispatcher.add_handler(zalgo_handler)

updater.start_polling()
