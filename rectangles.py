print("""
I am going to ask for the length and width of 2 separate rectangles
and then will tell you which one has more area or if they have
equal area.
""")

l1 = float(input("length 1: "))
w1 = float(input("width 1: "))

l2 = float(input("length 2: "))
w2 = float(input("width 2: "))

area1 = l1 * w1
area2 = l2 * w2

if area1 > area2:
    print("The area of the first rectangle is larger")
elif area1 < area2:
    print("The area of the second rectangle is larger")
else:
    print("Both rectangles have equal area")
