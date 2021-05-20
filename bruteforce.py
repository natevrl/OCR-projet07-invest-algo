from pprint import pprint
import time
import json

START_TIME = time.time()


with open('actions_algoinvest.json') as f:
    data = json.load(f)


# Chaque action ne peut être achetée qu'une seule fois.
# Nous ne pouvons pas acheter une fraction d'action.
# Nous pouvons dépenser au maximum 500 euros par client.


# for action in actions_algoinvest:
#     print(action["benef%_apres2ans"])


def get_top_investissement(list_actions, MISE_MAX_PAR_CLIENT=500, porte_monnaie=0):
    """
    :param list_actions: liste d actions(boursière) à trier
    :param MISE_MAX_PAR_CLIENT: par défaut le client investis 500 euros
    :param porte_monnaie: par défaut le porte monnaie du client commence à 0 euros
    """
    top_actions = sorted(list_actions, key=lambda tri: tri.get("profit"), reverse=True)
    pprint(top_actions)
    investissement = []
    total_return = 0
    for action in top_actions:
        if action["price"] + porte_monnaie > MISE_MAX_PAR_CLIENT:
            continue
        investissement.append(action)
        porte_monnaie += action["price"]
        benef = (action["price"] * action["profit"]) / 100
        total_return += benef
        print(benef)
    print(porte_monnaie)
    print(total_return)
    return investissement


pprint(get_top_investissement(data["les_20_actions"]))

print("--- %s seconds ---" % (time.time() - START_TIME))
