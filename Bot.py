import discord
import os
import time
import random
import classes
from discord.ext import commands
from discord import FFmpegPCMAudio

client = commands.Bot(command_prefix='rpg ')

list = []
classes.file_read(list)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.command(pass_context = True)
async def attack(ctx, arg1):
    id1 = ctx.message.author.id
    id2 = int(arg1[3:-1])
    index1 = classes.find_index(id1, list)
    print(id2)
    index2 = classes.find_index(id2, list)
    print(index2)
    attack = list[index1].attack
    defense = list[index2].defense
    hp = list[index2].hp
    str1 = "attackers dmg = " + str(attack) + " defenders defense = " + str(defense) + " defenders hp = "+ str(hp)
    await ctx.send(str1)
    dmg = classes.attack(id1, id2, list)
    if(dmg != 1234567):
        classes.file_write(list)
        newhp = list[index2].hp
        str2 = "defenders new hp = "+ str(newhp)
        await ctx.send(str2)
        await ctx.send("amogus")         
        await ctx.send(file=discord.File('my_image.png'))
    else:
        time_left = round(classes.get_attack_time(id1, list))
        str2 = "You need to wait {} seconds".format(time_left)
        await ctx.send(str2)         
        

f = open("token", "r")
token = f.readline()
f.close()

client.run(token)