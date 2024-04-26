
def apendFile(fileName, text):
    failas = open(fileName,"a",encoding="utf8")
    print(failas.write(text + '\n'))
    failas.close()

def readFile(fileName):
    failas = open(fileName,"r",encoding="utf8")
    print(failas.readlines())
    failas.close()

def formatName(name):
    res = ""
    for part in name.split(" "):
        res += str(part[0]).upper() + str(part[1:]).lower() + " "
    return res[:-1]