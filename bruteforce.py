import itertools
from pprint import pprint
import time
import json

START_TIME = time.time()
MISE_MAX_DU_CLIENT = 500

with open('actions_algoinvest.json') as f:
    data = json.load(f)

# Chaque action ne peut être achetée qu'une seule fois.
# Nous ne pouvons pas acheter une fraction d'action.
# Nous pouvons dépenser au maximum 500 euros par client.


liste_actions = data["les_20_actions"]
all_price = [action["price"] for action in liste_actions]

list_de_tests = [240, 480, 175, 15]
dict_de_tests = [{"nom": "Action-1", "price": 240, "profit": 5},
                 {"name": "Action-2", "price": 15, "profit": 10},
                 {"name": "Action-3", "price": 175, "profit": 15},
                 {"name": "Action-4", "price": 480, "profit": 5}]


def create_all_combinations(fichier_json, liste_des_prix, mise_max_du_client=500):
    """
    Cette fonction créer tout les combinaison possible d'une liste de nombres
    :param fichier_json: correspond a un dictionnaire contenant des actions
    :param liste_des_prix: liste des prix uniquement de toutes les actions d'un dictionnaire
    :param mise_max_du_client: la mise que le client va investir, par défaut 500 pour ce projet
    :return: Retourne une liste de listes contenant TOUTES les combinaison d'actions possible (plus d'1 millions)
    """
    all_combinations = []  # liste contenant toutes les listes de combinaisons // liste de tuples
    for L in range(len(liste_des_prix)):
        # subset sera forcement des nombres dans une tuple
        for subset in itertools.combinations(liste_des_prix, L):
            combi = []
            # je transforme les tuples de nombres en liste de dictionnaire contenant toutes les informations des actions
            if sum(subset) <= mise_max_du_client:
                for dicts in fichier_json:
                    if dicts["price"] in subset:
                        combi.append(dicts)
            # si la liste n'est pas vide:
            if combi:
                all_combinations.append(combi)
    return all_combinations


# def find_best_combinations (best profits + near 500€)
def find_best_combination(liste):
    """
    Cette fonction ce couple avec la fonction 'create_all_combinations', elle renvoie l'action la plus rentable/
    parmis toutes les combinaisons et l'affiche
    :param liste: la liste de toutes les combinaisons
    :return:
    """
    best_profits = 0
    best_action = str()
    for numb, combi in enumerate(liste, 1):
        prix_total = sum(action["price"] for action in combi)
        # print(f"combinaison n°{numb} - côuts total: {prix_total}")
        #profits de la combi en euro
        benef_total = 0
        for action in combi:
            benef_par_action = (action["price"] * action["profit"]) / 100
            # print(benef_par_action)
            benef_total += benef_par_action
        rendement = (benef_total / prix_total) * 100
        # print(f"total : {round(benef_total, 2)} ({round(rendement, 2)}%)")
        if benef_total > best_profits:
            best_profits = benef_total
            best_action = combi
    return best_action

def affichage(actions_a_afficher):
    print(actions_a_afficher)
    prix_total = sum(action["price"] for action in actions_a_afficher)
    benef_total = sum(action["price"] * action["profit"] / 100 for action in actions_a_afficher)
    rendement = (benef_total / prix_total) * 100
    print(f"côuts total: {prix_total}€, profits: {round(benef_total, 2)}€, rendement: {round(rendement, 2)}%")



if __name__ == "__main__":
    init_combi = create_all_combinations(liste_actions, all_price)
    best_combi = find_best_combination(init_combi)
    affichage(best_combi)
    print(f"\nCombinaisons : {len(init_combi)}")
    print("--- %s seconds ---" % (time.time() - START_TIME))

