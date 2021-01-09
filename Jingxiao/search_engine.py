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

#######################################################
# 3. BagofWord + Inverted
#######################################################
class BowInvertEngine(SearchEngineBase):
    def __init__(self):
        self.word2name={}
    def process_corpus(self,name,text):
        words=self.word_bag(text)
        for w in words:
            if w not in self.word2name: self.word2name[w]=[]
            self.word2name[w].append(name)
    def search(self,query):
        query=list(self.word_bag(query))
        #
        query_idx=[]
        for q in query: query_idx.append(0)
        #
        for q in query: 
            if q not in self.word2name:
                return []
        ##
        results=[]
        while True:
            cur_names=[]
            for i,q in enumerate(query):
                cur_idx=query_idx[i]
                cur_word2name=self.word2name[q]
                if cur_idx>=len(cur_word2name): return results   ## exit i >= length
                cur_names.append(cur_word2name[cur_idx])
            if all(n==cur_names[0] for n in cur_names):   ## files contain all query word, append i
                results.append(cur_names[0])
                query_idx=[i+1 for i in query_idx]
                continue
            min_val=min(cur_names)   ## files NOT contain all query word,  compare i+1, i
            min_val_pos=cur_names.index(min_val)
            query_idx[min_val_pos]+=1
        ##

    @staticmethod
    def word_bag(text):
            tmp=re.sub(r'([^\w]|\s+)',' ',text)
            tmp=tmp.lower()
            words=tmp.split(' ')
            #words=filter(None,words)
            return set(words)
