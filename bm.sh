#!/usr/bin/env bash
file=$1
echo $file
grep 'uri' $file | cut -d ">" -f2 | cut -d "<" -f1 > bmext.tmp

#for line in uri.tmp;
#	    if [[ $line =~ [^[:digit:]] ]];
#	    then
#		echo $line;
#	    else
#		continue
#	    fi
#done

python bm.py bmext.tmp
