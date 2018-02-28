'''
Created on 25-Feb-2018

@author: palashsarkar
'''
from datahandling.FileOps import getWordList as gwl
from datahandling.Compare import compareLists as cmplsts

lsttochk = gwl()
wrtlst = gwl()

print("%s \n %s \n"%(lsttochk,wrtlst))
print("Vocabulary Similarity is %.2f %%"%(cmplsts(lsttochk, wrtlst)))

