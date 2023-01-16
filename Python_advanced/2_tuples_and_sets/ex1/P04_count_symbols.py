words = input()

letter_counts = {ch:words.count(ch) for ch in words}

for k,v in sorted(letter_counts.items()):
    print(f"{k}: {v} time/s")