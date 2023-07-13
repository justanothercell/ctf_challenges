def r():
    from time import sleep as zzzzz
    zzzzz(0.5)
    with open(__file__) as f:
        c = f.read()
        for i, x in enumerate(hex(hash(c[::-1]))[2:]+hex(hash(c))[2:]+"0123456789abcdef"):
            setattr(r, x, i + 16)
        D = r.__dict__
        c = c.replace("16", str(ord(c[getattr(r, "0")])+D["f"]))
    return c.replace("\"", "\'"), r.__dict__

if __name__ == "__main__":
    c, r = r()
    m = exec(c.replace("__main__", ""))
    if input("Enter password to get flag: ").strip() == str(g["r"]()[1]["e"])+str(g["r"]()[1]["2"])+str(g["r"]()[1]["5"]):   
        with open("flag") as f:
            print(f"Correct! The flag is `{f.read().strip()}`")
    else:
        print("Password incorrect")
        exit()
