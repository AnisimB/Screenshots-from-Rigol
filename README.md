# Screenshots from Rigol
If you need to frequently share screenshots from your Rigol oscilloscope, this script will come in handy. 

It works like this: The oscilloscope must be connected via USB. The script takes a screenshot from your Rigol oscilloscope and places it in the clipboard and immediately pastes it from the clipboard. That is, when you need to insert a screenshot into a messenger or a document, you simply press Ctrl + Shift + F12 (the combination may be different) and what is now on the oscilloscope screen will be inserted into the document.

How did you live without it before?

## OS
This script was tested by me only under Windows 10 and Windows 11. I would be glad if someone supplements it for full-fledged work elsewhere.

## Requirements
This is my configuration at the time of publication, I do not rule out that it will work on other versions, but this needs to be confirmed separately.
* Python==3.8.2
* PyVISA==1.13.0
* keyboard==0.13.5
* pywin32==303
* Pillow==9.2.0

The script was tested on Rigol 1054Z, but I'm sure it will work on many others.

## How to install
0. Install IVI Compliance Package (from ni.com)
1. Open NI Package Manager and install NI-VISA in driver section
2. Install Python
3. pip install -U pyvisa
4. pip install keyboard
5. pip install pywin32
6. pip install Pillow

## How to use
0. Connect the Rigol oscilloscope via USB. USB Test and Measurement Device (IVI) must appear in your device manager.
1. Run this script (python rigscr.py)
2. Place the cursor where you want to paste the screenshot.
3. Press Ctrl + Shift + F12.
4. Enjoy
5. To exit the script, press Ctrl + C
