#!/usr/bin/env python3
# -*- coding:utf-8 -*-

print('Result is as following'.center(40, '-'))

for i in range(1, 101):
	if i % 7 == 0:
		continue
	elif i % 10 == 7:
		continue
	elif i // 10 ==7:
		continue
	else:
		print(i)
