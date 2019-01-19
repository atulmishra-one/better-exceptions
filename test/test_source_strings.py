# -*- coding:utf-8 -*-

import better_exceptions
better_exceptions.hook()


a = b = 0
a + "muti\nlines" + b"prefix" + 'single' + """triple""" + "天天天" + 1 + b
