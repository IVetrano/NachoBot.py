import discord
import random
import asyncio
from dotenv import load_dotenv
import os
import textos

NO_LOLEROS = [	641803467425447946,		# NachoNoGuide
				627391601831837696,		# Falcon
				565345833063809054,		# Gallardo
				215246995324010496,		# Macco
				410944349589864448,		# Idoboga
				396025475123773450,		# Toumas
				199290456461410315,		# Acosta
				574413933528612884		# Julian
			]

#------------------------------------------------------------ Inicializo el bot
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

prefix = "NachoBot "

@client.event
async def on_ready():
	print('Nos conectamos como {0.user}'.format(client))
#------------------------------------------------------------------------------

#-------------------------------------------------Cuando entra un nuevo miembro
@client.event
async def on_member_join(member):
	for channel in member.server.channels:
		await client.send_message(f"Bienvenido a la Virgocueva {member.mention} ")
#------------------------------------------------------------------------------

#----------------------------------------------------------------Con un mensaje
@client.event
async def on_message(message):
	
	if message.author == client.user:
		return

	# Expulsar temporalmente no loleros chistositos
	if message.role_mentions and message.author.id in NO_LOLEROS:
		roles_mencionados = [role.name for role in message.role_mentions]
		if "Loleros" in roles_mencionados:
			guild = message.guild
			try:
				await message.author.send(textos.frase_ban() + " 5 minutos de recreillo")
				await guild.kick(message.author, reason="Menciono un rol prohibido")
				await message.channel.send(f"{message.author.mention} \n {textos.frase_voxera()} \n En 5 minutos volves")

				# Esperar 5 minutos
				await asyncio.sleep(300)

				# Crear una nueva invitación y enviarla por DM
				invite = await guild.text_channels[0].create_invite(max_uses=1, unique=True)
				await message.author.send(f"Te dimos un recreíllo y ya estás de vuelta. Que sea sin bromitas esta vez, ¿sí, chistosillo? \n {invite.url}")
			
			except discord.Forbidden:
				await message.channel.send("No tengo permisos para expulsar a este usuario.")
			except discord.HTTPException:
				await message.channel.send("Hubo un error al intentar expulsarlo.")

	if message.content.startswith(prefix):
		
		comando = message.content.split()[1]                          #Encuentro el comando
			
		indice_comando = message.content.index(comando)               #Encuentro la posicion del comando
			
		argumento = message.content[indice_comando + len(comando):]   #Argumento es el mensaje desde que termino el comando hasta el finale

		if comando == "hola":
			await message.channel.send("Hola " + message.author.mention + ", todo cheto?")
			
		if comando == "chau":
			await message.channel.send("Nos vemos " + message.author.mention + "!")
				
		if comando == "decir":
			await message.channel.send(argumento)
					
					
		if comando == "rollear":
			cantidad = len(argumento.split(", "))
			numero = random.randint(-1, cantidad - 1)
			embed = discord.Embed(title = argumento.split(", ")[numero], description = "Porque sí")
			await message.channel.send(content=None, embed = embed)
				
		if comando == "pregunta":
			respuestas = ["Sí", "No", "Tal vez", "No sé", "Definitivamente", " Claro "," sisi "," nono "," Por supuesto! ","No sé"," Por supuesto que no ","Desde ya que si","Desde ya que no"]
			respuesta = respuestas[random.randint(-1, len(respuestas) - 1)]
			embed = discord.Embed(description=respuesta)
			await message.channel.send(content = message.author.mention + " a lo que me dijo '" + argumento + "' mi respuesta es " + respuesta, embed=embed)
			
		if comando == "reaccion":
			respuestas = ["¿Por qué?","XD", "Vamoo", "Como en Dark Souls!", "Eso es una referencia a Homestuck", "lol","que govir", "XD", "este esta ranciovich", "Domado"]
			respuesta = respuestas[random.randint(-1, len(respuestas) - 1)]
			embed = discord.Embed(description=respuesta)
			await message.channel.send(content = message.author.mention + " a lo que me dijo '" + argumento + "' mi reaccion es " + respuesta, embed=embed)
		
		if comando == "equipos":
			cantidad = len(argumento.split())
			integrantes = argumento.split()
			n_integrantes = cantidad/2
			equipo1 = []
			equipo2 = []
			for i in range(0, cantidad):
				if len(equipo1) < n_integrantes and len(equipo2) < n_integrantes:
					n_equipo = random.randint(1,2)
					if n_equipo == 1:
						equipo1.append(integrantes[i])
						print(integrantes[i] + " equipo1")
					else:
						equipo2.append(integrantes[i])
						print(integrantes[i] + " equipo2")
				elif len(equipo1) >= n_integrantes:
					equipo2.append(integrantes[i])
					print(integrantes[i] + " equipo2")
				elif len(equipo2) >= n_integrantes:
					equipo1.append(integrantes[i])
					print(integrantes[i] + " equipo1")
			embed = discord.Embed(title = "Equipos")
			embed.add_field(name="Buenardovich", value=equipo1)
			embed.add_field(name="VS", value="vs")
			embed.add_field(name="Picantovic", value=equipo2)
			await message.channel.send(content= message.author.mention + " acá tenés ranciovich", embed=embed)
				
		if comando == "dab":
			await message.channel.send("https://cdn.glitch.com/6353980a-f25a-4fd8-ab49-da62c9504e1d%2F2962cbec-5cdd-47ec-98de-0bf666b698fc_DAB.png?v=1601669406341")
		
		if comando == "momo":
			sujeto = ["tu gfa ", "tu awelita ", "tu elfa ", "un grasoso ", "un holkiano ", "el peniways ", "Acosta gracioso ", "NachoGuide ",
								"Lincrey ", "Idoboga ", "Nisman ", "Acosta pro ", "el Colo ", "Gochalo ", "el cabezon Tinelli ", "el sujeto ", "el maligno ", "el ladron ",
								"el luz extinguido ", "la creatura ", "el Hokague ", "Dross ", "el Rubius ", "un curifeo ", "NachoBot "]
			
			accion = ["no te ama", "se muere", "cumple años", "mira nopor", "es de legion holk", "es grasoso", "se retira",
								"te avienta un nokia", "esta DEVeando", "estudia", "se come un trava", "juega al LoL", "juega al DayZ", 
								"juega al Rocket League", "no DEVea", "hace un momazo", "no va a la virgofest", "se vuelve voxerdo", "trollea",
								"se cambia el apodo de discord", "te cambia el apodo de discord", "te banea", "es baneado", "es el impostor",
								"es SUS", "es negro", "es racista", "hace momos en video"]
			
			imagenes = ["https://imgur.com/BYc6fjG", "https://imgur.com/QDXZrk3", "https://imgur.com/kjmGWW4", "https://imgur.com/dD6NEt5",
									"https://imgur.com/hu1BbGg", "https://imgur.com/uLJcRyH", "https://imgur.com/y0kOpcu", "https://imgur.com/KxkdqkZ",
									"https://imgur.com/RDgT2XA", "https://imgur.com/Z9bvaiW", "https://imgur.com/tVszhB6", "https://imgur.com/6JwQpVY",
									"https://imgur.com/i9nxNxU", "https://imgur.com/KwXj5T5", "https://imgur.com/79iVWlc", "https://imgur.com/5e1WXKO",
									"https://imgur.com/kSGqL3A", "https://imgur.com/xKQiLdx", "https://imgur.com/8tO2sj3", "https://imgur.com/fRPNkhM",
									"https://imgur.com/OsmjvYD", "https://imgur.com/rJjfTBe", "https://imgur.com/A0oJoNq"]
			
			sujeto_1 = sujeto[random.randint(-1, len(sujeto) - 1)]
			sujeto_2 = sujeto[random.randint(-1, len(sujeto) - 1)]
			
			accion_1 = accion[random.randint(-1, len(accion) - 1)]
			accion_2 = accion[random.randint(-1, len(accion) - 1)]
			
			imagen_1 = imagenes[random.randint(-1, len(imagenes) - 1)]
			imagen_2 = imagenes[random.randint(-1, len(imagenes) - 1)]
			
			res = "When " + sujeto_1 + accion_1 + "\n" + imagen_1 + "\n" + "But " + sujeto_2 + accion_2 + "\n" + imagen_2
			await message.channel.send(content = message.author.mention + " aca tenes un momazo:")
			await message.channel.send(content = "When " + sujeto_1 + accion_1)
			await message.channel.send(content = imagen_1)
			await message.channel.send(content = "But " + sujeto_2 + accion_2)
			await message.channel.send(content = imagen_2)
			await message.channel.send(content = ":v xdxdxdxdxdxd")
			
			
		if comando == "RepetirRojo":
			if random.choice([True, False]):
				await message.channel.send(content = "https://imgur.com/4KmbqP5")
				await message.channel.send(content = message.author.mention + " No te lo vas a creer, pero" + "```diff\n-" + argumento[1:] + " hihihihihihihihihihihyahyahyahhahhah!" + "\n```")
			else:
				await message.channel.send(content = "https://imgur.com/nvEnsbE")
				await message.channel.send(content = message.author.mention + " ME NIEGO!!! ya verás el por qué\n" + "hihihihihihihihihihihyahyahyahhahhah!")
		
		if comando == "RepetirLeet":
			await message.channel.send(content = "https://c.tenor.com/sz5PGIaFe0UAAAAC/terezi-terezipyrope.gif")
			await message.channel.send(content = message.author.mention + str_a_leet(argumento))

		if comando == "anime":
			await message.channel.send("https://cdn.glitch.com/6353980a-f25a-4fd8-ab49-da62c9504e1d%2F2962cbec-5cdd-47ec-98de-0bf666b698fc_animeee3.png?v=1601669375160")
		
		if comando == "como" and argumento == " en dark souls":
			await message.channel.send("https://youtu.be/JNLQJcv2pj4")
			
		if comando == "bakamitai":
			await message.channel.send("https://www.youtube.com/watch?v=VgeBUREDC3g&feature=youtu.be")
		
		if comando == "miracles":
			await message.channel.send("https://www.youtube.com/watch?v=_-agl0pOQfs")
			
		if comando == "me" and argumento == " rindo":
			await message.channel.send("Te fuiste domado")
		
		if comando == "entragovir":
			canal = message.author.voice.channel
			await canal.connect()
			await message.channel.send(message.author.mention + " ya entre al chat de voz")
		
		if comando == "andate":
			await client.user.voice_channel.disconnect()
			await message.channel.send(message.author.mention + " Bue loco")
		
		if comando == "jefe" and argumento == " maestro":
			await message.channel.send("Jefe Maestro, ¿Pero qué haces?, ¿que haces con la mano? ¿Que te ha dado? Que te crees ahora un gato o un animal o algo por el estilo, no me digas que te has vuelto trolo.", tts=True)
	
		if comando == "ayuda":
				embed = discord.Embed(title="Comandos", description="Luego de escribir 'NachoBot ' escriba:")
				embed.add_field(name="hola", value="Para que NachoBot lo salude")
				embed.add_field(name="decir INSERTE TEXTO AQUÍ", value="Para que diga lo que escribiste")
				embed.add_field(name="rollear INSERTE OPCIONES AQUÍ", value="Para que rollee entre las opciones que me diste las cuales deben estar separadas por comas y espacios")
				embed.add_field(name="pregunta INSERTE PREGUNTA AQUÍ", value="Para que responda lo que me preguntaste, DEBEN SER PREGUNTAS QUE SE RESPONDAN CON SI O NO")
				embed.add_field(name="reaccion INSERTE AFIRMACION AQUÍ", value="Para que reaccione a lo que escribiste")
				embed.add_field(name="equipos INSERTE NOMBRES DE PARTICIPANTES AQUÍ", value="Para que para que arme 2 equipos con los nombres escritos, DEBEN ESTAR SEPARADOS POR ESPACIOS")
				await message.channel.send(content=None, embed=embed)

		if comando == "entra":
			channel = message.author.voice.channel
			await channel.connect()
		if comando == "andate":
			await message.voice_client.disconect()

		if comando == "PeopleJustAintNoGood":
			YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
			FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
			channel = message.author.voice.channel
			voice = await channel.connect()
			url = "https://www.youtube.com/watch?v=RVLbhg-OPHY&ab_channel=NickCave%26TheBadSeeds-Topic"

			if not voice.is_playing():
				with YoutubeDL(YDL_OPTIONS) as ydl:
					info = ydl.extract_info(url, download=False)
				URL = info['formats'][0]['url']
				voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
				voice.is_playing()
			else:
				await ctx.send("Ya estoy reproduciendo govir!!")
				return

		if comando == "OdioALosChinardos":
			YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
			FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
			channel = message.author.voice.channel
			voice = await channel.connect()
			url = "https://www.youtube.com/watch?v=IoLz7OOJCFg"

			if not voice.is_playing():
				with YoutubeDL(YDL_OPTIONS) as ydl:
					info = ydl.extract_info(url, download=False)
				URL = info['formats'][0]['url']
				voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
				voice.is_playing()
			else:
				await ctx.send("Ya estoy reproduciendo govir!!")
				return

#-------------------------------------------------------------------------------

#def hola():
#keep_alive()
#  mantener_vivo()
#  time.sleep(10)
		
#timer = threading.Thread(target=hola)
#timer.start()

def str_a_leet(string):
	string = string.upper()
	string = list(string)
	reemplazo = {"A": "4", "I": "1", "E": "3", "S": "5", "G": "6", "T": "7", "B": "8", "O": "0"}
	for i in range(len(string)):
		string[i] = reemplazo.get(string[i], string[i])
	string = "".join(string)
	return string


client.run(TOKEN)