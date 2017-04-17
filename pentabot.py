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
			print("Replying to: " + comment.title)
			#Actually replies
			comment.reply("I got gud, skreb.")
			#Makes sure that bot doesn't repeat itself
			break
		elif penta + 'penta' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("So balanced '3'.")
			break
		elif penta + 'overlord' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("NEEERFFFF!")
			break
		elif penta + 'team' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("*Spins*")
			break
		elif penta + 'destroyer' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("NOOO! MY ONLY WEAKNESS!")
			break
		elif penta + 'automod' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("I hope Automod-sama notices me...")
			break
		elif penta + 'hi' in text.lower():
			if author == 'ooouuuuuii':
				print("Replying to you. Why are you doing that?")
				comment.reply("Hi dad :3")
			else:
				print("Replying to: " + comment.title)
				comment.reply("Hi u/{0}!".format(author))
			break
		elif penta + 'spread' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("My poor, poor retarted brother.")
			break
		elif penta + 'destroy' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("YES MASTER.")
			break
		elif penta + 'suggestion' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("If you have a suggestion about me, you can PM /u/ooouuuuuii about it. I also mentioned him just now, so you can comment too.")
			break
		elif penta + 'necromancer' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("I love me a little snack sometimes!")
			break
		elif penta + 'up up down down left right left right b a start' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("PentaBot has now evolved to TeraBot!")
			break
		elif penta + 'booster' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("Even faster than me!")
			break
		elif penta + 'spam' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("oooooookaaaaaaaaayayyyuyuyyuyiuwyiruweyiruewifjbgiwubwbiewuebvwiejvewuijniewuvgbnswaiubrvkizjrgeqlgipqibqh0843tuqevnjlakerjbgqoajfaj")
			break
		elif penta + '日本語' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("すみません。　少し　日本語を　話します。")
			break
		elif penta + 'up up down down left right left right b a start' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("PentaBot has now evolved to TeraBot!")
			break
		elif penta + 'buff' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("*squealing*")
			break
		elif penta + 'hap' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("HAPHAPHAPHAPHAPHAPHAPHAPHAPHAPHAPHAPHAPHAP")
			break
		elif penta + 'noob' in text.lower():
			print("Replying to: " + comment.title)
			comment.reply("U WOT M8")
			break

#Post checker
#for submission in submissions:
