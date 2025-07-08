from discord import Intents, Client, Message, Member, VoiceState
import random
TOKEN = ""
USER_ID_1 = 123
USER_ID_2 = 456
USER_ID_3 = 789
USER_ME = 000
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    # if is_private := user_message[0] == '私':
    #     user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        # if is_private: 
        #     await message.author.send(response)
        # else:
        if("test1" in user_message):
            ran_num = random.randint(1,12)
            if(ran_num <= 3):
                await message.channel.send("123")
            elif(ran_num >= 10):
                await message.channel.send("456")
            elif(ran_num >= 4 and ran_num <= 6):
                await message.channel.send("789")

        if("test2" in user_message and message.author.id == USER_ID_1):
            await message.channel.send("111")
        
        # only react to specific users
        if(message.author.id == USER_ID_1 or message.author.id == USER_ID_2):
            await message.channel.send(response)
                
    except:
        pass

##########################################################################
##########################################################################

@client.event
async def on_ready() -> None:
    print(f'{client.user} is online')



@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(message.author)
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# detect member join voice channel
@client.event
async def on_voice_state_update(member: Member, before: VoiceState, after: VoiceState):
    channel = client.get_channel(1300441324285071381)
    if not before.channel and after.channel and member.id == USER_ID_1:
        print(f'{member} has joined the voice channel')
        await channel.send("<@681722907646361621> hello")

def main() -> None:
    client.run(token=TOKEN)

def get_response(user_input: str) -> str:
    input_msg: str = user_input

    if(input_msg == "test3"):
        return "333"

if __name__ == '__main__':
    main()