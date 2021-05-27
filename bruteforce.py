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
all_combinations = []  # liste contenant toutes les listes de combinaisons // liste de tuples
liste_actions = data["les_20_actions"]
all_price = [action["price"] for action in data["les_20_actions"]]

list_de_tests = [240, 480, 175, 15]
dict_de_tests = [{"nom": "Action-1", "price": 240, "profit": 5},
                 {"name": "Action-2", "price": 15, "profit": 10},
                 {"name": "Action-3", "price": 175, "profit": 15},
                 {"name": "Action-4", "price": 480, "profit": 20}]

# def create_all_combinations()
for L in range(len(all_price)):
    # subset sera forcement des nombres dans une tuple
    for subset in itertools.combinations(all_price, L):
        combi = []
        if sum(subset) <= 500:
            for dicts in liste_actions:
                if dicts["price"] in subset:
                    combi.append(dicts)
        if combi:
            all_combinations.append(combi)

# def find_best_combinations (best profits + near 500€)
best_action = 0
for numb, combi in enumerate(all_combinations, 1):
    prix = [action["price"] for action in combi]
    profits = [action["profit"] for action in combi]
    moyenne_profits = sum(profits) / len(profits)
    gain = (sum(prix) * moyenne_profits) / 100
    print(f"combinaison n°{numb} - côuts total: {sum(prix)}")
    print(f"gain: {gain} ({moyenne_profits}% profits)")
    if gain > best_action:
        best_action = gain

print(best_action)


# print(len(all_combinations))
# print(all_combinations)


print("--- %s seconds ---" % (time.time() - START_TIME))
