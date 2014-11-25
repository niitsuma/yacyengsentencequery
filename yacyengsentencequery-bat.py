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


# def convert_pdf_to_txt(url):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     codec = 'utf-8'
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

#     scrape = urlopen(url).read()
#     fp = StringIO(scrape)

#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     password = ""
#     maxpages = 0
#     caching = True
#     pagenos=set()
#     for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
#         interpreter.process_page(page)

#     fp.close()
#     device.close()
#     textstr = retstr.getvalue()
#     retstr.close()
#     return textstr

# def min_abs_sub_list_list(ll) :
#     n=len(ll)
#     r=0
#     for i1 in range(n):
#         for i2 in range(n):
#             if i1 != i2 :
#                 l1=ll[i1]
#                 l2=ll[i2]
#                 r += min([abs(e1-e2) for e1 in l1 for e2 in l2] )
#     return r

# import re
# def keys_in_str_distance(str,keys):
#     ll=[[m.start() for m in re.compile(k).finditer(str)] for k in keys]
#     return min_abs_sub_list_list(ll)/2


# class YaCyEngSentenceQuery:
#     def __init__(self, word_list):
#         self.word_list=word_list
#         self.word_list_lower=[k.lower() for k in word_list]
#         self.querystr=' AND '.join(self.word_list)
#         self.query=YaCyQuery(self.querystr)
#         self.fetch_timeout=12
#         self.unique_result=[]
#         self.sent_detector=nltk.data.load('tokenizers/punkt/english.pickle')
#         self.n_need_sentences=0
#         self.url_stack=[]
        
        
#     def rowtext2local_result(self,raw,url) :
#         sentences=self.sent_detector.tokenize(raw)
#         local_ret = [[url,t] for t in sentences if all(w.lower() in t.lower() for w in self.word_list) ]
#         return local_ret
    
#     def result2unique_result(self,local_ret) :
#         [self.unique_result.append(item) for item in local_ret if item not in self.unique_result]
#         return self.unique_result

#     def rowtext2result(self,raw,url):
#         return self.result2unique_result(self.rowtext2local_result(raw,url))
    
#     def request(self):
#         #self.query.setParam('rows',"20")
#         self.numresults = self.query.request()
#         #print self.numresults
#         for i in range(self.numresults):
#             #print i
#             result = self.query.getResult(i)
#             #print result  
#             #url = result['link']
#             url = result['sku'].encode('utf_8')
#             #print url
#             #description = result['description']
#             description = result['text_t'].encode('utf_8')
#             #print description
#             if len(description) > 0 :
#                 raw=description
#                 local_ret=self.rowtext2local_result(raw,url)
#                 if len( local_ret) > 0 :
#                     self.unique_result=self.result2unique_result(local_ret)
#             if len(local_ret) == 0 or len(description) ==0 :
#                 self.url_stack.append(url)
#             #print [len(self.unique_result),len(self.url_stack)]
#         #
#         return self.unique_result
    
#         if len(self.unique_result) <  self.n_need_sentences :
#             for url in self.url_stack:
#                 fileName, fileExtension = os.path.splitext(url)
#                 #fileExtension = result['url_file_ext_s'].encode('utf_8')
#                 if fileExtension == '.pdf' :
#                     #print str(i) + ": " + result['link']
#                     raw=convert_pdf_to_txt(url)
#                     self.unique_result=self.rowtext2result(raw,url)
#                 #print url
#                 try:
#                     html = urllib2.urlopen(url,timeout=self.fetch_timeout).read()    
#                     raw = nltk.clean_html(html)
#                     self.unique_result=self.rowtext2result(raw,url) 
#                 except urllib2.URLError, e:
#                     print "Url Error: %r" % e
#                 except Exception,e:
#                     print "Fallo de tipo ",e
#                 else:
#                     1+1
#                         #print url
#                         #print "all ok!"
#                         #                except urllib2.URLError, e:
#                         #                    raise MyException("There was an error: %r" % e)
#                 if len(self.unique_result) >=  self.n_need_sentences :
#                     break
#         if len(self.word_list) > 1 :
#             self.unique_result.sort(cmp=lambda x,y: cmp(keys_in_str_distance(x[1].lower(),self.word_list_lower),keys_in_str_distance(y[1].lower(),self.word_list_lower)))

#         return self.unique_result


# ##    http://stackoverflow.com/questions/16523939/how-to-write-and-save-html-file-in-python
# def html_write(fname,l,keys) :
#     with open(fname, 'w') as myFile:
#         myFile.write('<html>')
#         myFile.write('<body>')
#         myFile.write('<ul>')

#         for ut in l:
#             myFile.write('<li>')
#             s=ut[1]
#             for k in keys:
#                 s=s.replace(' '+k,' <strong><font color="#ff0000">'+k+'</font></strong>')
#             myFile.write('<a href="'+ ut[0]+ '">'+s+'</a>')
#             myFile.write('</li>')

#         myFile.write('</ul>')
#         myFile.write('</body>')
#         myFile.write('</html>')


# def yacy_eng_sentence_search_html_write(keys) :
#     fname= OUTPUT_DIR + 'yacy-eng-sentence-search-'+'_'.join(keys)+'.html'

#     print keys
#     print fname
#     qe=YaCyEngSentenceQuery(keys)
#     #qe.query.setParam('fq',"host_s:*.nips.cc")
#     qe.query.setParam('fq',"host_s:jmlr.org host_s:papers.nips.cc host_s:www.schemeworkshop.org")
#     qe.query.setParam('rows',"1000")

#     ret=qe.request()
#     html_write(fname,ret,keys)
#     return fname

# def yacy_eng_sentence_search_schemeworkshop_html_write(keys) :
#     fname= OUTPUT_DIR + 'yacy-schemeworkshop-sentence-search-'+'_'.join(keys)+'.html'

#     print keys
#     print fname
#     qe=YaCyEngSentenceQuery(keys)
#     #qe.query.setParam('fq',"host_s:*.nips.cc")
#     qe.query.setParam('fq',"host_s:www.schemeworkshop.org")
#     qe.query.setParam('rows',"1000")

#     ret=qe.request()
#     html_write(fname,ret,keys)
#     return fname


#server = EPCServer(('localhost', 0))

#@server.register_function   
def yacyengsentencesearchepc(keysstr) :
    return yacy_eng_sentence_search_html_write(keysstr.encode('utf_8').split())

def yacyengsentencesearchschemeworkshopepc(keysstr) :
    return yacy_eng_sentence_search_schemeworkshop_html_write(keysstr.encode('utf_8').split())

#server.print_port()
#server.serve_forever()

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
