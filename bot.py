import os
import discord
from discord import app_commands
from dotenv import load_dotenv
import requests

load_dotenv()
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = discord.Object(id=1506979142329962596)  # paste your server ID as an integer
CHAMPIONSHIP_ID = "f31d714b-53de-4e09-9d3c-6eb0ac85bdbe"  # S58 EU Open5-8 Central - Regular Season
OUR_TEAM_ID = "5a1da5f3-2d56-46d7-b0ae-93491b9ae486"       # Shock N Awe
API_KEY = os.getenv("FACEIT_API_KEY")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="ping", description="Test command", guild=GUILD_ID)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

@tree.command(name="schedule", description="Show our upcoming ESEA matches", guild=GUILD_ID)
async def schedule(interaction: discord.Interaction):
    await interaction.response.defer()

    response = requests.get(
        f"https://open.faceit.com/data/v4/championships/{CHAMPIONSHIP_ID}/matches",
        params={"type": "upcoming", "limit": 100},
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    matches = response.json()["items"]

    embed = discord.Embed(title="Upcoming Matches", color=discord.Color.blue())

    for match in matches:
        faction1 = match["teams"]["faction1"]
        faction2 = match["teams"]["faction2"]

        if faction1["faction_id"] == OUR_TEAM_ID:
            us, opponent = faction1, faction2
        elif faction2["faction_id"] == OUR_TEAM_ID:
            us, opponent = faction2, faction1
        else:
            continue

        timestamp = match["scheduled_at"]
        embed.add_field(
            name=f"{us['name']}  vs  {opponent['name']}",
            value=f"<t:{timestamp}:F>",
            inline=False
        )

    if len(embed.fields) == 0:
        await interaction.followup.send("No upcoming matches found.")
    else:
        await interaction.followup.send(embed=embed)

@client.event
async def on_ready():
    await tree.sync(guild=GUILD_ID)
    print(f"Logged in as {client.user}")

client.run(BOT_TOKEN)