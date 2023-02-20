let recv_timeout = 0
radio.setGroup(1)
basic.forever(function () {
    radio.sendNumber(input.lightLevel())
    basic.pause(1000)
    recv_timeout += 1
    if (30 < recv_timeout) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
