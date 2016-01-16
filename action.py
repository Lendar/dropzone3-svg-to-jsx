# Dropzone Action Info
# Name: svg-jsx
# Description: svgo, svg-to-jsx
# Handles: Files
# Creator: Lendar
# URL: https://github.com/Lendar/dropzone3-svg-to-jsx
# Events: Clicked, Dragged
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: Yes
# Version: 1.0
# MinDropzoneVersion: 3.5

import time

def dragged():
    # Welcome to the Dropzone 3 API! It helps to know a little Python before playing in here.
    # If you haven't coded in Python before, there's an excellent introduction at http://www.codecademy.com/en/tracks/python

    # Each meta option at the top of this file is described in detail in the Dropzone API docs at https://github.com/aptonic/dropzone3-actions/blob/master/README.md#dropzone-3-api
    # You can edit these meta options as required to fit your action.
    # You can force a reload of the meta data by clicking the Dropzone status item and pressing Cmd+R

    # This is a Python method that gets called when a user drags items onto your action.
    # You can access the received items using the items global variable e.g.
    print(items)
    # The above line will list the dropped items in the debug console. You can access this console from the Dropzone settings menu
    # or by pressing Command+Shift+D after clicking the Dropzone status item
    # Printing things to the debug console with print is a good way to debug your script.
    # Printed output will be shown in red in the console

    # You mostly issue commands to Dropzone to do things like update the status - for example the line below tells Dropzone to show
    # the text "Starting some task" and show a progress bar in the grid. If you drag a file onto this action now you'll see what I mean
    # All the possible dz methods are described fully in the API docs (linked up above)
    dz.begin("Starting some task...")

    # Below line switches the progress display to determinate mode so we can show progress
    dz.determinate(True)

    # Below lines tell Dropzone to update the progress bar display
    dz.percent(10)
    time.sleep(1)
    dz.percent(50)
    time.sleep(1)
    dz.percent(100)

    # The below line tells Dropzone to end with a notification center notification with the text "Task Complete"
    dz.finish("Task Complete")

    # You should always call dz.url or dz.text last in your script. The below dz.text line places text on the clipboard.
    # If you don't want to place anything on the clipboard you should still call dz.url(false)
    dz.text("Here's some output which will be placed on the clipboard")

def clicked():
    # This method gets called when a user clicks on your action
    dz.finish("You clicked me!")
    dz.url(False)
