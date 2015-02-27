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
	
if (__name__ == "__main__"):
	r = praw.Reddit(user_agent='my_cool_application_miami') #Create reddit object
	
	'''
	Account for RedirectException if user inputs invalid subreddit.
	'''
	try:
		#Ask user for name of desired subreddit
		subreddit = raw_input("Please enter name of subreddit: ") 
		
		submissions = r.get_subreddit(subreddit).get_hot(limit=30) #Get first 30 submissions from hot section of subreddit
		list = [str(item) for item in submissions] #Create list of all found submissions

		for item in list: #Loop through list to print all found submissions
			print(item)
	except:
		print("The subreddit %s does not exist." %(subreddit))
		
		