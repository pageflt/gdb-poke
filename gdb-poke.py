#!/usr/bin/env python
# coding: utf-8
#
# GDB remote protocol debugging aid
# Dimitris Karagkasidis <t.pagef.lt@gmail.com>
# https://github.com/pageflt/gdb-poke 

import sys
from socket import socket, AF_INET, SOCK_STREAM

def usage():
    return "Usage:\n%s DATA [HOST:PORT]" % sys.argv[0]


def send_packet(data, host="127.0.0.1", port=1234):
    cs = sum([ord(c) for c in data]) % 256
    pkt = "+$%s#%02x" % (data, cs)

    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host,port))
        s.send(pkt)
        s.close()
    except Exception as ex:
        raise Exception("Could not send the packet: %s" % ex)


def main():
    try:
        if len(sys.argv) == 2:
            send_packet(sys.argv[1])
        elif len(sys.argv) == 3:
            addr = sys.argv[2].split(":")
            send_packet(sys.argv[1], addr[0], int(addr[1]))
        else:
            print usage()
            return(1)
        return(0)
    except Exception as ex:
        sys.stderr.write("%s\n" % ex)
        return(1)


if __name__ == "__main__":
    sys.exit(main())

