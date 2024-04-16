def on_button_pressed_a():
    global x, y
    x += 0 - 1
    if x < 0:
        x = 4
        y += 0 - 1
        if y < 0:
            y = 4
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x, y
    x += 1
    if x > 4:
        x = 0
        y += 1
        if y > 4:
            y = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

jas = 0
x = 2
y = 2

def on_every_interval():
    global jas
    for y_pom in range(5):
        for x_pom in range(5):
            jas = led.point_brightness(x_pom, y_pom)
            jas += -20
            if jas < 0:
                jas = 0
            led.plot_brightness(x_pom, y_pom, jas)
    led.plot(x, y)
loops.every_interval(100, on_every_interval)
