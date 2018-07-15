'''
Exclamation marks series #8: Move all exclamation marks to the end of the sentence
Description:
Move all exclamation marks to the end of the sentence

Examples
remove("Hi!") === "Hi!"
remove("Hi! Hi!") === "Hi Hi!!"
remove("Hi! Hi! Hi!") === "Hi Hi Hi!!!"
remove("Hi! !Hi Hi!") === "Hi Hi Hi!!!"
remove("Hi! Hi!! Hi!") === "Hi Hi Hi!!!!"
'''
def remove(string):
	answer = ""
	exclamations = ""
	for i in string:
		if i == "!":
			exclamations += i
		else:
			answer += i
	return answer + exclamations


print remove("Hi!")# === "Hi!"
print remove("Hi! Hi!") #=== "Hi Hi!!"
print remove("Hi! Hi! Hi!")# === "Hi Hi Hi!!!"
print remove("Hi! !Hi Hi!")# === "Hi Hi Hi!!!"
print remove("Hi! Hi!! Hi!") #=== "Hi Hi Hi!!!!"