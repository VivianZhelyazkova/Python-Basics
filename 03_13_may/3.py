animal = input()
mammal = "dog"
reptiles =["crocodile", "tortoise", "snake"]

if animal == mammal:
    print("mammal")
elif animal in reptiles:
    print("reptile")
else:
    print("unknown")
    