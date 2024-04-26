import functions as fun

fun.apendFile("naujasFailas.txt", "ožėlis mažasis")
fun.apendFile("naujasFailas.txt", "ožėlis mekena")

fun.readFile("naujasFailas.txt")

print(fun.formatName("naglis jonas"))
print(fun.formatName("Naglis jonas"))
print(fun.formatName("nAGLIS jONAS"))

text = "labas rytas grazus oras"
print(text)
print(text.split("s"))
for txt in text.split("s"):
    if txt != "":
        print("|" + txt + "|")


