import discord
import random
import requests
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#URL of animal
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

#block of random animals
@bot.command()
async def animal(ctx):
    animals = ['duck', 'dog', 'fox']
    random_animal = random.choice(animals)

    if random_animal == 'duck':
        image_url = get_duck_image_url()
    elif random_animal == 'dog':
        image_url = get_dog_image_url()
    elif random_animal == 'fox':
        image_url = get_fox_image_url()

    await ctx.send(image_url)

bot.run("token")
