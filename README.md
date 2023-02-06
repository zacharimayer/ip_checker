# ip_http_checker

This script first tries to extract the IP address and port from each row.
If the port field is empty, it assumes the port is 80.
It then attempts to get the IP address from the URL using gethostbyname(), and skips to the next row if the URL cannot be resolved.

Finally, it creates a socket connection to the IP and port, and checks if the connection is successful.
If the connection is successful, it makes a GET request to the URL and checks if the response has a status code of 200, which indicates a successful response. The results are stored in a list, and finally written to a CSV file named results.csv.
 
# Requirements

Python 3, requests.

To install requests: 
```pip3 install request```

# Instructions:

In order to run this code, you will need a csv name ips.csv file with 2 columns:
- IP addresses
- Ports

Place the ips.csv file into the ip_checker folder and run:
``````
python3 main.py
``````