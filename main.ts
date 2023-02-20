radio.setGroup(1)
basic.forever(function () {
    radio.sendNumber(input.lightLevel())
    basic.pause(1000)
})
