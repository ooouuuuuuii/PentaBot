#!/usr/bin/env python
import praw

#Creates instance of bot
penta_bot = praw.Reddit(user_agent='PentaBot', client_id='4yX0om_uGfOuhw', client_secret='SEEECREET', username='PentaBot', password='NOT TELLING YOU LOL')

#Setting up
subreddit = penta_bot.subreddit('Diepio')
comments = subreddit.stream.comments()
#submissions = subreddit.stream.submissions()

#So I don't have to repeat it all the time :3
penta = 'pentabot, '

#Comment checker
#while True:
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
				comment.reply("So balanced '3'.")
				break
			elif penta + 'overlord' in text.lower():
				comment.reply("NEEERFFFF!")
				break
			elif penta + 'team' in text.lower():
				comment.reply("*Spins*")
				break
			elif penta + 'destroyer' in text.lower():
				comment.reply("Dodgeball is fun!")
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
			elif penta + 'spread' in text.lower():
				comment.reply("My poor, poor retarted brother.")
				break
			elif penta + 'suggestion' in text.lower():
				comment.reply("If you have a suggestion about me, you can PM /u/ooouuuuuii about it. I also mentioned him just now, so you can comment here too.")
				break
			elif penta + 'necromancer' in text.lower():
				comment.reply("I love me a little snack sometimes!")
				break
			elif penta + 'up up down down left right left right b a start' in text.lower():
				comment.reply("PentaBot has now evolved to TeraBot!")
				break
			elif penta + 'booster' in text.lower():
				comment.reply("Even faster than me!")
				break
			elif penta + 'spam' in text.lower():
				comment.reply("oooooookaaaaaaaaayayyyuyuyyuyiuwyiruweyiruewifjbgiwubwbiewuebvwiejvewuijniewuvgbnswaiubrvkizjrgeqlgipqibqh0843tuqevnjlakerjbgqoajfaj")
				break
			elif penta + 'up up down down left right left right b a start' in text.lower():
				comment.reply("PentaBot has now evolved to TeraBot!")
				break
			elif penta + 'buff' in text.lower():
				comment.reply("*squealing*")
				break
			elif penta + 'hap' in text.lower():
				comment.reply("HAPHAPHAPHAPHAPHAPHAPHAPHAPHAPHAPHAPHAPHAP")
				break
			elif penta + 'noob' in text.lower():
				comment.reply("U WOT M8")
				break
			elif penta + 'use thunderbolt' in text.lower():
				comment.reply("PENTAAA... BOOOOOOOOOOOOOOOOT!")
				break
			elif penta + 'predator' in text.lower():
				comment.reply("NOOOOO! MY ONLY WEEEAKNEEESSSS!")
				break
			elif penta + 'fanboy' in text.lower():
				comment.reply("*Changes font to Ubuntu Bold*")
				break
			elif penta + 'hate' in text.lower():
				comment.reply("**TRIGGERED**")
				break
			elif penta + 'in ur base' in text.lower():
				comment.reply("Killin ur doods, too!")
				break
			elif penta + 'attitude!' in text.lower():
				if author == 'ooouuuuuii':
					comment.reply("sorry dad")
				else:
					comment.reply("YOU'RE NOT MY DAD!")
				break
			#Commands inspired by others start here
			elif penta + 'fuck diep.io fuck fuckfcukfcyif fuck this fucking game fuckf uck' in text.lower():
				#thnx, /u/OvertrapperFTW
				comment.reply("so fucking rage")
				break
			elif penta + 'cancer' in text.lower():
				#thnx, /u/sbk2015
				comment.reply("[MG]xXminecraftkid_pro_sipn2taemXx")
				break
#Post checker
#for submission in submissions:
