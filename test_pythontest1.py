# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:35:22 2019

@author: pc caeshica
"""
import unittest
import pythontest1

class TestPythonTest1:
    def test_loadWordFromDoc(self):
        assert len(pythontest1.loadWordFromDoc())!=0,"empyfile no word found"

if __name__=='__main__':
    unittest.main()        