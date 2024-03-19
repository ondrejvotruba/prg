import random
colors = {"r": "red", "g": "green", "b": "blue"}
color_codes = []
for code in colors:    
    color_codes.append(code)
    print(color_codes)
    rnd = random.randint(0, 2)
    print(colors[color_codes[rnd]])