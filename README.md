/r/Overwatch Bug Bot
==========

A spontanious Reddit bot that aims to help out
the mods of /r/Overwatch by raising awareness of
the official Blizzard support forums.  It's simple,
fast, and efficient.


### Dependencies:
  - Python 2.7+: Current commit - Python 3 | Commit dcde959e0e0309e4ba38891dae84f551d998157a - Python 2
  - quote_plus module (renamed to urllib.parse in Python 3)
  - [PRAW: The Python Reddit API Wrapper](http://praw.readthedocs.io)
  

### Instructions:
  1. Install Python 2.7+
  2. [Install PRAW](http://praw.readthedocs.io/en/latest/getting_started/installation.html)
  4. [Configure the account information](http://praw.readthedocs.io/en/latest/getting_started/authentication.html)
  3. Run redditbot.py
  
  Note: If I remember correctly, depending on the version of Python,
  quote_plus could be stored in a different parent module. So know
  you might have to change it.
  

### Ideas:
  - Remove comment if votes fall below a number
  - Add a console to interact with it in real time