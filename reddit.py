'''
-Goals:
Get the api to work
Present the 30 posts to the user in a format of your choice
Allow user input to find specified subreddit

-To go above and beyond:
Create a gui, and give me a link to the story that opens up in a browser.
Allow the user to upvote/downvote

Link to methods: https://praw.readthedocs.org/en/v2.1.20/
'''

import praw #Import package with reddit library
r = praw.Reddit(user_agent='my_cool_application_miami') #Create reddit object

def main():
	subreddit = getSubreddit()
	number_of_subred = getNumber("How many topics do you want: ")
	subreddit = subreddit.get_hot(limit=number_of_subred)
	
	list = [str(item) for item in subreddit] #Create list of all found submissions

	for item in list: #Loop through list to print all found submissions
		print(item)
	
def getSubreddit():
	submissions = None
	try:
		subreddit = raw_input("Please enter name of subreddit: ") #Ask user for name of desired subreddit
		submissions = r.get_subreddit(subreddit)
	except:
		print("The subreddit %s does not exist." %(subreddit))
	
	return submissions

def getNumber(prompt):
	# Prompts user for input. Exception/While loop 
    # catches inputs that aren't proper integers.
    success = False
    number = 0
    while (not success):
        try:
            number = int(raw_input(prompt))
            success = True
        except:
            pass
        
    return number

	
if (__name__ == "__main__"):
	main()
	'''
	r = praw.Reddit(user_agent='my_cool_application_miami') #Create reddit object
	
	try:
		subreddit = raw_input("Please enter name of subreddit: ") #Ask user for name of desired subreddit
		
		submissions = r.get_subreddit(subreddit).get_hot(limit=30) #Get first 30 submissions from hot section of subreddit
		list = [str(item) for item in submissions] #Create list of all found submissions

		for item in list: #Loop through list to print all found submissions
			print(item)
	except:
		print("The subreddit %s does not exist." %(subreddit))
	'''	
		