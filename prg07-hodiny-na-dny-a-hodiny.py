hrs = (int(input("Zadej počet hodin: ")))

days = hrs // 24
hours = hrs % 24

print("Dnů: " +str(days) + "\tHodin: " +str(hours))