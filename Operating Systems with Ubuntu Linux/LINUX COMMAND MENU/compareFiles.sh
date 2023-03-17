#!/bin/bash
# Remember that you should always start writing the command that appears there on the first line.

cd D1
echo "Showing list of files in D1:"
ls -l
echo "The most recent file in D1 is:"
find . -mtime -1 | sort -n | tail -1
cd ..
cd D2
echo "Showing list of files in D2:"
ls -l
echo "The oldest file in D2 is:"
find . -mtime -1 | sort -r | tail -2
