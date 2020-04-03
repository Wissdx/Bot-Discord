# coding:utf-8
import discord
import CobraMusic
import asyncio
import hidden_token
import xp_file
ws_url = 'ws://Guesser-Cluster.scoder12.repl.co'
guess_url = 'https://guess-it.scoder12.repl.co/guess'

voiceclient = discord.VoiceClient
client = discord.Client()

BANNED_WORDS = ["pd","nigga","fdp","enculé","encule","connard","salope","pute","con"]

BONJOUR = ["bonjour","salut","bonsoir","yo","hello","salam","shalom","hola","hi","hey"]

@client.event
async def on_ready():
    print("Bonjour monseigneur !")
    
@client.event
async def on_message(message):
    print(message.content)
    member_name = message.author.name
    guild_name = message.guild.name
    if message.author != client.user:
        for w in BONJOUR:
            if message.content.lower().startswith(w):
                await message.channel.send(w + " " + member_name)
        
    if message.author != client.user:
        for word in BANNED_WORDS:
            if word in message.content.lower():
                await message.channel.send("Premier avertissement " + member_name + "! Tu n'as pas le droit d'utiliser ce(s) mot(s) : " + word)
                await message.author.send("Avertissement ! Sur le serveur " + guild_name + " tu ne dois pas utiliser le(s) mot(s) : " + word)
                await message.delete()
                
    if message.content.lower() == "juif":
        await message.channel.send("Salom shabili mi khali mi khouri alekhem")
        
    if message.content == "!carapute":
        await message.channel.send("Sous pute, double pute, octopute ... carapute !")
        
    if message.content == "!presentation":
            em = discord.Embed(title="Présentation", description="Je suis un passionné d'informatique et j'ai codé ce magnifique bot lors d'un coding club de l'école Epitech !", colour=0x2D75CC,
                               timestamp=message.created_at)
            em.add_field(name="Mon prénom", value="Wissem", inline=True)
            em.add_field(name="Mon age", value="16 ans", inline=True)
            em.add_field(name="Une citation", value="Sans dialogue ou introspection critique, la sphère intellectuelle est extrêmement restreinte.", inline=False)
            em.add_field(name="Mon album du moment", value="Stupeflip | 2003", inline=False)
            em.set_author(name="Wissdx, un mec sympa", icon_url=message.author.avatar_url)
            em.set_footer(text="Copyright @Wissdx 2020", icon_url=message.guild.icon_url)
            em.set_image(url="http://rds-engine.com/lecrou.jpg")
            await message.channel.send(embed=em)
            
    if message.content.startswith("!play" or "!p"):
        music_client = await CobraMusic.get_client(message, client)
        await music_client.play(message.content.split()[1]) 
        
    if message.content.startswith("!stop"):
        music_client = await CobraMusic.get_client(message, client)
        await music_client.disconnect()
        await message.channel.send("Je me tais :(")
    
    if message.content == "!help":
        help_msg = message.channel.send("Voici la liste des commandes disponibles : (tu peux dire bonjour et le bot te répond), !carapute, !presentation, !play [insérer une url YouTube], !help.")
        await help_msg
        
# Début du système d'xp

    if message.author != client.user:
        xp_file.xp += 1
        if message.content.startswith("!xp"):
            await message.channel.send(member_name + " tu as " + str(xp_file.xp) + "xp")
            
        if xp_file.xp == 10:
            xp_file.level += 1
            xp_file.xp = 0
            
        if message.content.startswith("!level"):    
            await message.channel.send("Bien joué " + member_name + " tu es niveau " + str(xp_file.level))
    
    

client.run(hidden_token.token)