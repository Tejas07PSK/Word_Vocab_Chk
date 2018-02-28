'''
Created on 27-Feb-2018

@author: palashsarkar
'''

import PyPDF2
#import os
#import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


file_obj=None

def opnFile(file_marker):
    global file_obj
    file_obj=open(file_marker,'rb', 100)
    return file_obj

def closeNDelFileObject():
    global file_obj
    file_obj.close()
    del file_obj

def getPdfReaderObj(file_marker):
    pdf_rd_obj = PyPDF2.PdfFileReader(opnFile(file_marker))
    return pdf_rd_obj

def getTextFromFile():
    file_marker=input("Enter file name: ")
    cntr=1
    txt=''
    pdr=getPdfReaderObj(file_marker)
    while cntr < pdr.numPages:
        pgOb = pdr.getPage(cntr)
        cntr +=1
        txt += pgOb.extractText()
    #if txt=="":
        #txt = textract.process(fileurl, method='tesseract', language='eng')
        # ------Textract Lib can be used to extract text from handwritten pdf files ------#
    closeNDelFileObject()
    return txt.strip()
        
def getWordList():
    txt=getTextFromFile()
    word_lst = word_tokenize(txt)
    seperators = ['(',')',';',':','[',']',',','{','}','-','=','\n','.',' ']
    #nouse_words = stopwords.words('english')
    nouse_words = ['are','Abstract'] #We can customize our own low priority words 
    word_lst=filterStringList(word_lst,seperators+nouse_words)
    return word_lst
    
def filterStringList(wrd_lst,excl_lst):
    for i in range(len(wrd_lst)):
        if(i>=len(wrd_lst)):
            break
        for j in excl_lst:
            if((wrd_lst[i]).lower()==j.lower()):
                    #print("%s %s"%('hit',wrd_lst[i]))
                    del(wrd_lst[i])
                    break
            else:
                continue
            
    return wrd_lst


    
    
    