# encoding=utf-8
"""
@author huxujun
@date 2019-06-10
"""
import logging
import telnetlib
import time

from IPy import IP


def parse_ip_address(address: str) -> str:
    try:
        return str(IP(address))
    except:
        pass


def parse_ip_addresses(addresses: str, sep=",") -> list:
    address_list = []
    if addresses:
        for address in addresses.split(sep):
            address = parse_ip_address(address)
            if address:
                address_list.append(address)
    return address_list


def ping(host: str, port=80, timeout=1) -> tuple:
    try:
        return True, telnetlib.Telnet(host, port, timeout).close()
    except Exception as ex:
        return False, ex


def wait_connect(host: str, port=80, wait_sec=10, connect_interval=1) -> bool:
    while wait_sec > 0:
        logging.info("Wait for connecting %s:%s - %s sec", host, port, wait_sec)
        time.sleep(connect_interval)
        logging.info("Try to connect %s:%s...", host, port)
        if ping(host, port)[0]:
            logging.info("Succeed to connect %s:%s", host, port)
            return True
        logging.warning("Failed to connect %s:%s", host, port)
        wait_sec -= connect_interval
    return False


def wait_all_connect(hosts: list, port=80, wait_sec=10, connect_interval=1) -> list:
    error_hosts = hosts.copy()
    while wait_sec > 0 and error_hosts:
        logging.info("Wait for connecting %s:%s - %s sec", error_hosts, port, wait_sec)
        time.sleep(connect_interval)
        logging.info("Try to connect %s:%s...", error_hosts, port)
        for host in error_hosts.copy():
            if ping(host, port)[0]:
                logging.info("Succeed to connect %s:%s", host, port)
                error_hosts.remove(host)
        if error_hosts:
            logging.warning("Failed to connect %s:%s", error_hosts, port)
        wait_sec -= connect_interval
    return error_hosts


def wait_disconnect(host: str, port=80, wait_sec=10, connect_interval=1) -> bool:
    while wait_sec > 0:
        logging.info("Wait for disconnecting %s:%s - %s sec", host, port, wait_sec)
        time.sleep(connect_interval)
        logging.info("Try to disconnect %s:%s...", host, port)
        if not ping(host, port)[0]:
            logging.info("Succeed to disconnect %s:%s", host, port)
            return True
        logging.warning("Failed to disconnect %s:%s", host, port)
        wait_sec -= connect_interval
    return False


def wait_all_disconnect(hosts: list, port=80, wait_sec=10, connect_interval=1) -> list:
    error_hosts = hosts.copy()
    while wait_sec > 0 and error_hosts:
        logging.info("Wait for disconnecting %s:%s - %s sec", error_hosts, port, wait_sec)
        time.sleep(connect_interval)
        logging.info("Try to disconnecting %s:%s...", error_hosts, port)
        for host in error_hosts.copy():
            if not ping(host, port)[0]:
                logging.info("Succeed to disconnecting %s:%s", host, port)
                error_hosts.remove(host)
        if error_hosts:
            logging.warning("Failed to disconnecting %s:%s", error_hosts, port)
        wait_sec -= connect_interval
    return error_hosts


if __name__ == '__main__':
    pass
