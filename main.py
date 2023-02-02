import socket
import csv
import requests

# This script first tries to extract the IP address and port from each row.
# If the port field is empty, it assumes the port is 80.
# It then attempts to get the IP address from the URL using gethostbyname(),
# and skips to the next row if the URL cannot be resolved.
# Finally, it creates a socket connection to the IP and port,
# and checks if the connection is successful.
# If the connection is successful, it makes a GET request to the URL and checks if the response has a status code of 200,
# which indicates a successful response. The results are stored in a list,
# and finally written to a CSV file named results.csv.

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