import click

from tcp_scanner import TCPScanner
from utils import expand_ips, expand_ports


@click.command()
@click.option(
    "--host_list",
    prompt="Host list (separated by comma or CIDR block)",
    help="The host list to scan.",
)
@click.option(
    "--port_list",
    prompt="Port list (separated by comma or [first]-[last])",
    help="The port list to scan.",
    default="",
)
@click.option(
    "--timeout",
    prompt="Timeout (empty to standard)",
    help="The timeout to scan.",
    default="0.2",
)
@click.option(
    "--only_show_open", prompt="Only show open (y/n)", help="Only show open ports."
)
@click.option(
    "--show_port_known_service",
    prompt="Show port known service (y/n)",
    help="Show port known service.",
)
def hello(host_list, port_list, timeout, only_show_open, show_port_known_service):
    scanner = TCPScanner(expand_ips(host_list), expand_ports(port_list), float(timeout))
    scanner.scan_ports(only_show_open == "y", show_port_known_service="y")


if __name__ == "__main__":
    hello()
