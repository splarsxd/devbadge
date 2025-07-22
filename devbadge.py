import os, sys, json, inspect, time, rich, datetime
from discord import Interaction, app_commands, Client, Intents

version = "b1.1"
cls = lambda: os.system("cls" if os.name == "nt" else "clear")
sleep = lambda: os.system("timeout -1 >nul" if os.name == "nt" else time.sleep(5))
os.system("title Devbadge %s by splars#1252" %version if os.name == "nt" else "pass")
os.system("color 0f" if os.name == "nt" else "pass")
cls()

# readsettings3
try:
    with open("config.json") as fileloader:
        config = json.load(fileloader)
except:
    config = {}

token = config.get("token", None)
if token:
    print("Token found in config.\n")
else:
    token = str(input("Token not found in config.\nEnter token: "))

with open("config.json", "w") as fileloader:
    config["token"] = token
    json.dump(config, fileloader, indent=2)

# discordpy setup
intents = Intents.none()
client = Client(intents=intents)
slash = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await slash.sync()
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    nullfile.close()
    time.sleep(1)
    rich.print(inspect.cleandoc(f"""
        [bright_white]Logged in as[/] [bold cyan]{client.user}[/]

        [bright_white]URL invite link for:[/] [bold cyan]{client.user}[/]
        [underline deep_sky_blue4]https://discord.com/oauth2/authorize?client_id={client.user.id}&scope=bot&permissions=0[/]
    """), end="\n\n")

@slash.command()
async def dev(interaction: Interaction):
    '''Grant yourself Discord's Official Active Developer Badge.'''
    rich.print(f"[bright_white]> Success by [cyan]{interaction.user}[/].[/]")
    renewal = (datetime.datetime.now() + datetime.timedelta(days=59)).strftime("%Y-%m-%d")
    await interaction.response.send_message(f"Renewal date: **{renewal}**")

try:
    nullfile = open(os.devnull, "w")
    sys.stdout = nullfile
    sys.stderr = nullfile
    time.sleep(1)
    client.run(token)
except:
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    time.sleep(1)
    rich.print("[bold red]Error:[/] [yellow]The provided token is invalid. Verify your token and try again.[/]")
    sleep()