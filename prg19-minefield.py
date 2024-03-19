import random


print("Minefield")

w = 10
h = 5
mine_cnt = 5
oper_cnt = 0
#gene with zero
field = [[0 for i in range(h)]for j in range(w)]

if mine_cnt > w * h:
    mine_cnt = 0
    print("Too many mines.")
for i in range(mine_cnt):
    while True:
        oper_cnt += 1
        rx = random.randint(0, w - 1)
        ry = random.randint(0, h - 1)
        if field[rx][ry] != "M":
            field[rx][ry] = "M"
            break
        print(oper_cnt)



for y in range(h):
    for x in range(w):
        if field[x][y] == "M":
            print("Na souradnici [{},{}] je mina.".format(x,y))

for y in range(h):
    for x in range(w):
        if field[x][y] == 0:
            neighbours = 0 
            if x > 0 and y >0 and field [x-1][y-1] == "M":
                neighbours +=1

            if y > 0 and field [x][y-1] == "M":
                neighbours +=1

            if x < w - 1 and y > 0 and field [x+1][y-1] == "M":
                neighbours +=1

            if x > 0 and field [x-1][y] == "M":
                neighbours +=1

            if x <w - 1 and field [x+1][y] == "M":
                neighbours +=1

            if x > 0 and y < h - 1 and field [x][y+1] == "M":
                neighbours +=1

            if y < h - 1 and field [x][y+1] == "M":
                neighbours +=1

            if x < w - 1 and y < h - 1 and field [x + 1][y + 1] == "M":
                neighbours +=1
            field[x][y] = neighbours
            

                   

#print
for y in range(h):
    for x in range(w):
        print(field[x][y], sep="", end="")
    print()