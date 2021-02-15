import discord
import pymongo
from discord.ext import commands, tasks
import random
from random import randint
import youtube_dl
import asyncio
from datetime import datetime as DT
client = pymongo.MongoClient("mongodb+srv://Snide:Famille252002@cluster0.bbl3z.mongodb.net/db.ticket?retryWrites=true&w=majority")
db = client.test

bot = commands.Bot(command_prefix = "Y!", description = "Bot de YTB Fantastiks", intents = discord.Intents().all(), help_command=None) 
warnings = {}
status = ["Pour connaître mes commandes utilise Y!help",
        "Mon créateur est Snide#0001"] 
#musics = {}
#ytdl = youtube_dl.YoutubeDL()

@bot.event
async def on_ready(): 
    print("Ready !")
    changeStatus.start()

color = [
    0xFFD400,
    0xFF0000,
    0xFF007C,
    0xBD00FF,
    0x5D00FF,
    0x0027FF,
    0x00FFE4,
    0x00FF9E,
    0x00FF4D,
    0xB6FF00,
]

@bot.command()
async def start(ctx, secondes = 5):
    changeStatus.change_interval(seconds = secondes)

@tasks.loop(seconds = 20)
async def changeStatus():
    game = discord.Game(random.choice( status))
    await bot.change_presence(status = discord.Status.online, activity = game)

#@bot.command()
#async def changeStatusOnline():
    #await bot.change_presence(status = discord.Status.online) 


@bot.command()
async def coucou(ctx):
    await ctx.send("**Coucou !** <a:infini:799193284031152139>")

@bot.command()
async def serverInfo(ctx, users):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    embed = discord.Embed(title = "Info Du Serveur")
    embed.add_field(name =  "Voici les infos du serveur", value =  f" \n \n Le serveur **{serverName}** contient *{numberOfPerson}* personnes. \n \n Il y a {users} \n \n  Ce serveur possède {numberOfTextChannels} salon écrit ainsi que {numberOfVoiceChannels} vocaux.")
    await ctx.send(embed = embed)
 
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban (ctx, user : discord.Member, *, reason = "Aucune raison n'a été donné"):
 if user.top_role >= ctx.author.top_role:
    await ctx.send("Tu ne peux pas bannir les personnes en dessous ou qui ont les mêmes rôles que toi !")
    return
 else:
        await ctx.guild.ban(user, reason = reason)
        embed = discord.Embed(title = "**Banissement**", description = "Un modérateur à banni un membre !", url = "https://www.youtube.com/channel/UCo70mMtkP59fw5spQ0rFkhA", color=0xfa8072)
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/BanneHammer.png")
        embed.add_field(name = "Membre banni", value = user.name, inline = False)
        embed.add_field(name = "Raison", value = reason)
        embed.add_field(name = "Modérateur", value = ctx.author.name)
                
        await ctx.send(embed = embed)

@bot.command()
async def help(ctx, info = None):
    if info == None:
        embed = discord.Embed(title = "Voici mes commandes", description = "**__Vous avez le choix entre ces catégories de commandes__ :**", colour = 0xfa8072)
        embed.add_field(name = "Modération", value = "`help Modérations`")
        embed.add_field(name = "Embed", value = "`help embed`")
        embed.add_field(name = "Musique", value = "`help musique`")

        await ctx.send(embed = embed)

    if info == "moderation":
        embed = discord.Embed(title="__Commande de Modération__",description="Voici les commandes de Modérations, toutes abus du staff sera sanctionné", colour =0xfa8072)  
        embed.add_field(name="`Y!ban <@non de l'utilisateur> <raison du ban>`",value="Bannit un membre du serveur.", inline=False)
        embed.add_field(name= "`Y!clear <nombre de message>`",value="Efface les messages dans un canal particulier.", inline=False)
        embed.add_field(name="`Y!kick <@nom de l'utilisateur> <raison de l'expulsement>` ",value="Expulse un membre du serveur.", inline=False)
        embed.add_field(name="`(Pas encore opérationel)Y!warn <@nom de l'utilisateur> <raison du warn>`",value="Avertit un membre.",inline=False)
        embed.add_field(name="`Y!mute <@nom de l'utilisateur> <raison du mute>`",value = "Interdit d'écrire à la personne sur le serveur", inline=False)
        embed.add_field(name="`Y!unmute <@nom de l'utilisateur>`",value = "Redonne la permission à la personne de parler",inline=False)
        embed.add_field(name="`!unban <nom de l'utilisateur avec le tag avec des guillemet entre la première et la dérnière lettre> <Raison du unban>",value="retire le ban de la personne")
        await ctx.send(embed=embed)

    if info == "fun":
        embed = discord.Embed(title="Commande de fun", colour =0xfa8072)  
        embed.add_field(name="Qi",value="Vous donne votre Qi ou celui de la personne mentioné.\n\n Mais ne vous inquitez pas la suite arrive<a:load:802533198747533332>", inline=False)
        await ctx.send(embed = embed)


@bot.command()
async def tarifs(ctx):
    embed=discord.Embed(title=":art: •Prix du shop des graphistes• :moneybag: ")
    embed.add_field(name = "__:bust_in_silhouette: • Tarifs des logos__", value = "•→ `Logo simple` **• 1.00€** `ou` pub pour le __serveur__ & le __graphiste__. \n •→ `Logo medium` **• 2.00€.**", inline = False)
    embed.add_field(name =  "\n __:camera_with_flash: • Tarif Miniature__", value =" •→ `Miniature basique` **• 1.00€** (image de fond + skin copié collé + écriture dessus) `ou` pub pour le __serveur__ & le __graphiste__. \n •→ `Miniature premium` (libre demande)**• 2.00€.** \n •→ `Logo gif` **• 1.00€** `ou` pub pour le __serveur__ & le __graphiste__. \n \n **__:computer:• Tarif screen Fortnite/ensemble Fortnite déjà fait__**", inline = False)
    embed.add_field(name = "__:computer:• Tarif Montage vidéo__", value = " •→ `Montage vidéo basique` •1.00€ `ou` pub pour le __serveur__ & le __graphiste__. \n •→ `Montage audio` **• 0.50€** `ou` pub pour le __serveur__ & le __graphiste__. •→ `Montage avancé` (libre demande)**• 2.00€**.", inline = False)
    embed.add_field(name = "__:gift:• Tarif Intro vidéo__", value = "•→ `Intro  basique` (intro déjà faite) + son + images que vous voulez mettre a des moments)** • 1.00€** . \n •→ `Intro premium` (libre demande) **• 2.00€**. \n \n :city_sunset: **• Voici les tarifs des commandes screen/pack •** :euro:", inline = False)
    embed.add_field(name = ":computer:__• Tarif screen Fortnite/ensemble Fortnite déjà fait__", value = "•→ `1 screen` (déjà fait) **• 0.10€** `ou` pub pour le __serveur__ & le __graphiste__. \n •→ `2 screens`  (déjà fait) **• 0.20€.** \n •→ `3 screens` (déjà fait) **• 0.40€.** \n •→ `4 screens`  (déjà fait) **• 0.80€.** \n •→ `1 screen personnalisé` (libre demande) **• 1.50€.** \n \n \n `• Payement accepté : PayPal / nitro • les tarifs peuvent êtres modifiés à tous moments`")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/775715318492168222/791217377601126410/standard-7.gif" )
    await ctx.send(embed = embed)



@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *reason):
 if user.top_role >= ctx.author.top_role:
    await ctx.send("Tu ne peux pas expulser les personnes en dessous ou qui ont les mêmes rôles que toi !")
    return
 else:
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    embed = discord.Embed(title = "Expulsion", description = "Un modérateur à expulser un membre")
    embed.add_field(name = "Raison de l'expulsement :", value = reason)
    embed.add_field(name = "Modérateur", value = ctx.author.name)
    
    await ctx.send(embed = embed)





@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return
    
    if "discord.gg/" in message.content.lower():
        role_names = [role.name for role in message.author.roles]
        if "👮‍♀️・staff" in role_names:
            return
        
        else:
            await message.delete()
            await message.channel.send(f"{message.author.mention} a envoyé une invitation")
    else:
        pass
        
    await bot.process_commands(message)



async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole

async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    
    return await createMutedRole(ctx)

@bot.command()
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
 if user.top_role >= ctx.author.top_role:
    await ctx.send("Tu ne peux pas mute les personnes en dessous ou qui ont les mêmes rôles que toi !")
    return
 else:
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été mute !")

@bot.command()
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
 if user.top_role >= ctx.author.top_role:
    await ctx.send("Tu ne peux pas unmute les personnes en dessous ou qui ont les mêmes rôles que toi !")
    return
 else:
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été unmute !")



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "je m'inscris" in message.content.lower():
        await message.channel.send(f"{message.author.mention} Tu es désormais inscris à la cup", delete_after = 5)
        await message.delete()

        
        channel = bot.get_channel(793478766982725663) 
        await channel.send(f"{message.author.mention}")
    else:
            pass
    await bot.process_commands(message)



class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

@bot.command()
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []

@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()


@bot.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()


@bot.command()
async def skip(ctx):
    client = ctx.guild.voice_client
    client.stop()


def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
        , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

    client.play(source, after=next)


@bot.command()
async def play(ctx, url):
    print("play")
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"Vous êtes prêt ? : {video.url}")
        play_song(client, musics[ctx.guild], video)


@bot.command()
@commands.has_role("👮‍♀️・Staff")
async def oooo(ctx, membre: discord.Member):
    #pseudo = membre.mention
    id = membre.id

    # si la personne n'a pas de warning
    if id not in warnings:
        warnings[id] = 0
        print("Le membre n'a aucun avertissement")

    warnings[id] += 1

    print("ajoute l'avertissement", warnings[id], "/3")
    await bot.get_channel(784698478935932960).send(f"{Member.mention} tu à été warn tu à maintenant {warnings[id]} warns avant le ban.")

    # verifier le nombre d'avertissements
    if warnings[id] == 3:
        # remet à les warnings
        warnings[id] = 0
        # message
        await membre.send("Vous avez été banni du serveur parce que tu ne réspectais pas les règles du serveur !")
        # ejecter la personne
        await membre.ban()

    # mettre à jour le fichier json
    with open('warnings.json', 'w') as outfile:
        json.dump(warnings, outfile)

    await ctx.send(f"Le membre {pseudo} a reçu une alerte ! Attention à bien respecter les regles")




bot.command()
async def embed(arg):
    pass
    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')


@bot.command()
async def embedt(ctx ,*arg):
    embed = discord.Embed(title = arg)

    await ctx.send(embed = embed)


@bot.command()
async def coucous(ctx):
  random_answer = ["Salut !", 
                "Bonjour",
                "coucou"]
  answer = random.choice(random_answer)
  await ctx.send(answer)




@bot.command(name='avatar', aliases=['Avatar', 'av'])
async def avatar(ctx, user: discord.Member):
    embed = discord.Embed(title = f"Voici l'avatar de {user}", color=0xff0000)
    embed.set_image(url=f"{user.avatar_url}")
    await ctx.send(embed = embed)
    await ctx.message.delete()

@avatar.error
async def avatar_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed = discord.Embed(title = f"Voici l'avatar de {ctx.author}", color =0xff0000)
        embed.set_image(url = f"{ctx.author.avatar_url}")
        await ctx.send(embed = embed)
        await ctx.message.delete()


@bot.command()
async def unban(ctx, user, *reason):
 if user.top_role >= ctx.author.top_role:
    await ctx.send("Tu ne peux pas unban les personnes en dessous ou qui ont les mêmes rôles que toi !")
    return
 else:
	    reason = " ".join(reason)
	    userName, userId = user.split("#")
	    bannedUsers = await ctx.guild.bans()
	    for i in bannedUsers:
		    if i.user.name == userName and i.user.discriminator == userId:
			    await ctx.guild.unban(i.user, reason = reason)
			    await ctx.send(f"{user} à été unban.")
			    return
	#Ici on sait que lutilisateur na pas ete trouvé
	    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")


@bot.command()
async def ticket(ctx, *,reason = "Aucune raison"):
	random_number = random.randint(1111, 9999)
	category_neme = "TICKET"
	category = discord.utils.get(ctx.guild.categories,
	name=category_neme
	)
	creation_ticket = await ctx.guild.create_text_channel(f"ticket-{random_number}", 
	category=category
	)
	await ctx.message.delete()
	await creation_ticket.set_permissions(ctx.message.author, 
												read_messages=True, 
												send_messages=True,
												read_message_history=True
	)										  
	channels = ctx.guild.text_channels
	for channel in channels:
		if channel.name == (f"ticket-{random_number}"):

			emb_ticket = discord.Embed(title="TICKET D'AIDE", color=random.choice(color))
			emb_ticket.add_field(name="__**INFORMATIONS**__", 
			value=(" > Bonjour a toi,\n > Ton ticket sera pris en compte le plus rapidement posible par \n > l'equipe de modération,\n > Si tu souhaite mettre fin a cette discussion tu a juste a taper le mot \"close\""), inline = False)
			emb_ticket.add_field(name="__**RAISON**__", value=reason)

			await channel.send(f"Ticket crée par {ctx.message.author.mention}")
			await channel.send(embed=emb_ticket)

			def check_in(message):
				return message.content == "close" and creation_ticket == message.channel

			try:
				ferme_ticket = await bot.wait_for("message", check = check_in, timeout=None)
				emb_close_ticket = discord.Embed(title="Se ticket va s'auto detruire dans 5 secondes", color=random.choice(color))
				await channel.send(embed=emb_close_ticket)
				await asyncio.sleep(1)
				await channel.send("5")
				await asyncio.sleep(1)
				await channel.send("4")
				await asyncio.sleep(1)
				await channel.send("3")
				await asyncio.sleep(1)
				await channel.send("2")
				await asyncio.sleep(1)
				await channel.send("1")
				await asyncio.sleep(1)
				await channel.delete()
			except TimeoutError:
				await channel.delete()



@bot.command()   
async def server(ctx):
        embed = discord.Embed(title="Server information",
                      timestamp=DT.utcnow())

        embed.set_thumbnail(url=ctx.guild.icon_url)

        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        fields = [("ID", ctx.guild.id, True),
                  ("Owner", ctx.guild.owner, True),
                  ("Region", ctx.guild.region, True),
                  ("Serveur crée le", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                  ("Membres", len(ctx.guild.members), True),
                  ("Humains", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                  ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                  ("Membres Bannis", len(await ctx.guild.bans()), True),
                  ("Statues", f":green_circle: {statuses[0]} :orange_circle: {statuses[1]} :red_circle: {statuses[2]} :white_circle: {statuses[3]}", True),
                  ("Salons Textuels", len(ctx.guild.text_channels), True),
                  ("Salons Vocaux", len(ctx.guild.voice_channels), True),
                  ("Categories", len(ctx.guild.categories), True),
                  ("Roles", len(ctx.guild.roles), True),
                  ("Invites", len(await ctx.guild.invites()), True),
                  ("\u200b", "\u200b", True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

@bot.command()
async def embed(ctx):
    message = await ctx.send(f"Voulez-vous commencé la configuration de votre embed ? ")
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    await ctx.send(embed = embed)

    def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

    def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

    try:
        reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = checkEmoji)
        if reaction.emoji == "✅":
            await ctx.send("La configuration de l'embed a commencé.")
        else:
            await ctx.send("La configuration de l'embed a bien été annulé.")
    except:
        await ctx.send("La configuration de l'embed a bien été annulé.")
    
        return

    message = await ctx.send(f"Voulez-vous mettre un titre ?")
    await message.add_reaction("✅")
    await message.add_reaction("❌")


@bot.command()
async def dm(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    serverName = ctx.guild.name
    embed = discord.Embed(title = 'Modération', description = f'Tu as reçu un message de l\'équipe de Modération de {ctx.guild.name}', color=0x037ef0)
    embed.add_field(name = ' Message :', value = f'{reason}')
    embed.set_thumbnail(url = f'{ctx.guild.icon_url}')
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.message.delete() 
    await user.send(embed = embed)
    embed=discord.Embed(title=f"{message.auhtor} j'ai bien envoyé le message en mp à {user}")
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *text):
    if ctx.message.content.lower() == "@everyone" or ctx.message.content.lower() == "@here":
        await ctx.send("Tu n'a pas le drois de mentioner !")
    else:
        await ctx.send(" ".join(text))
        await ctx.message.delete()


@bot.command()
async def ping(ctx):
    await ctx.send(f"**__Pong__ :** {round(bot.latency*1000)}ms**")

@bot.command()
@commands.has_permissions(manage_channels = True)
@commands.has_permissions(administrator= True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send( ctx.channel.mention + " **:WhiteMask2: Le channel a été lock !**")

@bot.command()
@commands.has_permissions(manage_channels=True)
@commands.has_permissions(administrator= True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + "  Le salon à bien été dévérouillé !")


#@bot.command()
#async def nuke(ctx):
    #user = discord.User
    #wuser = "<@!{}>".format(ctx.author.id)
    #await ctx.channel.send('Nuke en cours…')
    #await asyncio.sleep(2)
    #await ctx.channel.purge(limit=None)
    #await ctx.channel.send(f'Ce salon a été nuke par : {wuser}')
    #await ctx.channel.send('https://tenor.com/view/explosion-nuke-boom-nuclear-gif-5791468')


@bot.command()
async def invites( ctx, user : discord.User):
        totalInvites = 0
        for i in await message.guild.invites():
            if i.inviter == user:
                totalInvites += i.uses
        await message.channel.send(f"Tu as invité {totalInvites} membres {'' if totalInvites == 1 else 's'} sur le serveur !")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "<@781217154385051648>" in message.content.lower():
        await message.channel.send(f"Bonjour {message.author} moi c'est Les Fantastiks.\nMon préfix est  Y! , tu peux effectuer la commande Y!help pour voir toute mes commandes")
    if "<@!781217154385051648>" in message.content.lower():
         await message.channel.send(f"Bonjour {message.author} moi c'est Les Fantastiks.\nMon préfix est  Y! , tu peux effectuer la commande Y!help pour voir toute mes commandes")
    else:
         pass
    await bot.process_commands(message)


#@bot.command()
#async def blackliste(ctx):
    #embed = dicord.Embed(name="Voici la liste des membres banni :")
    #embed.add_field(name =f"Membres Bannis {len(ctx.guild.bans()}",)
    #await ctx.send(embed=embed)


@bot.event
async def on_raw_reaction_add(payload):

    channels = bot.get_channel(809089468693741640)
    msg = await channels.fetch_message(810113394652217396)
    role1 = get(ctx.guild.roles, id=784534548994064394)

    def check_a(reaction):
        return msg.id == reaction.message.id and reaction.emoji == "✔"

    await member.add_roles(role1)


@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")
        
    if reason is None:
        return await ctx.send("Please provide a reason for warning this user.")

    try:
        first_warning = False
        bot.warnings[ctx.guild.id][member.id][0] += 1
        bot.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        bot.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = bot.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{member.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(f"{member.mention} has {count} {'warning' if first_warning else 'warnings'}.")



@bot.command()
@commands.has_permissions(administrator=True)
async def warnings(ctx, member: discord.Member=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")
    
    embed = discord.Embed(title=f"Displaying Warnings for {member.name}", description="", colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in bot.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning {i}** given by: {admin.mention} for: *'{reason}'*.\n"
            i += 1

        await ctx.send(embed=embed)

    except KeyError: # no warnings
        await ctx.send("This user has no warnings.")

#@bot.event
#async def on_raw_reaction_add(payload):
    #msgID = 810113394652217396
    #user = payload.user_id
    #member = payload.member

#guild_id = payload.guild_id
#guild = discord.utils.find(lambda g : g.id == guild_id, bot1.guilds)
#role = get(member.guild.roles, name="test réact")

#if payload is not None:
    #if payload.message_id == msgID:
        #if str(payload.emoji) == "✔️":
        #await member.add_roles(role)

@bot.command()
async def mm(ctx, *text, random:random.choice ):
    randint = random.choice(random_randint)
    reason = " ".join(text)
    embed = discord.Embed(title="Question :", description=text) 
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.add_field(name="réponse", value=(random.randint("Oui", "Non", "Peut-être")))

    await ctx.send (embed=embed)

@bot.command(pass_context = True)
async def Qi(ctx, user : discord.User):
    embed = discord.Embed(title =f"Voici le QI de {user}", description = (random.randint(0, 230)))
    await ctx.send (embed = embed)

@Qi.error
async def Qi(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        embed = discord.Embed(title = f"Voici ton Qi {ctx.author}", description = (random.randint(0, 230)))
        await ctx.send(embed = embed)

@bot.command()
async def ball(ctx, *text):
    reponse = random.choice("Oui","Non", "Peut-être")
    embed = discord.Embed(title =f"Question : {text}", description = f" Réponse :  {reponse}")
    print(reponse)
    await ctx.send(embed = embed)


#@bot.command()
#async def ball8(ctx):
    #reason = " ".join(reason)
  #random_answer = ["Peut-être !", 
                #"Oui",
                #"Non"]
  #answer = random.choice(random_answer)
  #await ctx.send(answer)

@bot.command()
async def clear(ctx, nombre : int):
   await ctx.channel.purge(limit = nombre + 1)
   await ctx.send(f"**Les messages on bien été supprimés !**")


bot.run("TOKENN")
