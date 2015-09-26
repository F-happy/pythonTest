#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-03-26 21:35:34
# @Author  : jonnyF (fuhuixiang@jonnyf.com)
# @Link    : http://jonnyf.com


class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        res = list()
        for x in xrange(numRows):
            temp = list()
            for y in xrange(x + 1):
                if y is 0 or y is x:
                    temp.append(1)
                else:
                    temp.append(res[x-1][y-1] + res[x-1][y])
            res.append(temp)
        return res
