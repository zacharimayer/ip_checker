import socket
import csv
import requests

results = []

with open("ips.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            ip, port = row
        except ValueError:
            continue

        if not port:
            port = 80

        try:
            ip = socket.gethostbyname(ip)
        except socket.gaierror:
            results.append([ip, port, False])
            continue

        try:
            s = socket.create_connection((ip, int(port)), timeout=5)
        except (socket.timeout, ConnectionRefusedError):
            results.append([ip, port, False])
        else:
            s.close()
            try:
                r = requests.get(f"http://{ip}:{port}")
                if r.status_code == 200:
                    results.append([ip, port, True])
                else:
                    results.append([ip, port, False])
            except:
                results.append([ip, port, False])

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["IP", "PORT", "RESOLVES"])
    writer.writerows(results)