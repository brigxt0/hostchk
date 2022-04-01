import time
import requests
import argparse
from tqdm import tqdm
from rich import print
from functools import wraps
from pathlib import Path
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def banner():
    print(
        """
        [red] (◣_◢)ⱤEViⱠ(◣_◢) [/] presents 
[green] _   _           _       _     _
| | | | ___  ___| |_ ___| |__ | | __
| |_| |/ _ \/ __| __/ __| '_ \| |/ /
|  _  | (_) \__ \ || (__| | | |   <
|_| |_|\___/|___/\__\___|_| |_|_|\_\ [/]  [cyan] @Ver 1.0.1[/]

       Mass Host HttpStatusCode Enumeration
       Report bugs :Telegram [blue] @PwrBroka[/]
 """
    )


def timeit(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()
        print(
            f"Time Taken => [red] {(end_time-start_time)*1}[/]s"
        )  # method.__name__ for debug

        return result

    return wrapper


def get_args():
    """
    Define arguments to be used by the script
    """
    parser = argparse.ArgumentParser(
        description="Mass Host HttpStatusCode Enumerater ",
        prog="hostchk", 
        epilog="Have a nice day :)",
    )
    parser.add_argument(
      "-in", 
      dest="infile", 
      help="Read input from this file name", 
      required=True
    )
    parser.add_argument(
        "-out", 
        dest="outfile", 
        help="Save output to this file name", 
        required=True
    )
    parser.add_argument(
        "-proto",
        dest="protocol",
        help="The protocol to scan with",
        default="https://",
        type=str,
    )
    parser.add_argument(
        "-v",
        help="Print current version number",
        action="store_true"
    )
    return parser


def prototype_req(urls):
    """
    Create a prototype to parse url from file, send get request and receive a response.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
        }
        urls = urls.rstrip()
        req = requests.get(
            args.protocol + "{0}".format(urls),
            headers=headers,
            timeout=5,
            allow_redirects=False,
            verify=False,
        )
        try:
            result = req.headers["Server"]
            return (urls, req, result)
        except Exception as i:
            return ("header not found ", req, urls)
    except requests.exceptions.RequestException as e:
        return (urls, "error:: timeout ")


@timeit
def bulk_req(myfile, lines):
    """
    Create a thread pool wrapped inside tqdm and iterate on the prototype to request specified urls.
    """
    tasks = []
    count = len(lines)
    # index = 0 #for printing to screen

    with tqdm(
        total=count,
        desc="Thinking",
        initial=0,
        unit_scale=True,
        colour="green",
        unit=" urls",
    ) as pbar:
        with ThreadPoolExecutor(max_workers=13) as executor:
            for url in myfile:
                tasks.append(executor.submit(prototype_req, url))
                pbar.update(1)
                # print ( tasks[index].result())
                # index += 1
        for task in as_completed(tasks):
            print(format(task.result()), file=outfile)


parser = get_args()
args = parser.parse_args()
myfile = open(args.infile, "r")
tempfile = open(args.infile, "r")
lines = tempfile.readlines()
outfile = open(args.outfile, "w")


"""if __name__ == "__main__":
    args = parse_args()
    myfile = open(args.infile, "r")
    tempfile = open(args.infile, "r")
    lines = tempfile.readlines()
    outfile = open(args.outpfile, "w")

    banner()
    results = bulk_req(myfile, lines)
    myfile.close()
    outfile.close()"""
