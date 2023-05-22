import sys

class allFunc():
    def lowerChar(e):
        return e.lower()

    def countChar(e):
        return len(e) - e.count(' ')

    def replaceWhite(e):
        return e.replace("  ", "____")

    def checkFreq(e):
        freq = {}
        for c in set(e):
            freq[c] = e.count(c)
        return freq


source = sys.argv[1]
print("Source file:", source)

with open(source, 'r') as file:
    contents = file.read()

lowCont = allFunc.lowerChar(contents)
tabwhite = allFunc.replaceWhite(lowCont)    

a="-----------------------------------------------------------------------------------------"
print("Statict text:\n", contents, "\n",a)
print("Sanitized text:\n", tabwhite)
print("Counting each of alphabet :", allFunc.checkFreq(tabwhite))

