import csv
import socket
import urllib.request

filename = "ips.csv"

with open(filename, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            host = row[0]
            port = row[1] or 80
            if not port:
                port = 80
            port = int(port)
            if "." not in host:
                host = socket.gethostbyname(host)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            result = s.connect_ex((host, port))
            if result == 0:
                try:
                    urllib.request.urlopen("http://" + host + ":" + str(port))
                    print(host + ":" + str(port) + " is up")
                except:
                    print(host + ":" + str(port) + " is down")
            else:
                print(host + ":" + str(port) + " is down")
            s.close()
        except:
            print("Error: Could not resolve host or connect to port.")
