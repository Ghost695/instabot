import mega
from config import inst_login, inst_pwd, lang, mega_pwd, mega_login
from instagrapi import Client
from gtts import gTTS

mega = mega.Mega()
m = mega.login(mega_login, mega_pwd)
client = Client()
client.login(inst_login, inst_pwd)

print('Bot started!')
while True:
    try:
        unread_msgs = client.direct_threads(selected_filter='unread')
        for msg in unread_msgs:
            tts = gTTS(msg.messages[0].text, lang=lang)
            tts.save('res.mp3')
            file = m.upload('res.mp3')
            client.direct_send(text=m.get_upload_link(file), user_ids=[msg.messages[0].user_id])
    except Exception as e:
        print(e)
        continue