'''
Your task is to write a function maskify, which changes all but the last four characters into '#'.
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
'''
def maskify(cc):
	return ((len(cc) - 4) * '#') + cc[-4:]


print maskify("4556364607935616")# == "############5616"
print maskify(     "64607935616")# ==      "#######5616"
print maskify(               "1") #==                "1"
print maskify(                "")# ==                 ""