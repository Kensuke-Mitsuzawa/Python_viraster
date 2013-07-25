#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys, codecs;

input_lines=codecs.open(sys.argv[1], 'r', 'utf-8').readlines();

for line in input_lines:
    for item in line.split():
        print item.encode('utf-8');
