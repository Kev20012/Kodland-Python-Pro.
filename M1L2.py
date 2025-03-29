import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input("Masukkan panjang kata sandi yang diinginkan: "))

generated_password = ""
for i in range(pass_length):
    generated_password += random.choice(characters)

print("Kata sandi yang dihasilkan:", generated_password)
