'''Talk In Day'''
#1- Program Fundamental (VAR , DAtA TYPE ,Output,input , Library,small talk memory )
#2- Condition (if , switch ,When use one )
#3- Functions 
#4- Loop (while , do-while ,for ,Use Any One)
#5- Array - dictionary - tuples

from os import strerror;

#1-create Array For Servers name
Servers_Names=[];
for i in range(0,5):
    serverName =input("Enter Server Name => ");
    Servers_Names.append(serverName);
#2- Check Array
print(Servers_Names)
#3- write In File 
stream = open("ServersName",'a+');
for serverName in Servers_Names :
    stream.write(serverName+'\n')
stream.close();
#4- ReadForm fie
stream = open("ServersName",'r+');
content = stream.readlines()
print(content)
for serverName in content:
   print(serverName)
