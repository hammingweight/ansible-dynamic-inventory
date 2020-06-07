#!/usr/bin/env python
import argparse
import json
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Skeleton dynamic inventory")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true")
    group.add_argument("--host")
    return parser.parse_args()


def list_hosts():
    # TODO: Implement
    return {}


def get_host(host):
    # TODO:
    return {
        "ansible_host": "127.0.0.1"
    }


def main():
    args = parse_args()
    if args.list:
        hosts = list_hosts()
        json.dump(hosts, sys.stdout)
    elif args.host:
        host = get_host(args.host)
        json.dump(host, sys.stdout)


if __name__ == "__main__":
    main()