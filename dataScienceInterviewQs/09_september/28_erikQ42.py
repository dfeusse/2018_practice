'''
Question 42 - Sentiment analysis for app reviews
You are given an array containing reviews for a popular iOS app below: 

reviews = [list of reviews. ex "i love it", "i hate it"] 

Your task is to determine sentiment from the review above. 
To do this you first decide to write code to find the count of individual words across all the reviews -- 
write this code using Python.
'''
def lengthOfReviews(listOfReviews):
	return sum([len(i) for i in listOfReviews])
	words = 0
	for i in listOfReviews:
		words = words + len(i)
	return words


reviews = ["app is good, but forced updates are too frequent", "love this app, use it daily to log calories", "free version of this app has way too many ads", "app doesnt load, 0/10", "hate it", "so buggy", "amazing ux"] 
print lengthOfReviews(reviews)