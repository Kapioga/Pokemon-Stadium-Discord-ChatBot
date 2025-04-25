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
intents.message_content = True
client: Client = Client(intents=intents)

#Bot's Messaging functionality
async def send_message(message : Message, user_message : str) -> None:
    if not user_message:
        print("Message unavailable... Intents not enabled")
        return

    if is_private := user_message[0] == '?':
