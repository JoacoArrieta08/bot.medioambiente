import discord
import random
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

caracteres = ["+", "-", "/", "*", "!", "&", "$", "#", "?", "=", "@", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def join(ctx, member: discord.Member):
    # Envía el mensaje de bienvenida al canal
    await ctx.send(f'Bienvenido/a al servidor, {member.name}! Esperamos que disfrutes tu estancia.')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, largo: int = 10):
    contra = []
    for i in range(largo): 
        contra.append(random.choice(caracteres))
    contra1 = ''.join(contra)
    await ctx.send(f"La contraseña es: {contra1}")

@bot.command()
async def mem(ctx):
    img_mem = os.listdir("img")
    img_mostrar = random.choice(img_mem)
    with open(f'img/{img_mostrar}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

#BOT MEDIO AMBIENTE

@bot.command()
async def consejos(ctx):
    consejos = [
            "Reducir el consumo de plástico: Utiliza bolsas reutilizables de tela en lugar de bolsas de plástico cuando vayas de compras. Evita comprar productos en envases de plástico siempre que sea posible, opta por productos a granel o en envases de papel, vidrio o metal. Lleva tu propia botella de agua reutilizable en lugar de comprar agua embotellada.", 
            "Ahorrar energía en el hogar: Apaga las luces y los aparatos electrónicos cuando no los estés utilizando. Utiliza bombillas LED de bajo consumo energético en lugar de bombillas incandescentes. Aprovecha la luz natural abriendo cortinas y persianas durante el día en lugar de encender luces artificiales.", 
            "Compostaje: Comienza separando los residuos orgánicos, como restos de frutas y verduras, cáscaras de huevo y posos de café, en un contenedor separado. Crea un compostero en tu jardín o utiliza un compostador de interior para convertir los residuos orgánicos en abono natural. Aprende qué materiales son adecuados para compostar y cuáles no lo son, como carne, productos lácteos y aceites.",
            "Transporte sostenible: Utiliza el transporte público, camina o anda en bicicleta siempre que sea posible en lugar de conducir un automóvil. Considera compartir viajes o utilizar servicios de transporte compartido para reducir las emisiones de carbono. Si necesitas un automóvil, elige vehículos con mejor eficiencia de combustible o considera opciones eléctricas o híbridas.",
            "Reducción de residuos: Reduce el uso de productos desechables, como toallas de papel y servilletas, utilizando alternativas reutilizables. Opta por productos duraderos y de alta calidad en lugar de productos de un solo uso. Aprende a reparar y mantener tus pertenencias en lugar de desecharlas y reemplazarlas rápidamente.",
            "Consumo responsable: Investiga sobre las prácticas de las empresas y marcas antes de comprar sus productos, optando por aquellas que sean social y ambientalmente responsables. Prioriza la compra de productos locales y de temporada para reducir la huella de carbono asociada con el transporte de mercancías. Reduce el consumo excesivo y practica el minimalismo, comprando solo lo que necesitas y valorando la calidad sobre la cantidad."
            ]
    await ctx.send(random.choice(consejos))

bot.run(TOKEN)
