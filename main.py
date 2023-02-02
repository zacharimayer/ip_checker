# This script first tries to extract the IP address and port from each row.
# If the port field is empty, it assumes the port is 80.
# It then attempts to get the IP address from the URL using gethostbyname(),
# and skips to the next row if the URL cannot be resolved.
# Finally, it creates a socket connection to the IP and port,
# and checks if the connection is successful.
# If the connection is successful, it makes a GET request to the URL and checks if the response has a status code of 200,
# which indicates a successful response. The results are stored in a list,
# and finally written to a CSV file named results.csv.

import socket
import csv
import urllib.request

output_file = 'output.csv'
with open('ips.csv', 'r') as ips_file:
    reader = csv.reader(ips_file)
    headers = next(reader)
    with open(output_file, 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(['IP/URL', 'PORT', 'WEBPAGE'])
        for row in reader:
            try:
                ip, port = row
                port = int(port) if port.isdigit() else 80
                if '.' in ip:
                    # IP address
                    ip = socket.gethostbyname(ip)
                else:
                    # URL
                    ip = socket.gethostbyname(urllib.request.urlsplit(ip).hostname)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((ip, port))
                sock.close()
                webpage = 'True' if result == 0 else 'False'
                writer.writerow([ip, port, webpage])
            except:
                writer.writerow([ip, port, 'Error'])
