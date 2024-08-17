"""Fetch JSON from URL and display."""

import argparse
import httpx
import json


HOST = "127.0.0.1"
PORT = 8000
RESOURCE = "/"


def main():
    """Main driver."""
    opt = parse_args()
    url = f"http://{opt.host}:{opt.port}{opt.resource}"
    response = httpx.get(url)
    print(response.status_code)
    print(json.dumps(json.loads(response.text), indent=2))


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default=HOST, help="server address")
    parser.add_argument("--port", type=int, default=PORT, help="server port")
    parser.add_argument("--resource", type=str, default=RESOURCE, help="resource path")
    return parser.parse_args()


if __name__ == "__main__":
    main()
