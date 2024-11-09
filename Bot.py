import discord
import rpoems
import randfacts
 
 
 
from datetime import datetime as dt
before = dt(2018, 8, 22)
after = dt(2018, 8, 20)
corpus = rpoems.build_corpus(subreddit="AskReddit", before=before, after=after, limit=1000)
poem = rpoems.couplet_rhyming_poem(corpus)
 
client = discord.Client()
 
@client.event
async def on_ready():
   print(f'{client.user.name} has connected to Discord!')
 
@client.event
async def on_message(message):
   print(message)
   print(message.author)
   print(message.content)
   if 'redditpoem' in message.content.lower():
       poem = rpoems.couplet_rhyming_poem(corpus)
       await message.channel.send(poem)
   if 'randomfact' in message.content.lower():
       randomfact = randfacts.get_fact()
       await message.channel.send(randomfact)
   if 'Redditpoem' in message.content.lower():
       poem = rpoems.couplet_rhyming_poem(corpus)
       await message.channel.send(poem)
   if 'Randomfact' in message.content.lower():
       randomfact = randfacts.get_fact()
       await message.channel.send(randomfact)
 
      
 
client.run('TOKEN HERE')
