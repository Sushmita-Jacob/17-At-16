label goal1:
    if persistent.goal1a == True:
        jump goal1a

    elif persistent.goal1b == True:
        jump goal1b
    
    else:
        "Level 1 is not unlocked yet!"
        return


label goal1a:
    scene bg room onlayer master
    with None

    show eileen happy:
        xalign 0.5
        yalign 1.0

    with dissolve
    "Level 1: Path A"
    a "Goal 1: No Poverty! Let's see what I can do."
    jump endgoal1

label goal1b:
    scene bg room
    show eileen happy onlayer master
    "Level 1: Path B"
    a "Wow, I can't wait to check out this part of Yonkers!"
    jump endgoal1

label endgoal1:
    a "You've reached the end of Goal 1"