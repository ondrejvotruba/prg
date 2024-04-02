vklad = 1000
roky = 10
urok = 0.05

hodnota = vklad
for rok in range(roky):
    hodnota *= (1 + urok)

hodnota = round(hodnota * 100) / 100  # Zaokrouhlení bez desetinných cisel

print(f"Hodnota vašeho vkladu po {roky} letech při {urok * 100:.0f}% úrokové sazbě je {hodnota:.0f} Kč.")
