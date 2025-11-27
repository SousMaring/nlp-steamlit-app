import re
def sudification(txt:str)-> str:
    listwords = txt.split()
    processedlist = []
    for word in listwords:
        if re.match(r".*[aeiou]n$", word):
            processedlist.append(word + "g")
        else:
            processedlist.append(word)
    processedstring = ' '.join(processedlist)
    return processedstring