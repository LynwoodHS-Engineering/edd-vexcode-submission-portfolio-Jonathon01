from vex import *

brain=Brain()


limit_switch_a = Limit(brain.three_wire_port.a)
limit_switch_b = Limit(brain.three_wire_port.b)
led_g = Led(brain.three_wire_port.g)
led_h = Led(brain.three_wire_port.h)


while True:
    led_g.on();
    led_h.off();
    limit_switch_a
    limit_switch_b
    if limit_switch_a.pressing():
     if limit_switch_b.pressing():
         led_g.off()
         led_h.on()
         limit_switch_a.pressing()
