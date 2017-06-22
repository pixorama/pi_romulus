# Pi Romulus

[![Code Health](https://landscape.io/github/ArthurMoore85/pi_romulus/master/landscape.svg?style=flat)](https://landscape.io/github/ArthurMoore85/pi_romulus/master)
[![Build Status](https://travis-ci.org/ArthurMoore85/pi_romulus.svg?branch=master)](https://travis-ci.org/ArthurMoore85/pi_romulus)

Retropie ROM downloader

Based on Romulus, the Linux Retropie ROM manager, Pi Romulus is intended to fill a gaping hole
in the Retropie functionality.
It allows you to search for games for the Retropie that you already own and then downloads it
directly to your Retropie installation, no further work required.
What makes Pi Romulus so attractive, is that there is no need for any other computer system.
You dont need to switch on your laptop to download and transfer the games. Just hook up a
keyboard to your Retropie, or ssh into the Pi, search for the game, select and play.

Features:
* Searching ROMs (uses Emuparadise)
* Automatic detection of required emulator
* Automatic ROM extraction, if ROM arrives in an archive
* Places ROMs in the correct folder for direct playability
* Pi Romulus entry in EmulationStation (not tested)

Technical Details
-----------------
Romulus is written using Python 2.7.
For it's GUI framework it makes use of the excellent npyscreen library.

Installation
------------
Step 1. Install requirements: `sudo apt-get install python-pip libarchive-dev`

To install using PIP: `sudo pip install pi-romulus`. 
After this, you should be able to start Pi Retropie with the command `pi-romulus`.

To install from source:

Clone this app into a folder on your Retropie.
After this, install all the requirements with `pip install -r requirements.txt`.

Once completed, run `python romulus.py` to start the app.
Note, if this is the first time you run Pi Romulus, it will create a shortcut into your EmulationStation menu (not tested)

Developers
----------
All code is licensed under GNU Public License 2 (GPLv2). This license allows you to copy, edit, and redistribute without restriction, as long as it retains the free GPLv2 license.

All help is appreciated, whether filing bug reports, squashing bugs, requesting features or anything else, simply clone this repo, and if you have improved it somehow, make a pull request.

Reporting bugs
--------------
If you have discovered a bug, please report it using the issues tab at the top of the project page.
Before reporting a bug, check if the bug you encounter hasn't already been raised.
You can also reach out to me directly.

Authors
-------
Arthur Moore <arthur.moore85@gmail.com>
