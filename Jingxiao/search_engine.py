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
