from pprint import pprint
import time
import json

START_TIME = time.time()

with open('actions_algoinvest.json') as f:
    data = json.load(f)


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
    for action in top_actions:
        if action["price"] > 0:
            # if action["price"] + porte_monnaie > mise_max_par_client:
            #     continue
            # if action["price"] == 42:
            #     continue
            investissement.append(action)
            porte_monnaie += action["price"]
            benef = (action["price"] * action["profit"]) / 100
            print(benef)
            total_return += benef
            if porte_monnaie > mise_max_par_client:
                investissement.pop(-1)
                porte_monnaie -= action["price"]
                total_return -= benef
                break

    # print(f"total cost : {round(porte_monnaie, 2)}")
    # print(f"total return : {round(total_return, 2)}")
    return investissement, round(porte_monnaie, 2), round(total_return, 2)


test = get_top_investissement(data["les_20_actions"])
print()
pprint(test[0])
print(f" total cost : {test[1]}")
print(f" total return : {test[2]}")


# for numb, action in  enumerate(get_top_investissement(data["Sienna_dataset1"])):
#     print(numb+1, action['name'])


print("--- %s seconds ---" % (time.time() - START_TIME))
