#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Passing arguments to threads when they are created
"""
#end_pymotw_header

import threading
import time


def worker(num):
    """thread worker function"""
    print 'Worker: %s' % num
    print time.ctime()
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()


# my test
# not use threading, serialize
# for i in range(5):
# 	worker(i)