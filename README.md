# RPi-Guitar-FX

This repository stores all the code used to drive my Raspberry Pi-based guitar effects project. Currently, I plan to add support for external buttons to switch between effects presets in Guitarix, and I also plan to enable the volume to be adjusted using an external potentiometer.

A guide to what I have done already can be found here: [Guitar Effects using a Raspberry Pi](https://henryjburg.medium.com/guitar-effects-using-a-raspberry-pi-b24d39489a89)

This repository currently contains two items: `preset_switcher.py` and `startup.sh`. `preset_switcher.py` is a basic Python script that listens for button presses on two GPIO pins and sends two key combinations depending on which button was pressed. The key combinations sent correspond to the Guitarix shortcuts to change presets back and forth. `startup.sh` is a script designed to be run on startup that activates the JACK software before starting Guitarix.
