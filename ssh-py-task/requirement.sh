#!/bin/bash
for i in {a..z}
do
  echo "$i">$i.log  
  echo "$i.log">>logsfile.txt 
done 

echo ("files from a to z created")
