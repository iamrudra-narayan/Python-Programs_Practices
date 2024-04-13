with open("i\\o\\file4.txt", "r") as f:
    detect = f.read()
if "donkey" in detect: 
    with open("i\\o\\file4.txt", "w") as f:
        f.write(detect.replace("donkey", "######"))    