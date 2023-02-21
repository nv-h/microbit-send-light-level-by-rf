radio.set_group(1)
radio.set_transmit_power(7)

def on_forever():
    radio.send_number(input.light_level())
    basic.pause(1000)
basic.forever(on_forever)
