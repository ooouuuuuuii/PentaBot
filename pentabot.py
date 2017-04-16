#!/usr/bin/env python
import praw

#Creates instance of bot
penta_bot = praw.Reddit(user_agent='PentaBot', client_id='4yX0om_uGfOuhw', client_secret='WF5iZjc5Cjmg8T5OjqvJHQTG2jY', username='PentaBot', password='00poiuytrewq00')

#Setting up
subreddit = bot.subreddit('Diepio')
comments = subreddit.stream.comments()
submissions = subreddit.stream.submissions()

#So I don't have to repeat it all the time :3
penta = 'pentabot, '

#Comment checker
for comment in comments:
		text = comment.body
		author = comment.author
		if penta + 'git gud' in text.lower():
			#Replies
			comment.reply("I got gud, skreb.")
		elif penta + 'penta' in text.lower():
			comment.reply("So balanced '3'.")
		elif penta + 'overlord' in text.lower():
			comment.reply("NEEERFFFF!")
		elif penta + 'team' in text.lower():
			comment.reply("*Spins*")
		elif penta + 'destroyer' in text.lower():
			comment.reply("NOOO! MY ONLY WEAKNESS!")
		elif penta + 'automod' in text.lower():
			comment.reply("I hope Automod-sama notices me...")
		elif penta + 'hi' in text.lower():
			comment.reply("Hi ")

#Post checker
#for submission in submissions:
