#AIRPLANE SEAT COST CALCULATOR

def seat_cost(row, seat):

    seat = str.upper(seat)
    if len(seat) != 1:
        return "invalid seat"
    if row < 1 or row > 25:
        return "invalid seat"
    if seat < "A" or seat > "F":
        return "invalid seat"

    # 1-5 : 500
    # 10-11: 200
    # every other: 150
    # B and E: -50

    if row <= 5:
        cost = 500
    elif row == 10 or row == 11:
        cost = 200
    else:
        cost = 150

    if seat == "B" or seat == "E":
        cost -= 50

    return cost
    
