price_per_square = 7.61
space = float(input())
if 0.00<=space<=10000.00:
    print("The final price is:" + str((space * price_per_square) - (space * price_per_square * 0.18)) + " lv.")
    print("The discount is:" + str((space * price_per_square * 0.18)) + " lv.")
