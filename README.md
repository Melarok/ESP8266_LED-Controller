# How to use this
## Requirements
- A ESP8266 and a USB-to-serial converter if not included in the package
- esptool and rshell (both installable via pip)

## Procedure
- Flash MicroPython on the ESP8266
    - Follow the instructions [here](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware)
- Use rshell to connect and copy the main.py to it via USB

```shell
        $ rshell
        $ connect serial /dev/ttyUSB0 115200
        $ cp /path/to/main.py /pyboard/
```

- The ESP8266 is now ready and will start the script at power-on

## How to modify this
- Edit the main.py and adjust the time.sleep(#) statements according to your needs
- If you need more complex cycles, uncomment the lines at the end of the while loop, or add more as needed
- Use rshell as described above to copy the modified main.py to the ESP8266
