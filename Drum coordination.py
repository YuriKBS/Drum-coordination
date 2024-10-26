# Two lists, one for the drum rudiments single stroke, double stroke and paradiddle.
rudiments = ("single stroke", "double stroke", "paradiddle")
# Think of parallel, vertical and X.
pairings = ("right hand", "left hand"),
("left hand", "right hand"),
("left foot", "right foot"),
("left hand", "left foot"),
("right hand", "right foot"),
("right hand", "left foot"),
("left hand", "right foot")
#I tried to make the pairings between single stroke, double stroke and paradiddle already written,
#other attempt I did making a list of them individually made the program repeat itself or give more than one thing to the same limb.

combinations = []

for pairing in pairings:
    for rudiment in rudiments:
        combinations.append((pairing, rudiment))

for combo in combinations:
    print(combo)
# The result should be what you can practice