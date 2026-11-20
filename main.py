barsik = {"type": "cat", "owner": "Jim"}
rex = {"type": "dog", "owner": "Alex"}
kesha = {"type": "parrot", "owner": "Elena"}

pets = [barsik, rex, kesha]

for pet in pets:
    print(f"{pet['owner']} is the owner of a pet - a {pet['type']}.")


