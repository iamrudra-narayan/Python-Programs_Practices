myDict = {
    "appreciate":"to appreciate someone",
    "justice":"to justice someone",
    "explain":"to elaborate something"
}

options = myDict.keys()
print(options)
word = input("Enter a word from the above option: ")
print("Meaning is: ",myDict.get(word))