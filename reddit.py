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
from Tkinter import *

class Reddit_App:

	def __init__(self):
		r = praw.Reddit(user_agent='my_cool_application_miami') #Create reddit object
		self.login = Tk()
		self.login.wm_title("Reddit Login")
		self.main = Tk()
		self.main.wm_title("Reddit")

		self.login_label_username = Label(self.login, text="Username:")
		self.login_label_password = Label(self.login, text="Password:")
		self.login_label_username.grid(row=0,column=0)
		self.login_label_password.grid(row=1,column=0)

		self.login_username = Entry(self.login)
		self.login_password = Entry(self.login)
		self.login_username.grid(row=0,column=1)
		self.login_password.grid(row=1,column=1)

		self.login_submit_button = Button(self.login, text="Submit")
		self.login_submit_button.grid(row=2,columnspan=2)
		
		self.login.mainloop()	
		self.main.mainloop()
		
	def main(self):
		subreddit = getSubreddit()
		number_of_subred = getNumber("How many topics do you want: ")
		subreddit = subreddit.get_hot(limit=number_of_subred)
		try:
			list = [str(item) for item in subreddit] #Create list of all found submissions
		except:
			print("The subreddit does not exist.")
			quit()
			
		for item in list: #Loop through list to print all found submissions
			print(item)
	
	def getSubreddit(self):
		subreddit = raw_input("Please enter name of subreddit: ") #Ask user for name of desired subreddit
		submissions = r.get_subreddit(subreddit)
		
		return submissions

	def getNumber(self, prompt):
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
	Reddit_App()
	
'''
-Buttons on GUI can be equivalent to numbers in dictionary-as-switch.
-Establish what options users can select from program.
-Allow ability to login if desired. Have if-statements for when user tries option that requires logging in, but isn't logged in.
'''