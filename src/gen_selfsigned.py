from selfsigned import generate_selfsigned_cert
from ipaddress import IPv4Address

if __name__ == '__main__':
    from config import ssl_cn, ssl_context
    hostname = ssl_cn
    public_ip, private_ip = [IPv4Address('127.0.0.1')]*2
    files = dict()
    files[ssl_context[0]], files[ssl_context[1]] = generate_selfsigned_cert(hostname, public_ip, private_ip)
    for filename, content in files.items():
        with open(filename, 'wb') as f:
            f.write(content)
