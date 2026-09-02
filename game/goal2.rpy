label goal2:
    if persistent.goal2a == True:
        jump goal2a

    elif persistent.goal2b == True:
        jump goal2b

    else:
        "Level 2 is not unlocked yet!"
        return

label goal2a:
    "Level 2: Path A"

label goal2b:
    "Level 2: Path B"