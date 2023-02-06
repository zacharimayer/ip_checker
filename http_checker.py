import csv
import socket
import requests

def check_ip(ip, port, protocol):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return True
        else:
            return False
    except socket.gaierror:
        return False

def check_url(url, port):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

with open('ips.csv') as file:
    reader = csv.reader(file)
    headers = next(reader)
    with open('results.csv', 'w', newline='') as results_file:
        writer = csv.writer(results_file)
        writer.writerow(['IP/URL', 'Port', 'HTTP Checked', 'HTTP Result', 'HTTPS Checked', 'HTTPS Result'])
        for row in reader:
            ip_or_url = row[0].strip()
            port = int(row[1].strip()) if row[1].strip().isdigit() else 80
            if '.' in ip_or_url:
                print(f'Now checking IP: {ip_or_url}:{port}')
                http_result = check_ip(ip_or_url, port, 'http')
                https_result = check_ip(ip_or_url, port, 'https')
                writer.writerow([ip_or_url, port, True, http_result, True, https_result])
                print('Done.')
            else:
                print(f'Now checking URL: {ip_or_url}:{port}')
                http_result = check_url(f'http://{ip_or_url}', port)
                https_result = check_url(f'https://{ip_or_url}', port)
                writer.writerow([ip_or_url, port, True, http_result, True, https_result])
                print('Done.')
print('Process completed. Please see check results file for details.')
