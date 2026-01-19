from machine import Pin, I2C, time_pulse_us
import time

# ----------------------------
# PINS
# ----------------------------
TRIG_PIN = 4
ECHO_PIN = 16
BUTTON_PIN = 13
LED_PIN = 2
BUZZER_PIN = 27

# LCD I2C pins: SDA=21, SCL=22
I2C_ADDR = 0x27   # keep this unless your scan shows different

# ----------------------------
# SETUP IO
# ----------------------------
trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
led = Pin(LED_PIN, Pin.OUT)
buzzer = Pin(BUZZER_PIN, Pin.OUT)
led.value(0)
buzzer.value(0)

# ----------------------------
# LCD (PCF8574) DRIVER
# ----------------------------
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

# PCF8574 -> LCD pin mapping (common for 0x27 I2C backpacks)
# P0 RS, P1 RW, P2 E, P3 Backlight, P4 D4, P5 D5, P6 D6, P7 D7
RS = 0x01
RW = 0x02
EN = 0x04
BL = 0x08  # backlight

def _write_pcf(val):
    i2c.writeto(I2C_ADDR, bytes([val]))

def _pulse_enable(data):
    _write_pcf(data | EN)
    time.sleep_us(2)
    _write_pcf(data & ~EN)
    time.sleep_us(50)

def _write4bits(data):
    _write_pcf(data | BL)
    _pulse_enable(data | BL)

def _send(value, mode):
    # mode: RS=0 command, RS=1 data
    high = (value & 0xF0)
    low  = ((value << 4) & 0xF0)

    _write4bits(high | mode)
    _write4bits(low  | mode)

def lcd_cmd(cmd):
    _send(cmd, 0)

def lcd_data(ch):
    _send(ch, RS)

def lcd_init():
    time.sleep_ms(50)
    # init in 4-bit mode
    _write4bits(0x30)
    time.sleep_ms(5)
    _write4bits(0x30)
    time.sleep_us(150)
    _write4bits(0x30)
    _write4bits(0x20)

    lcd_cmd(0x28)  # 4-bit, 2 line, 5x8
    lcd_cmd(0x0C)  # display on, cursor off
    lcd_cmd(0x06)  # entry mode
    lcd_cmd(0x01)  # clear
    time.sleep_ms(2)

def lcd_clear():
    lcd_cmd(0x01)
    time.sleep_ms(2)

def lcd_goto(row, col):
    # row 0 -> 0x80, row 1 -> 0xC0
    addr = 0x80 + col if row == 0 else 0xC0 + col
    lcd_cmd(addr)

def lcd_print_line(row, text):
    lcd_goto(row, 0)
    s = text[:16]
    s = s + (" " * (16 - len(s)))  # pad to clear old chars
    for c in s:
        lcd_data(ord(c))

# Initialize LCD
try:
    lcd_init()
except OSError as e:
    print("LCD I2C error:", e)
    print("Run I2C scan to confirm address.")
    raise

lcd_print_line(0, "Warehouse Ready")
lcd_print_line(1, "")
time.sleep(1.5)

# ----------------------------
# HELPERS
# ----------------------------
def beep(ms=120):
    buzzer.value(1)
    time.sleep_ms(ms)
    buzzer.value(0)

def read_distance_cm():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    dur = time_pulse_us(echo, 1, 30000)
    if dur < 0:
        return 999.0
    return (dur * 0.0343) / 2.0

# ----------------------------
# MAIN LOOP
# ----------------------------
OCCUPIED_THRESHOLD = 12.0
last_btn = 1
last_state = None  # None/True/False

while True:
    # Button press -> scan detected
    btn = button.value()
    if btn == 0 and last_btn == 1:
        lcd_print_line(0, "SCAN DETECTED")
        lcd_print_line(1, "")
        beep(120)
        time.sleep(1.0)
        last_state = None  # force refresh after scan
    last_btn = btn

    # Ultrasonic -> shelf state
    dist = read_distance_cm()
    occupied = (dist < OCCUPIED_THRESHOLD)

    # update LCD only if state changed (prevents flicker)
    if last_state is None or occupied != last_state:
        if occupied:
            led.value(1)
            lcd_print_line(0, "Shelf: OCCUPIED")
            lcd_print_line(1, "LED: ON")
        else:
            led.value(0)
            lcd_print_line(0, "Shelf: EMPTY")
            lcd_print_line(1, "LED: OFF")
        last_state = occupied

    time.sleep(0.2)
