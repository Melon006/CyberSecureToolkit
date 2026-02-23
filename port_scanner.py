import socket

COMMON_SERVICES = {
    21:"FTP",
    22:"SSH",
    80:"HTTP",
    443:"HTTPS",
    3306:"MySQL"
}

def scan_ports(target):

    results=[]

    for port,service in COMMON_SERVICES.items():

        s=socket.socket()
        s.settimeout(0.5)

        try:
            s.connect((target,port))
            results.append((port,service))
        except:
            pass

        s.close()

    return results
