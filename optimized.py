from pprint import pprint
import time
import json

START_TIME = time.time()

with open('actions_algoinvest.json') as f:
    data = json.load(f)

"""
Cet algorithme commence par trier la liste d'actions par ordre décroissant de profit
du plus rentable au moins rentable.
Il ajoute dans une nouvelle list les actions en partant du haut jusqu'a atteindre la mise du client
(500 euros pour ce projet).
 Option 01 : Si une actions dépasse les 500 eu, il passe a l'actions d'en dessous.
 Option 02 : Dès que tu ajoutes une action qui fait dépasser la mise client, tu l'enlève de la liste et tu arrete l'algo
"""


def get_top_investissement(list_actions, mise_max_par_client=500, porte_monnaie=0):
    """
    :param list_actions: liste d actions(boursière) à trier
    :param mise_max_par_client: par défaut le client investis 500 euros
    :param porte_monnaie: par défaut le porte monnaie du client commence à 0 euros
    """
    top_actions = sorted(list_actions, key=lambda tri: tri.get("profit"), reverse=True)
    pprint(top_actions)
    investissement = []
    total_return = 0
    moyenne_profits = 0
    for action in top_actions:
        # Si l'action fait entre 1 et 500€
        if 0 < action["price"] <= mise_max_par_client:
            # option 1 : Si l'action + la somme du porte monnai actuel dépasse la mise client,
            # Alors tu passe a l'action suivante (continue)
            # if action["price"] + porte_monnaie > mise_max_par_client:
            #     continue
            investissement.append(action)
            porte_monnaie += action["price"]
            benef = (action["price"] * action["profit"]) / 100
            moyenne_profits += action["profit"]
            total_return += benef
            # option 2 : Dès que tu ajoute une action qui fait dépasser la mise client, tu l'enlève et tu arrete l'algo
            if porte_monnaie > mise_max_par_client:
                investissement.pop(-1)
                porte_monnaie -= action["price"]
                total_return -= benef
                break
            print(benef)
    # print(f"total cost : {round(porte_monnaie, 2)}")
    # print(f"total return : {round(total_return, 2)}")
    return investissement, round(porte_monnaie, 2), round(total_return, 2), round(total_return / porte_monnaie * 100, 2)


if __name__ == "__main__":
    test = get_top_investissement(data["Sienna_dataset1"])
    print("\nSelon l'algo, voici la meilleur combinaison d'action : ")
    # la fonction return une tuple de plusieurs value,
    # j'appelle l'instance de la fonction avec l'index de chaque valeurs
    pprint(test[0])
    print(f" total cost : {test[1]}")
    print(f" total return : {test[2]}")
    print(f" profits : {test[3]}%")

    print("--- %s seconds ---" % (time.time() - START_TIME))
