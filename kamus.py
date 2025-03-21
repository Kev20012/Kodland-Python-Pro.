meme_dict = {"CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "SHEESH": "sedikit ketdaksetujuan",
            "SECRET": "suatu rahasia",
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    
else:
    print("Tidak ada kata yang ditemukan")
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
