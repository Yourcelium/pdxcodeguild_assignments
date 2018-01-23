print("Hello! Lets talk walls.\n\n")
width = int(input("How wide is this wall?\n"))
height = int(input("How tall is this wall?\n"))
cost = int(input("How much damage is this paint?\n"))

def paint_cost(i,ii,iii):
    sqft = i * ii
    cost = sqft * iii
    print("\n\n\tYou wall will cost ${} to paint\n\n".format(cost))

paint_cost(width, height, cost)
