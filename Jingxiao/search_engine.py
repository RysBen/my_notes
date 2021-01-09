#######################################################
# search engine: scrawler, index, search, ui
#######################################################
class SearchEngineBase():
    def __init__(self):
        pass
    def add_corpus(self,fn):
        with open(fn) as fi:
            text=fi.read()
        self.process_corpus(fn,text)   ## 2 paras
    def process_corpus(self,fn,text):   #index
        raise Exception("process not completion")
    def search():   #search
        raise Exception("seach not completion")

def main(se):   #ui
    for i in ["1.txt","2.txt","3.txt"]:
        se.add_corpus(i)
    while True:
        query=input("Input a word you want search:")
        results=se.search(query)
        print("found {} results".format(len(results)))

#######################################################
# 1. SimpleEngine
#######################################################
class SimpleSearch(SearchEngineBase):
    def __init__(self):
        self.__name2text={}
    def process_corpus(self,name,text):
        self.__name2text[name]=text
    def search(self,query):
        result=[]
        for k,v in self.__name2text.items():
            if query in v:
                result.append(k)
        return result

#######################################################
# 2. BagofWord
#######################################################
import re

class BOWengine(SimpleSearch):
    def __init__(self):
        self.__name2text={}
    def process_corpus(self,name,text):
        #self.__name2text[name]=word_bag(text)   ## false
        self.__name2text[name]=self.word_bag(text)
    def search(self,query):
        results=[]
        #query=word_bag(query)   ##
        query=self.word_bag(query)
        for k,v in self.__name2text.items():
            #if word_match(query,v):
            if self.word_match(query,v):
                results.append(k)
        return results
    
    @staticmethod
    def word_bag(text):
            tmp=re.sub(r'([^\w]|\s+)',' ',text)
            tmp=tmp.lower()
            words=tmp.split(' ')
            #words=filter(None,words)
            return set(words)
    @staticmethod
    def word_match(query,bow):
        results=[]
        for q in query:
            if q in bow:
                return True
            return False

#
