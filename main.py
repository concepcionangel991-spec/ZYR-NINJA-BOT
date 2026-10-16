import discord
from discord import app_commands
import random
import os  

ID_SERVIDOR = 1540716044329418862  

class MiBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Bot conectado como {self.user}')
        try:
            guild = discord.Object(id=ID_SERVIDOR)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            print("¡Comandos sincronizados con éxito!")
        except Exception as e:
            print(f"Error al sincronizar comandos: {e}")

bot = MiBot()

CUALIDADES = [
    "PRODIGIO 🌟",
    "GENIO 🧠",
    "DOBLE DOUJUTSU 👁️👁️",
    "SANADOR 💚",
    "NINGUNA"
]

@bot.tree.command(name="cualidad", description="Muestra tu rol o cualidad ninja al azar")
@app_commands.checks.cooldown(1, 604800.0, key=lambda i: i.user.id)
async def cualidad(interaction: discord.Interaction):
    cualidad_elegida = random.choice(CUALIDADES)
    if cualidad_elegida == "NINGUNA":
        mensaje = f"❌ ¡{interaction.user.mention}, no obtuviste ninguna cualidad!"
    else:
        mensaje = f"✨ ¡{interaction.user.mention}, tu cualidad asignada hoy es: **{cualidad_elegida}**!"
    await interaction.response.send_message(mensaje)

@cualidad.error
async def cualidad_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            dias = int(error.retry_after // 86400)
            horas = int((error.retry_after % 86400) // 3600)
            mensaje_error = f"⏳ ¡Falta mucho entrenamiento, {interaction.user.mention}! Tienes que esperar **{dias} días y {horas} horas** para volver a usar este comando."
            await interaction.response.send_message(mensaje_error, ephemeral=True)
        else:
            await interaction.response.send_message("Ocurrió un error inesperado al ejecutar el comando.", ephemeral=True)

bot.run(os.environ['TOKEN'
        
