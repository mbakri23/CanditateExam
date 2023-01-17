import requests
import json

ipaddress = "161.185.160.93"
response = requests.get("https://ipinfo.io/"+ipaddress+"/geo")

if(response.status_code!=200):
    print("Web Page did not respond correctly " + response.status_code)
print(response.status_code)



checkfor= ["city","timezone","country","loc"]  

for element in checkfor:
    try:
        test1 = response.json()[element]=="" 
        test2 = response.json()[element]==None 
        if(test1 or test2):
            print(element + " is empty or does not exist")
    
    except KeyError as e:
         print("The Key " + element + " is empty or does not exist")       
    


try: 
    json.loads(text)
except ValueError as error:
    print(error)
     



def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

    if(ipaddress in text):
        print("IP address is valid: " + ipaddress)
    else:
        print("looks like you are behind a firewall and being natted")

    

jprint(response.json())