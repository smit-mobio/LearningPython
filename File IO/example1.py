with open("twinkle.txt") as f:
    g = f.read()
    if "twinkle" in g:
        print("Twinkle is present")
    else:
        print("Twinkle is not present")