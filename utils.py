import ipaddress


def expand_ips(ip_list):
    ips = []
    for ip in ip_list.split(","):
        ip = ip.strip()
        if "/" in ip:
            cidr = ipaddress.ip_network(ip, strict=False)
            ips += [str(ip) for ip in cidr.hosts()]
        else:
            ips.append(ip.strip())
    return ips


def expand_ports(port_list):
    ports = []
    for port in port_list.split(","):
        port = port.strip()
        if "-" in port:
            start_port, end_port = port.split("-")
            ports += list(range(int(start_port), int(end_port) + 1))
        else:
            ports.append(int(port.strip()))
    return ports
