import time
from datetime import datetime as dt

hosts_path = 'C:\Windows\System32\drivers\etc\hosts'
hosts_temp = 'C:\Python Training\Websiteblocker\hosts\hosts'

redirect = '127.0.0.1'

website_list = ['www.facebook.com','www.youtube.com']

while True:
    if(dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16)):
        print('Working Hours...')
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if(website in content):
                    pass
                else:
                    #Mapping the hostnames to yours localhost IP address
                    file.write("\n" + redirect + " " + website)
    else:
        print('Fun Hours...')
        with open(hosts_temp,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            
            file.truncate()
            
    time.sleep(5)     