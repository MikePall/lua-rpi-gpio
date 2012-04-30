local gpio = require("rpi.gpio")

for i=1,10 do
  print("GPIO 6:", gpio.pin[6])
  gpio.pin[0] = 1
  gpio.msleep(100)
  gpio.pin[0] = 0
  gpio.msleep(100)
end

