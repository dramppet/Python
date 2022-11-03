aquarium_length = int(input())
aquarium_weidht = int(input())
aquarium_height = int(input())
procent = float(input())

voluem_aquarium = aquarium_length * aquarium_weidht * aquarium_height
litri = voluem_aquarium / 1000
need_litri = litri * (1 - procent/100)

print(need_litri)