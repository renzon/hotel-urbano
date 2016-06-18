with open("./estados.txt", mode="w", encoding="utf-8") as f:
    f.write("MG\nSP\nRJ\nES")

with open("./estados.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
