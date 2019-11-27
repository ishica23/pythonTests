# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:35:22 2019

@author: pc caeshica
"""
import unittest
from  pythontest1 import loadWordFromDoc

class TestProc(unittest.TestCase):
    
    def test_loadWordFromDoc(self):
        assert len(loadWordFromDoc())!=0,"empyfile no word found"

if __name__=='__main__':
    unittest.main()        
