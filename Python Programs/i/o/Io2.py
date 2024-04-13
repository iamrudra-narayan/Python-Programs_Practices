def game():
    return 44677

score = game()
with open("i\\o\\hiscore.txt") as f:
    hiScoreStr = f.read()
    
if hiScoreStr=='':
    with open("i\\o\\hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score :
    with open("i\\o\\hiscore.txt", "w") as f:
        f.write(str(score))