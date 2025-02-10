#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
optical_1 = Optical(Ports.PORT1)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
while True:
 
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    if optical_1.is_near_object():
     

        if optical_1.color() == Color.RED:
            brain.screen.print("Red Object")
            brain.screen.draw_rectangle(75, 75, 100, 100)
            brain.screen.set_fill_color(Color.RED)
            brain.screen.set_font(FontType.PROP40)
        elif optical_1.color() == Color.GREEN:
            brain.screen.print("Green Object")
            brain.screen.draw_rectangle(75, 75, 100, 100)
            brain.screen.set_fill_color(Color.GREEN)
            brain.screen.set_font(FontType.MONO60)
        elif optical_1.color() == Color.BLUE:
            brain.screen.print("Blue Object")
            brain.screen.draw_rectangle(40, 40, 100, 100)
            brain.screen.set_fill_color(Color.BLUE)
            brain.screen.set_font(FontType.MONO12)
        elif optical_1.color() == Color.YELLOW:
            brain.screen.print("Yellow Object Detected")
            brain.screen.draw_rectangle(50,65, 100, 100)
            brain.screen.set_fill_color(Color.YELLOW)
            brain.screen.set_font(FontType.PROP20)
        elif optical_1.color() == Color.CYAN:
            brain.screen.print("Cyan Object Detected")
            brain.screen.draw_rectangle(75, 75, 80, 80)
            brain.screen.set_fill_color(Color.CYAN)
            brain.screen.set_font(FontType.MONO15)
        else:
            brain.screen.clear_screen()
            brain.screen.set_fill_color(Color.BLACK)
   
    wait(100, MSEC)
