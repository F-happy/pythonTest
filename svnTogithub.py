#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-05-19 11:25:54
# @Author  : jonnyF (fuhuixiang@jonnyf.com)
# @Link    : http://jonnyf.com


import os, re, pdb, shutil

# os.chdir('C:\\Users\\Jonny\\Documents\\project\\dlnubuy')

# a = os.listdir('C:\\Users\\Jonny\\Documents\\project\\dlnubuy')

# p = re.compile(r'py')
# c = []
# for i in a:
    # pdb.set_trace()
    # b = p.findall(i)
    # if len(b) > 0:
    #     c.append(i)
# print a
# print c
svn = ['C:\\Users\\Jonny\\Documents\\project\\dlnubuy\\dlnubuy',
       'C:\\Users\\Jonny\\Documents\\project\\dlnubuy\\dlnuFHX',
       'C:\\Users\\Jonny\\Documents\\project\\dlnubuy\\templates',
       'C:\\Users\\Jonny\\Documents\\project\\dlnubuy\\autoScript.py',
       'C:\\Users\\Jonny\\Documents\\project\\dlnubuy\\manage.py']

github = ['C:\\Users\\Jonny\\Documents\\GitHub\\test']


def copyFiles(svn, github):
    # pdb.set_trace()
    if os.path.isfile(svn):
        shutil.copyfile(svn, github)
    else:
        # pdb.set_trace()
        shutil.copy(svn, github)
        for i in os.listdir(svn):
            copyFiles(i, github)


for i in svn:
    copyFiles(i, github[0])
