#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install names')


# In[4]:


pip install gTTS


# In[5]:


pip install temp


# In[1]:


import names
from gtts import gTTS
import tempfile
import os


# In[2]:


def spellApco(word):
    alphabet = {
        'A': "Apple",
        'B': "Boy",
        'C': "Cat",
        'D': "Dog",
        'E': "Elephant",
        'F': "Frog",
        'G': "Girrafe",
        'H': "Hen",
        'I': "India",
        'J': "John",
        'K': "King",
        'L': "London",
        'M': "Mother",
        'N': "Nest",
        'O': "Ocean",
        'P': "Parrot",
        'Q': "Queen",
        'R': "Rat",
        'S': "Shark",
        'T': "Tom",
        'U': "Umbrella",
        'V': "Van",
        'W': "Wool",
        'X': "X-Ray",
        'Y': "Young",
        'Z': "Zebra",
    }

    # Speak the word at the beginning
    spelling = word + ". "

    # Spell out each letter of the word
    for letter in word:
        if letter == " ":
            spelling += "... "
        else:
            spelling += letter.upper() + " for " + alphabet.get(letter.upper(), "Sorry! I have no Idea about this one.") + ". "

    # Say the word again at the end
    spelling += word + "."

    return spelling


if __name__ == '__main__':
    # Get a random name
    print("Selecting random name...")
    name = names.get_full_name()

    # Spell out name
    spelling = spellApco(name)

    # Get MP3 of phrase
    print("Converting text to speech...")
    tts = gTTS(text=spelling)

    # Write MP3 to a temporary file
    f = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tts.write_to_fp(f)
    f.close()

    # Play MP3 in temporary file
    print("Speaking...")
    response = "R"
    while response.upper() == "R":
        os.system("start " + f.name)

        # Ask user to repeat or continue
        response = input("(R)epeat or (C)ontinue? ")

    # Close and delete temporary file
    os.remove(f.name)

    # Check is name is correct
    response = input("What was the name? ")
    if response.upper() == name.upper():
        print("Correct! Well done!")
    else:
        print("The correct answer was '%s'." % name)


# In[ ]:




