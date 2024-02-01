message = "XXX-"

if message[:2].isalpha():
    if message[3] == "-":
        if message[4:7].isdigit():
            print("Le format du message de commit est correct.")
