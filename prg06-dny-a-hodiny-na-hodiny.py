days, hours = (int(x) for x in input("Zadej dny a hodiny oddělené mezerou: ").split())
final_cnt = 0
if days > 0:
    final_cnt += (((days*24)+hours))
else:
    final_cnt += hours
print(final_cnt)
