# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Ada")
define k = Character("Ms. Katherine")
default goal1a = False
default goal1b = False


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

    hide eileen happy
    # scene title screen
    # scene teacher room

    "Welcome to 17@16"
    
    show eileen happy

    a "Time to get to work, then! Let's ask Ms. Katherine for help."

    k "Hey Ada! How's it going?"

    a "I mean, I just found out I needed 170 volunteer hours to graduate, so..."

    k "Don't worry! At Grace Hopper Technical High School, we do community service requirements based on the following framework:"

    k "This is the United Nation's 17 Sustainable Developmental Goals. We recommend students work ten hours per goal."

    # Show goal chart, highlight each one, and explain

    a "Wow! But Yonkers is kind of in the middle of nowhere, no?"

    k "Don't worry! Here's a map of all the opportunities I did when I was a young lad."

    k "Not sure if they still exist, but it's worth a try!"

    # Gained new item

    a "Time to work on Goal 1: No Poverty!"

    k "Reflection: What does poverty look like to you?"
    # Option to skip reflection

    a "Poverty looks like homelessness and not having enough money to have basic needs in life, like food or shelter."

    k "That's super close! According to the United Nations, poverty is defined as _"

    a "What can I do to help? I'm just 16..."

    k "You can filter the opportunities on the map by SDG goal!"

    k "It looks like you have the option of either the Mount Vernon Community Garden or B"

    k "I volunteered at the garden as a teenager, and was pretty cool! But it was a little far away."

    k "But B is more local, in Yonkers. I've never tried it. I only heard about it from my friend... but I trust her!"

    k "Which one will you choose?"
    #Pick between two options

    menu:
        "Do the community garden in Mount Vernon":
            a "I'll try the Mount Vernon Community Garden."
            k "Great choice!"
            $ goal1a = True
            jump goal1a
        "Do B in Yonkers":
            a "I'll try B!"
            k "Great choice!"
            $ goal1b = True
            jump goal1b
    # This ends the game.
    
    a "I'm so excited!"

    return
