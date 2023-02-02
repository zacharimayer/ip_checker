# ip_http_checker

# This script first tries to extract the IP address and port from each row.
# If the port field is empty, it assumes the port is 80.
# It then attempts to get the IP address from the URL using gethostbyname(),
# and skips to the next row if the URL cannot be resolved.
# Finally, it creates a socket connection to the IP and port,
# and checks if the connection is successful.
# If the connection is successful, it makes a GET request to the URL and checks if the response has a status code of 200,
# which indicates a successful response. The results are stored in a list,
# and finally written to a CSV file named results.csv.
 
