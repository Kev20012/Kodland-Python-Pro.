import discord
from discord.ext import commands

# Mengatur bot agar bisa membaca pesan
intents = discord.Intents.default()
intents.message_content = True

# Membuat bot dengan prefix $
bot = commands.Bot(command_prefix="$", intents=intents)

# Menyimpan data polusi untuk setiap pengguna (sementara, di memori)
data_polusi = {}

@bot.event
async def on_ready():
    print(f"Bot berhasil login sebagai {bot.user}")

# Command untuk mencatat aktivitas polusi
@bot.command()
async def catat_polusi(ctx, jenis: str, jumlah: int):
    user_id = ctx.author.id  # ID pengguna
    # Jika belum ada data, buat data kosong
    if user_id not in data_polusi:
        data_polusi[user_id] = {}

    # Jika jenis belum ada, set 0 dulu
    if jenis not in data_polusi[user_id]:
        data_polusi[user_id][jenis] = 0

    # Tambahkan jumlah polusi
    data_polusi[user_id][jenis] += jumlah

    await ctx.send(f"✅ Kamu mencatat {jumlah} untuk jenis polusi '{jenis}'.")

# Command untuk melihat total polusi yang dicatat
@bot.command()
async def total_polusi(ctx):
    user_id = ctx.author.id
    if user_id not in data_polusi or not data_polusi[user_id]:
        await ctx.send("📭 Belum ada data polusi yang kamu catat.")
        return

    # Buat pesan laporan total
    pesan = "📊 Total Polusi yang Kamu Catat:\n"
    for jenis, jumlah in data_polusi[user_id].items():
        pesan += f"- {jenis}: {jumlah}\n"
    await ctx.send(pesan)

# Command untuk mereset (menghapus) semua data polusi
@bot.command()
async def reset_polusi(ctx):
    user_id = ctx.author.id
    data_polusi[user_id] = {}
    await ctx.send("♻️ Semua data polusi kamu sudah dihapus.")

# Command untuk bantuan
@bot.command()
async def bantu(ctx):
    bantuan = (
        "**Panduan Bot Pencatat Polusi**\n"
        "`$catat_polusi <jenis> <jumlah>` - Catat aktivitas polusi\n"
        "`$total_polusi` - Lihat total polusi\n"
        "`$reset_polusi` - Hapus semua data\n"
        "`$bantu` - Tampilkan panduan ini"
    )
    await ctx.send(bantuan)

with open('token.txt', 'r') as file:
    token = file.read()

# Menjalankan bot
bot.run(token)
