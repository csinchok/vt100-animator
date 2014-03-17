#!/usr/bin/env python

import urllib2
import sys
import os
import time


def main():
    for url in sys.argv[1:]:
        os.system('clear')
        req = urllib2.urlopen(url)
        for chunk in req.read(16 * 1024):
            for char in chunk:
                sys.stdout.write(char)
                time.sleep(1.0 / 1500.0)


if __name__ == "__main__":
    main()
