price_skumria = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())

price_palamud = price_skumria + (price_skumria * 0.6)
sum_palamud = kg_palamud * price_palamud

price_safrid = price_caca + (price_caca * 0.8)
sum_safrid = kg_safrid * price_safrid

sum_midi = kg_midi * 7.5

all_sum = sum_palamud + sum_safrid + sum_midi

print(f'{all_sum:.2f}')
