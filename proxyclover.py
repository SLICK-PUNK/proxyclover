#!/bin/env python3
import argparse
import requests

parser = argparse.ArgumentParser(
    description="Find working HTTPS/SOCKS4/SOCKS5 proxies using the ProxyScrape API with filters. Specify parameters with adequate arguments"
)
parser.add_argument(
    "--fetch",
    action="store_true",
    help="Download the proxies satisying given parameters (proxytype, timeout, ssl, anonymity, country, limit, format, serialkey, age, status, averagetimeout, port",
)
parser.add_argument(
    "--amount",
    action="store_true",
    help="Return the amount of available proxies for the given parameters (proxytype, timeout, ssl, anonymity, country, serialkey, age, status, averagetimeout, port",
)
parser.add_argument(
    "--lastupdated",
    action="store_true",
    help="Return when the proxies were last updated, only requires one parameter (proxytype)",
)
parser.add_argument(
    "--keystatus",
    action="store_true",
    help="the status of a key, only requires one parameter (serialkey)",
)
parser.add_argument(
    "--remaining",
    action="store_true",
    help="return how long a premium serial key remains active. requires one parameter (serialkey)",
)
parser.add_argument(
    "--proxytype", "-p", help="Type of proxy (HTTP/SOCKS5/SOCK4/all) (Default=HTTP)"
)
parser.add_argument(
    "--timeout", "-t", help="The timeout in milliseconds (Default=10000)"
)
parser.add_argument(
    "--country",
    "-c",
    help="Alpha 2 ISO Country Code for  proxy origin, or 'all'. Seperate multiple entries with commas (Eg:DE,IN,US/DE/all) (Default=all)",
)
parser.add_argument(
    "--port", 
    help="Specify proxy port with 1-65525/all (Default=all)"
)
parser.add_argument(
    "--anonymity",
    "-a",
    help="Specify anonymity with 4 options (transparent, anonymous, elite, all) (Default=all)",
)
parser.add_argument(
    "--ssl",
    "-s",
    help="If SSL is to be used. use all if you dont care (yes,no,all) (Default=all)",
)
parser.add_argument(
    "--limit",
    "-l",
    help="Limit the of number proxies to be displayed. No limit by default. (Default=all)",
)
parser.add_argument(
    "--serialkey",
    help="specify ProxyScrape serialkey to fetch premium servers. Not mentioned by default",
)
parser.add_argument(
    "--age", help="age when the proxy was firsrt seen in days. (Default=Unlimited)"
)
parser.add_argument(
    "--status",
    help="Status of proxy (alive) or number of days since offline (Default=alive)",
)
args = parser.parse_args()
requestlist = []
parameters = {"request": "getproxies", "proxytype": "http"}
link = "https://api.proxyscrape.com"


def reqappend(argument, append):
    requestlist.append(append) if eval("args." + argument) == True else None


def paramadd(*items):
    for item in items:
        if eval("args." + item.lower()) != None:
            parameters[item] = eval("args." + item).lower()


def sendreq():
    print("# Start of request " + parameters["request"] + "\n")
    response = requests.get(link, params=parameters)
    print(response.content.decode())
    print("\n# End of request " + parameters["request"] + "\n")


reqappend("fetch", "getproxies")
reqappend("amount", "amountproxies")
reqappend("lastupdated", "lastupdated")
reqappend("keystatus", "keystatus")
reqappend("remaining", "remaining")
paramadd(
    "proxytype",
    "timeout",
    "country",
    "anonymity",
    "ssl",
    "limit",
    "serialkey",
    "age",
    "status",
)
if requestlist != []:
    for element in requestlist:
        parameters["request"] = element
        sendreq()
else:
    sendreq()
