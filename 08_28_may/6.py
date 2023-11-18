cake_width = int(input())
cake_length = int(input())
cake_surface = cake_length * cake_width
piece = 1
command = input()
total_pieces = 0

while command != "STOP":
    current_pieces = int(command)
    total_pieces += current_pieces
    if total_pieces > cake_surface:
        print(f"No more cake left! You need {total_pieces - cake_surface} pieces more.")
        break
    command = input()
else:
    print(f"{cake_surface - total_pieces} pieces are left.")