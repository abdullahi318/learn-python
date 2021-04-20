#!/usr/bin/env python3

import time

def main():
    """Print the latest tutorial from Real Python"""
    tic = time.perf_counter()
    val = [str(i) for i in range(1000)]
    toc = time.perf_counter()
    print(f"List populated in {toc - tic:0.4f} seconds")

    print(val)

if __name__ == "__main__":
    main()
