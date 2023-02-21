radio.setGroup(1)
radio.setTransmitPower(7)
basic.forever(function () {
    radio.sendNumber(input.lightLevel())
    basic.pause(1000)
})
