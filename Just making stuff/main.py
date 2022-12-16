import discord
from discord.ext import commands
import json
import os
import

os.chdir("C:\\Users\\S1980253\\Downloads\\Just making stuff")

client = commands.Bot(command_prefix = ">")

@client.command()
async def balance(ctx):
    await open_account(ctx.author)

    user = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_users = users[str(user.id)]["bank"]

    em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.Blue)
    em.add_field(name = "Wallet",value = wallet_amt)
    em.add_field(name = "Bank balance",value = bank_amt)
    await ctx.send(embed = em)


@client.command()
async def beg(ctx):


    with open("mainbank.json","r") as f:
        users = json.load(f)



async def open_account(user):
    with open("mainbank.json","r") as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return True


async def get_bank_data():
    