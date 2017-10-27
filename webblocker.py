import time
from datetime import datetime as d

hostlocation="/etc/hosts"
redirect="127.0.0.1"
websites=["varzesh3.com","www.varzesh3.com"]

while True :
    if d(d.now().year, d.now().month, d.now().day, 2 ) < d.now() < d(d.now().year, d.now().month, d.now().day, 3 ):
        with open(hostlocation,'r+') as file:
            content=file.read()
            print (content)
            print (type(content))
            for i in websites:
                if i in content:
                    pass
                else:
                    file.write(redirect+" "+ i + "\n")
    else:

        print("Free Hours")
        with open(hostlocation,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)
