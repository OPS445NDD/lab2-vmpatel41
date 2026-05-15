#!/usr/bin/env python3

# Author: Satnam Singh
# Author ID: vmpatel41
# Date Created: 2026/05/15

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print('blast off!')
