import itertools
from pprint import pprint
import time
import json

START_TIME = time.time()
with open('actions_algoinvest.json') as f:
    data = json.load(f)

# Chaque action ne peut être achetée qu'une seule fois.
# Nous ne pouvons pas acheter une fraction d'action.
# Nous pouvons dépenser au maximum 500 euros par client.


"""
POUR  TESTER TOUTES LES COMBINAISONS POSSIBLE (bruteforce):
pour chaque nombre, tester tout les nombre en deuxieme, puis en toisieme... 
jusqua 500 de somme max

"""
liste_nombre = [20, 30, 50]
all_combinations = [] #liste contenant toutes les listes de combinaisons // liste de liste


all_price = [action["price"] for action in data["les_20_actions"]]
print(all_price)

for L in range(len(all_price)+1):
    for subset in itertools.combinations(all_price, L):
        if sum(subset) <= 500:
            all_combinations.append(subset)

# pprint(all_combinations)
print(len(all_combinations))

for numb, combi in enumerate(all_combinations):
    print(f"combinaison n°{numb}")
    print(f"côuts total :{sum(combi)}")





print("--- %s seconds ---" % (time.time() - START_TIME))