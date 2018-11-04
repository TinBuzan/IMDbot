import discord
import imdb

client = discord.Client()
with open('token.txt', 'r') as myfile:
    token = myfile.read().replace('\n', '')

@client.event # decorator/wrapper
async def on_ready():
    print(f'we have logged in as  {client.user}')

@client.event # bots react to user messages
async def on_message(message):
    # print(f'{message.channel} : {message.author} : {message.author.name} : {message.content}')

    if '?imdb q' == message.content.lower():
        await message.channel.send('Goodbye Peasants')
        client.close()
    elif '?imdb help' == message.content.lower():
        await message.channel.send(
        '''```\nCommands\n---\n?imdb q : quit IDMbot\n?imdb s {movie title} : search IDMb for movie```''')
    elif '?imdb s' in message.content.lower():
        i = imdb.IMDb()
        # Remove '?imdb' & 'sum' from search criteria
        words = message.content.split()[2:]
        # Join split values to new string
        movie_title = ' '.join(words)
        # search for our movie
        movie_list = i.search_movie(movie_title)
        # First match of search result
        first_match = movie_list[0]
        header = first_match.summary()
        # a lot of information will be printed
        i.update(first_match)
        # async print method for discord
        await message.channel.send('```\n' + first_match.summary() + '```')
    else:
        return
client.run(token)
