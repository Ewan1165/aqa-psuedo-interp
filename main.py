from sys import argv
from time import sleep

if len(argv) < 2:
    print("Drag the file onto this exe")
    sleep(3)
    exit()

with open(argv[1],"r") as file:
    codetxt = file.read()

cmds = [
    ["USERINPUT", "input()"],
    ["ENDIF",""],
    ["IF","if"],
    ["ELSE","else:"],
    ["THEN",":"],
    ["ENDWHILE",""],
    ["=","=="],
    ["<<","="],
    ["<-","="],
    ["AND","and"],
    ["OR","or"]
]

for i in cmds:
    codetxt = codetxt.replace(i[0], i[1])

for i in codetxt.splitlines():
    if "OUTPUT" in i:
        codetxt = codetxt.replace(i,i.replace("OUTPUT ","print(") + ")")
    elif "INCREMENT" in i:
        codetxt = codetxt.replace(i,i.replace("INCREMENT ","") + "+= 1")
    elif "WHILE" in i:
        codetxt = codetxt.replace(i,i.replace("WHILE","while") + ":")

exec(codetxt)
sleep(5)