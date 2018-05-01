#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'文档注释'

__author__='xixicjw'

import hashlib
md=hashlib.md5()
md.update('how to use md5 in '.encode('utf-8'))
md.update('python hashlib?'.encode('utf-8'))
print(md.hexdigest())