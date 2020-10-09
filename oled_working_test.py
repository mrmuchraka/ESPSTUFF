from machine import Pin, I2C
import ssd1306
from time import sleep

# Declering OLED Address & size
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3C)



#Lets start a small and boring Test
# filling the screen with NOTHING (Black screen) using "oled.fill(0)" / executing by this command -> "oled.show()"
oled.fill(0)
oled.text("Test Me Harder", 0, 32, 1) #
oled.show()
sleep(3)

# screen cleaning sequence - Ends with Black screen
oled.fill(0)
oled.show()

# next screen
oled.text("Hmmmmm", 0, 32, 1) #
oled.show()
sleep(3)

# screen cleaning sequence - Ends with Black screen
oled.fill(0)
oled.show()

# next screen
oled.text("weird....", 0, 32, 1) #
oled.show()
sleep(3)

# screen cleaning sequence - Ends with Black screen
oled.fill(0)
oled.show()

# next screen
oled.text("cant fill it", 0, 32, 1) #
oled.show()
sleep(3)

# screen cleaning sequence - Ends with Black screen
oled.fill(0)
oled.show()


# next screen
oled.text("BORING Blyat !", 0, 32, 1) #
oled.show()
sleep(3)

# screen cleaning sequence - Ends with Black screen
oled.fill(0)
oled.show()

# next screen
oled.text("The End :)", 0, 32, 1) #
oled.show()
