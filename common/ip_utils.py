# encoding=utf-8
"""
@author huxujun
@date 2019-06-10
"""
from IPy import IP


def parse_ip_address(address: str) -> str:
    try:
        return str(IP(address))
    except Exception as ex:
        pass


def parse_ip_addresses(addresses: str, sep=",") -> list:
    address_list = []
    for address in addresses.split(sep):
        address = parse_ip_address(address)
        if address is not None:
            address_list.append(address)
    return address_list


if __name__ == '__main__':
    pass
