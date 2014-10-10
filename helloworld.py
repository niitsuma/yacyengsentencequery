# -*- coding: utf-8 -*-
from Pymacs import lisp
#from ustr import *

def hello():
    lisp.insert("Hello from Python!")
    #lisp.py_insert(ustring2bytes("Hello from Python!"))
    #lisp.py_insert(ustring2bytes(u"Hello from Python!"))
    

#def hello2():
#    list.setq(tmpv,["11","bb","kkkk"])

def hello2(l):
    return l[0]+"pypy123"


def hello3(l):
    return [l[0]+"12pypy123",l[1]+"bbb"]


    #hello()    
