import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channels
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NjAxOTUxMTgyNDAzMDEwNjMw.XTJw7A.C4qDOCh0CG0rKsGnFoPqm25z4GE'
self_bot_token = 'NTQ5OTQwOTc3MTE3Mjk4NzA4.XSxtxA.p7sDLqU4kCjN240l7r7uCE-xXp0'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '603475810489466880')

input_hq_private  = [
    "603475810489466880",
    "593990608914219008",
    "569420128794443776",
	    "601814968710594627",
	    "595635734904307742",
	    "590109407950667776",
	    "601966175525666817",
	    "590224806256050196",
	    "590182835948879872",
	    "570257859850272788",
	    "590471026899550208",
	    "589120764347678750",
	    "585682137202819101",
	    "590470896649502750",
	    "590182635653824542",
	    "589120764347678750",
	    "589516793350062100",
    "583796470394781696",
    "603475810489466880", # answers1
    "559442345674670082", #answers2
    '577486564402397194' #trivia-answers
]
input_hq_public = ['603475810489466880']
command_channel = '603475810489466880' #trivia-answers
admin_chat = '603475810489466880' # answers2

game_in_session = False
counter_public_1 = 0
counter_public_2 = 0
counter_public_3 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter1 = 0
counter2 = 0
counter3 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0

seconds_elapsed = 0
