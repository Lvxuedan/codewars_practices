'''Backer'''

def cakes(recipe, available):
    # TODO: insert code
    available_none = list(set([i for i in recipe])-set([i for i in available]))
    if len(available_none) > 0:
        return 0
    a_list = [available[i]/recipe[i] for i in recipe]
    return min(a_list)

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
cakes(recipe, available)

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
cakes(recipe, available)