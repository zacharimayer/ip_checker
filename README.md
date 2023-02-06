# ip_http_checker

To run the code, you will need to follow these steps:

1. Make sure you have the following Python packages installed: csv, socket, and requests. If you do not have these packages installed, you can install them by running the following command in your terminal: pip install csv socket requests.
2. Export the Nessus data by searching for HTTP servers in your Nessus Scan, then click on "report", select "csv", uncheck all options except for "host" and "port".
3. Save the csv file to the same folder that this code is located on your computer and name it "ips.csv"
4. Open the terminal and go to the ip_checker folder
5. Run the following command: ```python3 http_checker.py```
6. The results will be printed to a file called "results.csv"



