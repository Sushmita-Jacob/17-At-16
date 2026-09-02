label goal1:
    if goal1a == True:
        jump goal1a

    elif goal1b == True:
        jump goal1b
    
    else:
        "Level 1 error"
        return


label goal1a:
    a "Level 1"
    a "Goal 1: No Poverty! Let's see what I can do."

    jump level_menu

label goal1b:
    a "level 1"
    a "Wow, I can't wait to check out this part of Yonkers!"

    jump level_menu