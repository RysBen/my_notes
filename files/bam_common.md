import pysam
mysam=pysam.AlignmentFile('test.bam')

#get mutated reads

#stat strand bias



##########################################################################
# [1] extract reads containing a SNV
##########################################################################
```bash
samtools view -b in.bam 1:161518378-161518378 |samtools fillmd -e - $REF |grep -v "@" | \
awk -v pos="161518378" 'BEGIN{OFS=FS="\t"}; {n=split($10,a,""); if(a[pos-$4+1]!="=") print pos,pos-$4+1,a[pos-$4+1],$1,$4,$10}'
```


[1] https://www.biostars.org/p/86199/
