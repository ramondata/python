#!/usr/bin/env python3

# -*- encoding:utf-8 -*-

from subprocess import PIPE
from subprocess import Popen

sub_1: None = Popen(args="ls",
                    shell=True,
                    stdin=None,
                    stdout=PIPE,
                    stderr=PIPE)

#out, err = sub_1.communicate()
#print(out, err)

sub_1.stdout.close()

sub_2: None = Popen(args="pwd",
                    shell=True,
                    stdin=None,
                    stdout=PIPE,
                    stderr=PIPE)

out, err = sub_2.communicate()
print(out, err)