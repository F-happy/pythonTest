#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-21 17:50:27
# @Author  : jonnyF (fuhuixiang@jonnyf.com)
# @Link    : http://jonnyf.com

x = int(input('你要计算斐波纳契数列的前几项？（PS：必须大于等于3）：'))
a_list = [1, 1]
print('以下是计算过程')
for i in range(x-2):
    n = a_list[len(a_list)-2]
    n_1 = a_list[len(a_list)-1]
    a_list.append(n + n_1)
    print 'n =%s' % n
    print 'n_1=%s' % n_1
    print '这是斐波纳契数列的第%s项：%s' % (len(a_list),a_list[len(a_list)-1]))
print '这是为你精心炮制的斐波纳契数列的前%s项，请慢用(●⌒◡⌒●)' %x
print a_list
