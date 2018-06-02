'''
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
'''
# return masked string
def maskify(cc):
	if len(cc) >= 4:
		return '#' * (len(cc)-4) + cc[-4:]
	else:
		return cc

print maskify("4556364607935616") #== "############5616"
print maskify(     "64607935616") #==      "#######5616"
print maskify(               "1") #==                "1"
print maskify(                "") #==                 ""
print maskify("Skippy")                                   #== "##ippy"
print maskify("Nananananananananananananananana Batman!")# == "####################################man!"

'''
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

def maskify(cc):
    l = len(cc)
    if l <= 4: return cc
    return (l - 4) * '#' + cc[-4:]

def maskify(cc):
    return '{message:#>{fill}}'.format(message=cc[-4:], fill=len(cc))
    '''