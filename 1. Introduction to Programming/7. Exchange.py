CENT = 1
FIVE_CENTS = 5
TWENTY_FIVE_CENTS = 25
LOONIE = 100
TOONIE = 200

value = int(input("Enter exchange: "))

need_cents = value / CENT
need_five_cents = value / FIVE_CENTS
need_twenty_five_cents = value / TWENTY_FIVE_CENTS
need_loonies = value / LOONIE
need_toonies = value / TOONIE

print(f"You need: {need_cents} cents\nYou need: {need_five_cents} five cents\n
You need: {need_twenty_five_cents} twenty five cents\nYou need: {need_loonies} loonies\n
You need: {need_toonies} toonies\n")
