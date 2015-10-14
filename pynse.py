#!/usr/bin/python
import os, sys, argparse, importlib

parser = argparse.ArgumentParser(
        description="pyNSE - An Nmap Python extender")
parser.add_argument("--host", help="Host to process")
parser.add_argument("--port", help="Port to process")
parser.add_argument("--plugin", help="pyNSE plugin to run")
args = parser.parse_args()

def main(args):
    try:
        m = importlib.import_module("plugins.{}".format(args.plugin))
        m.Process(args.host, args.port)
    except:
        sys.exit("pyNSE {} plugin not found.".format(args.plugin))

if __name__ == "__main__":
    if args.host and args.plugin:
        main(args)
    else:
        sys.exit("pyNSE requires a host and plugin.")

