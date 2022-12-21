import discord
from discord.ext import commands
import json
import os
import

os.chdir("C:\\Users\\S1980253\\Downloads\\My discord bot main\\Just making stuff")

client = commands.Bot(command_prefix = ">")


@client.event
async def on_ready():
    print(f"{bot.username} is ready!!")

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
    await open_account(ctx.author)

    users = await get_bank_data()

    earnings = random.randrange(101) # you can change the number to what you want

    await ctx.send(f"Someone gave you {earnings} coins!!")


    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", "w") as f:
        json.dump(users,f)


@client.command()
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)


    if amount == None:
        await ctx.sned("what do you want to withdraw dumb idiot")
        return

    bal = await update_bank(ctx.author)


    if amount>bal[1]:
        await ctx.send("you don't have that much money idiot get a job")
        return
    if amount<0:
        await ctx.send("you idiot it needs to be more than 1")
        return
        
        await update_bank(ctx.author,amount)
        await update_bank(ctx.author, -1*amount,"bank")




    with open("mainbank.json","r") as f:
        users = json.load(f)



async def open_account(user):
    with open("mainbank.json","r") as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return True


async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)

    return users


async def update_bank(user,change = 0,mode = "wallet")
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
