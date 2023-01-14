import requests

def main():
    r = requests.get("IP LOGGING WEBSITE", timeout=2)
    time = str(r.elapsed).split(".")[:2]
    miliseconds = time[1][:2]
    print(f"LOGGED IN {miliseconds} MILISECONDS")


if __name__ == "__main__":
    main()
