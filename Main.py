from telethon import TelegramClient
from conf import api_id, api_hash
client = TelegramClient("sesion", api_id, api_hash)
async def main():
    me = await client.get_me()
    print(me.stringify())
with client:
    client.loop.run_until_complete(main())