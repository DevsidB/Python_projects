# ## updates highscore in a text file: Dosent work if the text is blank
# def game():
#     return 100

# score = game()

# with open ("hiscore.txt") as f:
#     hiscore = int(f.read())

# if score > hiscore:
#     with open ("hiscore.txt", 'w') as f:
#         f.write (str(score))

##--------------------------------------------------------------------------------
## updates highscore in a text file: works even if the text is blank
def game():
    return 1000

score = game()

with open ("hiscore.txt") as f:
    hiscore = f.read()

if hiscore == '' :   ## This condition needs to be in 'if' statem only. If reversed order code will not work when text file has no value in it.
        with open ("hiscore.txt", 'w') as f:
            f.write (str(score))

elif score > int(hiscore):
    with open ("hiscore.txt", 'w') as f:
        f.write (str(score))


