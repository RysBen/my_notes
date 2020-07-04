#!/bin/sh

mdir=$1
qc_dir=${mdir}/01_clean/fastqc

if [ $# -ne 2 ];then
    echo "Usage: $0 <mdir> <threads>"
    exit

if [ -d $qc_dir ];then
    echo "qc_dir has existed!"
    exit
else
    mkdir $qc_dir
fi

ls ${mdir}/01_clean/*gz| xargs /tools/fastqc -t $2 -o $qc_dir 
