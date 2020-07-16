       
#qc
def end_trim(seq,qual,threshold):
    i=0
    while ord(qual[i])-33 < threshold:
        seq[i]='N'
        qual[i]='-'
        i+=1
    return seq, qual

def windows_trim():
    i=0
    

def main():
    with open('test.fq') as f:
        while True:
            try:
                head,seq,sep,qual=f.next(),f.next(),f.next(),f.next()
            except:
                break
