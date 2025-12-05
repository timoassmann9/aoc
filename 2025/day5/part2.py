with open("input.txt", "r") as f:
    data = f.read()

data = data.split()

fresh_ingredient_id_ranges = [id_range for id_range in data if "-" in id_range]

# es müssen nun alle fresh ids gefunden werden. Problem: Alle in eine Liste zu packen ist viel zu groß. JA IST ES