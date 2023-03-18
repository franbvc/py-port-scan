import json
import socket

with open("clean_dict.json") as f:
    WELL_KNOWN_PORTS = json.load(f)


class TCPScanner:
    target_hosts: list[str] = []
    target_ports: list[int] = []
    open_ports: dict[str, list[int]] = {}
    timeout: float = 0.2

    def __init__(
        self, target_hosts: list[str], target_ports: list[int], timeout: float = 0.2
    ):
        self.target_hosts = target_hosts
        self.target_ports = target_ports
        self.timeout = timeout

        self.open_ports = {host: [] for host in self.target_hosts}

    def scan_port(
        self,
        target_host: str,
        target_port: int,
        only_show_open: bool = True,
        show_port_known_service: bool = True,
    ):
        """Attempts to connect to a given port on a given host."""
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(float(self.timeout))
            client_socket.connect((target_host, target_port))

            if (
                show_port_known_service
                and WELL_KNOWN_PORTS.get(str(target_port)) is not None
            ):
                print(
                    f"[+] {target_host} : {target_port} ({WELL_KNOWN_PORTS[str(target_port)]})"
                )

            else:
                print(f"[+] {target_host} : {target_port}")

            self.open_ports[target_host].append(target_port)

            client_socket.close()

        except:
            if not only_show_open:
                if (
                    show_port_known_service
                    and WELL_KNOWN_PORTS.get(str(target_port)) is not None
                ):
                    print(
                        f"[-] {target_host} : {target_port} ({WELL_KNOWN_PORTS[str(target_port)]})"
                    )
                else:
                    print(f"[-] {target_host} : {target_port}")

    def scan_ports(
        self, only_show_open: bool = True, show_port_known_service: bool = True
    ):
        for host in self.target_hosts:
            for port in self.target_ports:
                self.scan_port(host, port, only_show_open, show_port_known_service)
