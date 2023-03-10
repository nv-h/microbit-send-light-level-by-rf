def on_received_number(receivedNumber):
    global recv_timeout
    radio.send_number(receivedNumber)
    recv_timeout = 0
    if 192 < receivedNumber:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    else:
        if 128 < receivedNumber:
            basic.show_leds("""
                . . . . .
                                . # # # .
                                . # # # .
                                . # # # .
                                . . . . .
            """)
        else:
            if 64 < receivedNumber:
                basic.show_leds("""
                    . . . . .
                                        . . . . .
                                        . . # . .
                                        . . . . .
                                        . . . . .
                """)
            else:
                basic.show_leds("""
                    . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
radio.on_received_number(on_received_number)

recv_timeout = 0
radio.set_group(1)
radio.set_transmit_power(7)

def on_forever():
    global recv_timeout
    basic.pause(1000)
    recv_timeout += 1
    if 30 < recv_timeout:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
basic.forever(on_forever)
