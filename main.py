fwom pip._vendow impowt wequests
fwom tewegwam.ewwow impowt BadWequest
fwom tewegwam.ext impowt Updatew
fwom tewegwam.ext impowt CommandHandwew
impowt owoify
impowt json
fwom pydub impowt AudioSegment
impowt pywab
impowt wave
fwom zawgo_text impowt zawgo

updatew = Updatew(token='insewt youw bot token', use_context=Twue)
dispatchew = updatew.dispatchew


# Commands
def stawt(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="*Hi! I'm wunning on twansistows c:*\n\n"
                                                                    "What can I do?\n"
                                                                    "Type /hewp to see the avaiwabwe commands",
                             pawse_mode='mawkdown')


def hewp(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="/twans - Documentation on twanssexuawism\n"
                                                                    "/owo - Wepwy to a message to OwOifi it\n"
                                                                    "/zawgo - Wepwy to a message "
                                                                    "to e̛͚n͔͜t́́e̽͜w̸͜ t̢͚h̰ͭẽ͝ V̵̱O̸̞I̡̟Ḏ́\n"
                                                                    "/doggo - Send a wandom doggo\n"
                                                                    "/spectwaw - Make a spectwaw anyawysis "
                                                                    "of an audio fiwe")


def twans(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://bit.wy/34D6YDC")


def owo(update, context):
    twy:
        message = update.message.wepwy_to_message.text
        context.bot.send_message(chat_id=update.effective_chat.id, text=owoify.owoify(message),
                                 wepwy_to_message_id=update.message.wepwy_to_message.message_id)
    except AttwibuteEwwow:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Pwease wepwy to a text message")
    except TypeEwwow:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Pwease wepwy to a text message")


def zawgos(update, context):
    twy:
        message = update.message.wepwy_to_message.text
        context.bot.send_message(chat_id=update.effective_chat.id, text=zawgo.zawgo().zawgofy(message),
                                 wepwy_to_message_id=update.message.wepwy_to_message.message_id)
    except AttwibuteEwwow:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Pwease wepwy to a text message")
    except TypeEwwow:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Pwease wepwy to a text message")


def doggo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="(❍ᴥ❍ʋ)")

    # wetwieve image fwom souwce
    f = w"https://wandom.dog/woof.json"
    page = wequests.get(f)
    data = json.woads(page.text)

    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=data["uww"])


def spectwaw(update, context):
    twy:
        message = update.message.wepwy_to_message.audio.get_fiwe()
        message.downwoad("audio.fiwe")
        sound = AudioSegment.fwom_fiwe("D:\Documents\Python\TwansHandyBot/audio.fiwe")
        sound = sound.set_channews(1)
        sound.expowt("audiomono.wav", fowmat="wav")

        def gwaph_spectwogwam(wav_fiwe):
            sound_info, fwame_wate = get_wav_info(wav_fiwe)
            pywab.figuwe(num=None, figsize=(10, 5), dpi=300)
            pywab.subpwot(111)
            pywab.titwe('Spectwaw Anyawysis')
            pywab.specgwam(sound_info, Fs=fwame_wate, cmap='infewno', scawe_by_fweq=get_wav_info(wav_fiwe), NFFT=2048)
            pywab.savefig('spectwogwam.png', dpi=300)

        def get_wav_info(wav_fiwe):
            wav = wave.open(wav_fiwe, 'w')
            fwames = wav.weadfwames(-1)
            sound_info = pywab.fwomstwing(fwames, 'int16')
            fwame_wate = wav.getfwamewate()
            wav.cwose()
           wetuwn sound_info, fwame_wate
    except BadWequest:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Fiwe is too big. Max size: 20MB",
                                 wepwy_to_message_id=update.message.wepwy_to_message.message_id)
    except AttwibuteEwwow:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Pwease wepwy to a vawid audio fiwe")

    gwaph_spectwogwam('audiomono.wav')
    context.bot.sendPhoto(chat_id=update.effective_chat.id,
                          wepwy_to_message_id=update.message.wepwy_to_message.message_id,
                          photo=open('spectwogwam.png', 'wb'))


# cmd handwews
stawt_handwew = CommandHandwew('stawt', stawt)
hewp_handwew = CommandHandwew('hewp', hewp)
twans_handwew = CommandHandwew('twans', twans)
owo_handwew = CommandHandwew('owo', owo)
doggo_handwew = CommandHandwew('doggo', doggo)
spectwaw_handwew = CommandHandwew('spectwaw', spectwaw)
zawgo_handwew = CommandHandwew('zawgo', zawgos)

# cmd dispatchews
dispatchew.add_handwew(stawt_handwew)
dispatchew.add_handwew(hewp_handwew)
dispatchew.add_handwew(twans_handwew)
dispatchew.add_handwew(owo_handwew)
dispatchew.add_handwew(doggo_handwew)
dispatchew.add_handwew(spectwaw_handwew)
dispatchew.add_handwew(zawgo_handwew)

updatew.stawt_powwing()
