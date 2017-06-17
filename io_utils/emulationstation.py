# -*- coding: utf-8 -*-
"""
.. module:: .emulationstation.py
    :synopsis: EmulationStation compatibility.

.. moduleauthor:: Arthur Moore <arthur.moore85@gmail.com>
.. creation date:: 17-06-2017
.. licence:: 
"""
import os
import stat

__author__ = "arthur"

EMU_LOC = '/home/pi/.emulationstation'


def create_menu_item(loc):
    """
    Creates an EmulationStation Entry
    :param loc: Root location of project.
    """
    menu_entry = """    <system>
            <fullname>Pi Romulus</fullname>
            <name>pi_romulus</name>
            <path>{0}</path>
            <extension>.sh .SH</extension>
            <command>%ROM%</command>
            <platfom>pi_romulus</platform>
            <theme>esconfig</theme>
        </system>
    </systemList>
    """.format(loc)
    emu_file = os.path.join(EMU_LOC, 'es_systems.cfg')
    f = open(emu_file, 'r+')
    f.seek(0, os.SEEK_END)
    pos = f.tell() - 1
    while pos > 0 and f.read(1) != "\n":
        pos -= 1
        f.seek(pos, os.SEEK_SET)

    if pos > 0:
        f.seek(pos, os.SEEK_SET)
        f.truncate()
    f.write(menu_entry)
    f.close()


def create_bash(loc):
    """
    Creates bash file for Pi Romulus.
    :param loc: Root location of project
    """
    bash_text = """#!/bin/bash
    python romulus.py"""
    sh_file = os.path.join(loc, 'pi_romulus.sh')
    with open(sh_file, 'w') as sh:
        sh.write(bash_text)
    st = os.stat(sh_file)
    os.chmod(sh_file, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
