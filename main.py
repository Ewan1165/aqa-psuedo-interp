with open("test.ps","r") as file:
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
    ["<-","="]
]

for i in cmds:
    codetxt = codetxt.replace(i[0], i[1])

for i in codetxt.splitlines():
    if "OUTPUT" in i:
        codetxt = codetxt.replace(i,i.replace("OUTPUT ","print(") + ")")
    elif "WHILE" in i:
        codetxt = codetxt.replace(i,i.replace("WHILE","while") + ":")

print(codetxt)
exec(codetxt)