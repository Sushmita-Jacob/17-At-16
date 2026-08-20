# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Ada")
define k = Character("Ms. Katherine")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    a "English, check. History, check. PE, check, thankfully..."

    a "I did all my classes, paid all my grad dues, and-"

    a "Wait..."

    a "Community service is a graduation requirement?!"

    # hide eileen happy
    # scene title screen
    # scene teacher room
    # show eileen happy

    a "Time to get to work, then! Let's ask Ms. Katherine for help."

    k "Hey Ada! How's it going?"

    a "I mean, I just found out I needed 170 volunteer hours to graduate, so..."

    k "Don't worry! At Grace Hopper Technical High School, we do community service requirements based on the following framework:"

    k "This is the United Nation's 17 Sustainable Developmental Goals. We recommend students work ten hours per goal."

    # Show goal chart, highlight each one, and explain

    a "Wow! But Yonkers is kind of in the middle of nowhere..."

    k "Don't worry! Here's a map of all the opportunities I did when I was a young lad."

    k "Not sure if they still exist, but it's worth a try!"

    # Gained new item



    # This ends the game.

    return
