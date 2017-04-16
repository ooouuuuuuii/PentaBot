#!/usr/bin/env python
import praw

#Creates instance of bot
penta_bot = praw.Reddit(user_agent='PentaBot', client_id='4yX0om_uGfOuhw', client_secret='WF5iZjc5Cjmg8T5OjqvJHQTG2jY', username='PentaBot', password='00poiuytrewq00')

#Setting up
subreddit = penta_bot.subreddit('Diepio')
comments = subreddit.stream.comments()
#submissions = subreddit.stream.submissions()

#So I don't have to repeat it all the time :3
penta = 'pentabot, '

#Comment checker
for comment in comments:
		text = comment.body
		author = comment.author
		if penta + 'git gud' in text.lower():
			#Notifies reply being sent
			print("Replying to: {}".format(comment.title))
			#Actually replies
			comment.reply("I got gud, skreb.")
			#Makes sure that bot doesn't repeat itself
			break
		elif penta + 'penta' in text.lower():
			comment.reply("So balanced '3'.")
			break
		elif penta + 'overlord' in text.lower():
			comment.reply("NEEERFFFF!")
			break
		elif penta + 'team' in text.lower():
			comment.reply("*Spins*")
			break
		elif penta + 'destroyer' in text.lower():
			comment.reply("NOOO! MY ONLY WEAKNESS!")
			break
		elif penta + 'automod' in text.lower():
			comment.reply("I hope Automod-sama notices me...")
			break
		elif penta + 'hi' in text.lower():
			if author == 'ooouuuuuii':
				comment.reply("Hi dad :3")
			else:
				comment.reply("Hi u/{0}!".format(author))
			break

#Post checker
#for submission in submissions:
