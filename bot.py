from telethon import TelegramClient, events, sync
from telethon.tl.types import PeerChat
from dotenv import load_dotenv
import os

load_dotenv()

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
chat_id = 848215194

client = TelegramClient('bot_session', api_id, api_hash)


@client.on(events.Raw)
async def handler(update):
    # Print all incoming updates
    print(type(update))
    if (update.__class__.__name__ == 'UpdateChatDefaultBannedRights'):
        can_send_messages = not update.default_banned_rights.send_messages
        print(f'can_send_messages: {can_send_messages}')
        if (can_send_messages):
            await client.send_message(
                entity=PeerChat(chat_id), reply_to=18224, message='Reservar')


@client.on(events.NewMessage())
async def handler(event):
    print("Event Occured")
    print(event.peer_id)
    if (hasattr(event.peer_id, 'chat_id') and event.peer_id.chat_id == chat_id):
        print(event.to_json())


client.start()

# messages = client.iter_messages(entity=PeerChat(chat_id), limit=5)

# for message in messages:
#     print(message.id, message.text)

# dialogs = client.get_dialogs()
# print(dialogs[0].entity)
# for d in dialogs:
#     print(d.name)
#     print(d.entity.id)
#     print(d.entity.title)


# print(client.get_me().stringify())


client.run_until_disconnected()
