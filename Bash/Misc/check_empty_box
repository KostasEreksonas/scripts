#!/bin/sh

# One liner command to check wether user input is empty or not. While it is empty, prompt the user to input something

name=; while [ -z $name ]; do name=$(dialog --stdout --title "User Creation" --inputbox "User Name:" 0 0); if [ -z $name ]; then dialog --title "User Creation" --msgbox "User name cannot be empty. Try again" 0 0; else dialog --title "User Creation" --msgbox "User name is $name" 0 0; fi; done
