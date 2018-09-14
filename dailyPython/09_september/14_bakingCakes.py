'''
Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object)
 and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the 
 amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the 
 objects, can be considered as 0.
'''

def cakes(recipe, available):
	possibleUnits = []
	for key in recipe:
		if key not in available.keys():
			return 0
		#print "recipe: ", key, 'corresponds to', recipe[key]
		#print available[key] 
		possibleUnits.append(available[key] / recipe[key])
	return min(possibleUnits)

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print cakes(recipe, available)#, 2, 'Wrong result for example #1')

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print cakes(recipe, available)#, 0, 'Wrong result for example #2')


def cakes(recipe, available):
  return min(available.get(k, 0)/recipe[k] for k in recipe)


def cakes(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0