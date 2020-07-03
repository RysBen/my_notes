#!/bin/bash

adapter=/path/TruSeq3-PE-2.fa
cpu=10

while getopts o:a:c: opt
do
  case $opt in 
    o)
    $optO=$OPTARG
    ;;
    a)
    adapter=$OPTARG
    ;;
    c)
    cpu=$OPTARG
    ;;
    '?')
    echo "Usage: $0 fq1 fq2 sample"
    esac
done

shift $((OPTINT-1))
if [ $# lt 3 ];then
  echo "Usage: $0 [-cpu cpu] [-o ~ ] fq1 fq2 sample" #???
  exit 1
fi

fq1=$1
fq2=$2
sample=$3

java -jar $TRIMMOMATIC_DIR/trimmomatic-0.33.jar \
PE -threads $cpu -trimlog $optO/trim.log \
$R1 $R2 \
$sample_clean_R1.fq.gz \
$sample_unpaired_R1.fq.gz \
$sample_clean_R2.fq.gz \
$sample_unpaired_R2.fq.gz \
ILLUMINACLIP:$adapter:2:30:9:1:TRUE \
LEADING:3 \
TRAILING:3 \
SLIDINGWINDOW:4:15 \
MINLEN:36
