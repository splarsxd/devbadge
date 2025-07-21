import os, sys, json, inspect, time, rich, datetime
from discord import Interaction, app_commands, Client, Intents

prefix = "devbadge by splars#1252"
cls = lambda: os.system("cls" if os.name == "nt" else "clear")
sleep = lambda: os.system("timeout -1 >nul" if os.name == "nt" else time.sleep(5))
os.system("title %s" % prefix if os.name == "nt" else "pass")
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
        [gray]Logged in as[/gray] [bold cyan]{client.user}[/bold cyan]

        [gray]URL invite link for:[/gray] [bold cyan]{client.user}[/bold cyan]
        [underline deep_sky_blue4]https://discord.com/oauth2/authorize?client_id={client.user.id}&scope=bot&permissions=0[/underline deep_sky_blue4]
    """), end="\n\n")

@slash.command()
async def dev(interaction: Interaction):
    '''Grant yourself Discord's Official Active Developer Badge.'''
    rich.print(f"> Success by [cyan]{interaction.user}[/cyan].")
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
    rich.print("[bold red]Error:[/bold red] [yellow]The provided token is invalid. Verify your token and try again.[/yellow]")
    sleep()