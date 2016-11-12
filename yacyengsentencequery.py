#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# vim: ts=2 sw=2 expandtab

import os
import sys
import nltk
from YaCyQuery import YaCyQuery
from config import *

# http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library

import urllib2
from urllib2 import urlopen

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

from epc.server import EPCServer

from yacyengsentencequerycommon import *


server = EPCServer(('localhost', 0))

@server.register_function   
def yacyengsentencesearchepc(keysstr) :
    return yacy_eng_sentence_search_html_write(keysstr.encode('utf_8').split())

@server.register_function   
def yacyengsentencesearchschemeworkshopepc(keysstr) :
    return yacy_eng_sentence_search_schemeworkshop_html_write(keysstr.encode('utf_8').split())

server.print_port()
server.serve_forever()

def main() :


    # html_write("mypage.html",
    #            [ [
    #                 "http://www.google.com"
    #                 ,"google 1111 kvkv aa bb av 23232 kvkvkv av hhh av "
    #                 ],[
    #                 "http://www.yahoo.com"
    #                 ,"yahoo 1111 kk aa bb av vvvv 23232 av hhh 2323222"
    #                     ]],
    #             ['23232','av']                  )

    print "starting up..."

    argvs = sys.argv  
    argc = len(argvs)

    l=argvs
    del l[0]
    print l

    fname=yacy_eng_sentence_search_html_write(l)
    #fname=yacy_eng_sentence_search_schemeworkshop_html_write(l)
    url='file://'+fname
    import webbrowser    
    webbrowser.open(url)

    

    
    #fname=yacy_eng_sentence_search_html_write(['as', 'if', 'like' , 'kernel'] )
    #print 'file://'+fname 

    # #qe=YaCyEngSentenceQuery(['as', 'if', 'like' , 'kernel'] )
    # qe=YaCyEngSentenceQuery(['as', 'if', 'like'] )
    # #qe.query.setParam('fq',"host_s:*.nips.cc")
    # #qe.query.setParam('fq',"host_s:jmlr.org host_s:papers.nips.cc host_s:www.schemeworkshop.org")
    # #qe.query.setParam('rows',"200")

    # ret=qe.request()
    # #print ret
    # #print len(ret)
  
    # for i in range(len(ret)):
    #     #print str(i) + ": "
    #     print ret[i][0]
    #     print ret[i][1]

    print "end"

if __name__ == "__main__" :
  main()
