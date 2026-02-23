import socket

COMMON_PORTS = {
    21:"FTP",
    22:"SSH",
    25:"SMTP",
    53:"DNS",
    80:"HTTP",
    110:"POP3",
    139:"NetBIOS",
    143:"IMAP",
    443:"HTTPS",
    445:"SMB",
    3306:"MySQL",
    8080:"HTTP-Proxy"
}

def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except:
        return None

def scan_ports(target):

    ip = resolve_target(target)
    if not ip:
        return None, []

    results=[]

    for port,service in COMMON_PORTS.items():

        s=socket.socket(socket.AF_INET,
                        socket.SOCK_STREAM)
        s.settimeout(0.4)

        try:
            s.connect((ip,port))
            results.append((port,service))
        except:
            pass

        s.close()

    return ip, results

        s.close()

    return ip, results
