#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'文档注释'

__author__='xixicjw'

from datetime import datetime

now = datetime.now()
print(now)

dt=datetime(2018,4,22,20,50,59)
dtms=dt.timestamp()

print(dt,dtms)

print(datetime.utcfromtimestamp(dtms))