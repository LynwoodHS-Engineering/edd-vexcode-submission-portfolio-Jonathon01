#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()
optical_2 = Optical(Ports.PORT2)


wait(30, MSEC)


def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
initializeRandomSeed()


wait(200, MSEC)

print("\033[2J")

#endregion VEXcode Generated Robot Configuration
# Begin project code
# Print all Optical sensing values to the screen in an infinite loop
while True:
 
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    optical_2.set_light(LedStateType.OFF)

    if optical_2.color() == Color.GREEN:
        optical_2.set_light(LedStateType.ON)

    if optical_2.is_near_object():
        brain.screen.print("Found Object, printing information ")
        brain.screen.next_row()

        brain.screen.print("Brightness: ", optical_2.brightness())
        brain.screen.next_row()

        brain.screen.print("Hue: ", optical_2.hue())
        brain.screen.next_row()

        if optical_2.color() == Color.RED:
            brain.screen.print("Red Object Detected")
        elif optical_2.color() == Color.GREEN:
            brain.screen.print("Green Object Detected")
        elif optical_2.color() == Color.BLUE:
            brain.screen.print("Blue Object Detected")
        elif optical_2.color() == Color.YELLOW:
            brain.screen.print("Yellow Object Detected")
        elif optical_2.color() == Color.ORANGE:
            brain.screen.print("Orange Object Detected")
        elif optical_2.color() == Color.PURPLE:
            brain.screen.print("Purple Object Detected")
        elif optical_2.color() == Color.CYAN:
            brain.screen.print("Cyan Object Detected")
        else:
            brain.screen.print("Could Not Detect Object Color")
        
    else:
 
        brain.screen.print("No object found, readings would not be accurate")
   
    wait(100, MSEC)
