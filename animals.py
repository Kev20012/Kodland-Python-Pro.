link_animals = ['animal-memes-10-20240825.jpg', 'animalmeme2.jpg', 'animalmeme3,jpeg']
# ini buat file gambar

@bot.command('animals')
async def animals(ctx):
    link_animals = os.listdir('animals')
    link_yang_dipilih = random.choice(link_animals)
    
    with open(f'animals/{link_yang_dipilih}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
# ini buat commands gambar
