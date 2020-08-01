#!/usr/bin/python3

import syslog
import time

while True:
    text = input('$ ')
    syslog.syslog(syslog.LOG_LOCAL6 | syslog.LOG_INFO, text)

