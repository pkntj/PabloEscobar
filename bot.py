from calendar import c
from re import A
from tokenize import Number
from turtle import color
from click import command
import discord #importações do discord
from discord.ext import commands 
import asyncio
import random

ban_gifs = ["https://c.tenor.com/nlNB0Aep-2IAAAAM/thor-fat.gif"]
limpeza_gifs = ["https://c.tenor.com/FT0OSZaHHbcAAAAM/thor-thunder-thor-ragnarok.gif"]
welcome_gifs = ["https://c.tenor.com/ZkbzXhgZwiAAAAAS/cheers-narcos.gif"]



intents = discord.Intents.default()
intents.members = True
Prefix = "c!" #prefixo do bot
client = commands.Bot(command_prefix=Prefix, intents = intents)

@client.event #definimos eventos
async def on_ready():
    print("olá, mundo!")
    print(client.user)

#evento teste

@client.command()
async def dm(ctx):
    embed = discord.Embed(title="Eu queria ser amado!", color=discord.Color.green())
    embed.add_field(name="Campo de texto 1", value="Sub text1") 
    embed.add_field(name="Campo de texto 2", value="Sub texto2") 
    embed.add_field(name="Campo de texto 3", value="Sub texto3") 
    embed.add_field(name="Campo de texto 4", value="Sub texto4") 
    await ctx.author.send(embed=embed)

#teste
@client.command()
async def teste123(ctx, member):
    embed = discord.Embed(title="Foram apagas 82342534 mensagens", color=discord.Color.dark_red())
    embed = discord.Embed(description=f"comando requisitado por{member.id}")
    await ctx.author.send(embed = embed)


@client.event #evento de saudações
async def on_member_join(member):
    canal = client.get_channel(860692037618630656)
    regras = client.get_channel(860692031974277121)
    registro = client.get_channel(860692034104590336)
    embed = discord.Embed(title="Membro novo!")
    embed.add_field(name=f"Bem-vindo,", value=f"{member.mention}!", inline=False)
    embed.add_field(name=f"Leia as regras em:", value=f"{regras.mention}", inline=False)
    embed.add_field(name=f"Registre-se em:", value=f"{registro.mention}.")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Id do usuário: {member.id}") 
    embed.set_image(url=(random.choice(welcome_gifs)))
    await canal.send(embed = embed)

    await asyncio.sleep(15)

    await embed.delete()

    

@client.command()
async def say(ctx, *, mensagem):   

        mensagem = await ctx.send(f"{mensagem}") 
        
        autor = await ctx.mensagem


#comandos de moderação



@client.command(aliases=['clear'])
async def limpar(ctx, amount=11):
    if(not ctx.author.guild_permissions.manage_messages):
        await ctx.send('Você não pode usar esse comando!', color=discord.Color.random())
        return
    amount = amount+1
    if amount > 101:
        embed = discord.Embed(title="Eu não posso apagar mais de 100 mensagens ao mesmo tempo!")
        await ctx.send(embed = embed)
    else: 
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title=f"Mensagens apagadas!")
        embed.add_field(name="Moderador responsável:", value=f"{ctx.author.mention}", inline=False)
        embed.add_field(name="Quantidade de mensagens apagadas:", value=f"{amount}")  
        embed.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed = embed)



@client.command()
async def purge(ctx, membro, amount=11):
    amount = amount+1
    await ctx.message.membro.purge(limit=amount)
    await ctx.send(f"Apaguei {amount} mensagens de {membro.mention}")




@client.command()
async def av(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Avatar de {member}")
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Requisitado por {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)
    await asyncio.sleep(1)
    await ctx.delete()



@client.command()
async def avatar(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    
    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Avatar de {member}")
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Requisitado por {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)
    await asyncio.sleep(1)
    await ctx.message.delete()
    await asyncio.sleep(30)
    await userAvatar.delete()



@client.command()
async def banner(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    userBanner = member.banner_url

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Banner de {member}")
    embed.set_image(url=member.banner_url)
    embed.set_footer(text=f"Requisitado por {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Avatar de {member}")
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Requisitado por {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)



@client.command()
async def kick(ctx, membro : discord.Member, *,motivo=None):
    if(not ctx.author.guild_permissions.administrator):
        await ctx.send('❌Você precisa ter a permissão de expulsar membros.')
        return
    embed = discord.Embed(title="🔨Usuário punido!", color=discord.Color.random())
    embed.add_field(name="🔰Moderador responsável:", value=f"{ctx.author.mention}") 
    embed.add_field(name="Usuário punido:", value=f"{membro.mention}") 
    embed.add_field(name="💬Motivo:", value=f"{motivo}")
    embed.set_footer(text=f"Id do usuário: {membro.id}") 
    embed.add_field(name="Punição Aplicada:", value="Kick") 
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_image(url=(random.choice(ban_gifs)))

    await ctx.send(embed=embed)    

    await membro.kick()

    await asyncio.sleep(2)

    await ctx.message.delete()

   

@client.command()
async def ban(ctx, membro : discord.Member, *,motivo=None):
    if(not ctx.author.guild_permissions.administrator):
        await ctx.send('Você precisa ter a permissão de expulsar membros.')
        return
    embed = discord.Embed(title="🔨Usuário punido!", color=discord.Color.random())
    embed.add_field(name="🔰Moderador responsável:", value=f"{ctx.author.mention}") 
    embed.add_field(name="Usuário punido:", value=f"{membro.mention}") 
    embed.add_field(name="💬Motivo:", value=f"{motivo}")
    embed.set_footer(text=f"Id do usuário: {membro.id}") 
    embed.add_field(name="Punição Aplicada:", value="Banimento") 
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_image(url=(random.choice(ban_gifs)))

    msg = "https://cdn.discordapp.com/attachments/860692037618630656/936794941349318696/F0E85819-05C9-4F56-A7E6-40B455BCCDF1.gif"

    await ctx.send(embed=embed)    

    await membro.ban()

    await ctx.send(msg)

    await asyncio.sleep(2)

    await msg.delete()



@client.command()
async def unban(ctx, membro : discord.Member, *,motivo=None):
    if(not ctx.author.guild_permissions.administrator):
        await ctx.send('Você precisa ter a permissão de expulsar membros.')
        return
    embed = discord.Embed(title="🔨Usuário punido!", color=discord.Color.random())
    embed.add_field(name="🔰Moderador responsável:", value=f"{ctx.author.mention}") 
    embed.add_field(name="Usuário punido:", value=f"{membro.mention}") 
    embed.add_field(name="💬Motivo:", value=f"{motivo}")
    embed.set_footer(text=f"Id do usuário: {membro.id}") 
    embed.add_field(name="Punição Aplicada:", value="Unban") 
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_image(url=(random.choice(ban_gifs)))

    msg = "https://cdn.discordapp.com/attachments/860692037618630656/936794941349318696/F0E85819-05C9-4F56-A7E6-40B455BCCDF1.gif"

    await ctx.send(embed=embed)    

    await membro.unban()

    await ctx.send(msg)

    await asyncio.sleep(2)

    await msg.delete()


@client.command() #definimos comando
async def acorda(ctx):
    msg = f"soninho muito, {ctx.author.mention}"
    await ctx.send(msg)

@client.command()
async def oi(ctx):
    msg = f"passa visão, {ctx.author.mention}."
    await ctx.send(msg)

@client.command()
async def bom_dia(ctx):
    msg = f"bom dia, meu pit!\nNão esquece de se alimentar e beber água em!!"
    await ctx.send(msg)

@client.command()
async def boa_noite(ctx):
    msg = f"boa noite, {ctx.author.mention}! Finalmente indo dormir. Sonha com os anjos e não esquece você é foda! <3"
    await ctx.send(msg)

@client.command()
async def pk(ctx):
    msg = f"O mais brabo daqui!"
    await ctx.send(msg)

@client.command()
async def fazenda(ctx):
    msg = f"https://cdn.discordapp.com/attachments/860692037618630656/937217849926246480/IMG-20220130-WA0008.jpg"
    await ctx.send(msg)

@client.event 
async def on_ready():
    activity = discord.Game(name='prefixo: c!', type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('Olá, mundo!') 
    print(f'{client.user}')

client.run("TOKEN AQUI")#token do bot/login
