from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

from responses import Get_Response


#Safely loads Discord Token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#Bot Setup
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

#Bot's Messaging functionality
async def send_message(message : Message, user_message : str) -> None:
    if not user_message:
        print("Message unavailable... Intents not enabled")
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response :str = Get_Response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print (e)

#Bot Startup Handling
@client.event
async def on_ready() -> None:
    print(f'{client} is running')

#Bot Message Handler
@client.event
async def on_message( message : Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str (message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

#Main Bot Function
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()