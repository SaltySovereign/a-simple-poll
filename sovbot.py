import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
from emoji import emojize
from discord.ext import commands
import asyncio

Client = discord.Client()
bot_prefix = ";;"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def poll(ctx, title, *args):
    print(args)
    print(len(args))
    i = 0
    descript = "\n \n "
    
    
    for x in range(0, len(args)):
        if (i==0):
            descript = descript+":one: = "+str(args[i])+"\n \n"
            
        if (i==1):
            descript = descript+":two: = "+str(args[i])+"\n \n"
            
        if (i==2):
            descript = descript+":three: = "+str(args[i])+"\n \n"
            
        if (i==3):
            descript = descript+":four: = "+str(args[i])+"\n \n"

        if (i==4):
            descript = descript+":five: = "+str(args[i])+"\n \n"

        if (i==5):
            descript = descript+":six: = "+str(args[i])+"\n \n"

        if (i==6):
            descript = descript+":seven: = "+str(args[i])+"\n \n"

        if (i==7):
            descript = descript+":eight: = "+str(args[i])+"\n \n"

        if (i==8):
            descript = descript+":nine: = "+str(args[i])+"\n \n"

        if (i==9):
            descript = descript+":keycap_ten: = "+str(args[i])+"\n \n"
            
        i+= 1
    await client.delete_message(ctx.message)  
    embed = discord.Embed(title=str(title), description=str(descript), color=0xffffff)
    #await client.send_message(ctx.message.author, embed=embed)
    react_message = await client.say(embed=embed)
    
    i = 0
    one = "1"+chr(8419)
    two = "2"+chr(8419)
    three = "3"+chr(8419)
    four = "4"+chr(8419)
    five = "5"+chr(8419)
    six = "6"+chr(8419)
    seven = "7"+chr(8419)
    eight = "8"+chr(8419)
    nine = "9"+chr(8419)
    ten = "\U0001F51F"

    for x in range(0, len(args)):
        if (i==0):
            await client.add_reaction(react_message, one)

        if (i==1):
            await client.add_reaction(react_message, two)

        if (i==2):
            await client.add_reaction(react_message, three)

        if (i==3):
            await client.add_reaction(react_message, four)

        if (i==4):
            await client.add_reaction(react_message, five)

        if (i==5):
            await client.add_reaction(react_message, six)

        if (i==6):
            await client.add_reaction(react_message, seven)

        if (i==7):
            await client.add_reaction(react_message, eight)

        if (i==8):
            await client.add_reaction(react_message, nine)

        if (i==9):
            await client.add_reaction(react_message, ten)

        i+= 1



client.login(process.env.NDMyNDQ2NjcwMzQxNDA2NzIx.DatbJA.3EdUia7w4Ln_C7qYI2_Z2fcSq4M)
