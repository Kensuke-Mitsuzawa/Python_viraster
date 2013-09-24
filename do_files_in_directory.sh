#! /bin/sh

DIRPATH=$1
TARGET_DIRPATH=$2
for filepath in ${DIRPATH}* 
do
	echo $filepath
	newpath=`echo $filepath | sed "s|$DIRPATH||" `
	OUTPATH=$TARGET_DIRPATH$newpath
	echo $OUTPATH
	python for_dataset.py -m l_a -w True $filepath $OUTPATH
done

