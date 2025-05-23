from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

facts_list = ["Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.", 
            "Menurut sebuah penelitian yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka ketergantungan pada ponsel pintar mereka.", 
            "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini.", 
            "Studi tentang kecanduan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan."]

def generate_password(length=12, use_digits=True, use_special=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    return "<h1>about Among us</h1>"

@app.route("/random-fact")
def rand_fact():
    # cara pertama
    # text = random.choice(facts_list)
    # return text

    text = random.choice(facts_list)
    return f"<h1>Ini text yang diacak: {text}</h1> <a href='/about'>Kembali ke Home</a>"

@app.route("/Alamat")
def password_generator():
    # Ambil parameter dari URL (opsional)
    length = int(request.args.get('length', 12))
    use_digits = request.args.get('digits', 'true').lower() == 'true'
    use_special = request.args.get('special', 'true').lower() == 'true'

    password = generate_password(length, use_digits, use_special)

    return jsonify({
        'password': password,
        'length': length,
        'use_digits': use_digits,
        'use_special': use_special
    })

if __name__ == '__main__':

app.run(debug=True)
