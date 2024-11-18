from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message').lower()

    # Definisikan respons berdasarkan input pengguna
    if "subjek hukum pidana" in user_input:
        response = "Subjek hukum pidana adalah individu yang melakukan tindakan pidana."
    elif "presumption of innocence" in user_input:
        response = "Presumption of innocence adalah prinsip hukum yang menyangkal keyakinan bahwa seseorang bersalah sampai terbukti secara sah."
    elif "regulasi resmi tentang hukum pidana" in user_input:
        response = "Regulasi resmi tentang hukum pidana di Indonesia bisa kita temukan di Undang-Undang Republik Indonesia Nomor 48 Tahun 2009 tentang Kriminal."
    elif "tindak pidana ringan" in user_input:
        response = "Tindak pidana ringan biasanya memiliki sanksi yang lebih ringan, sedangkan tindak pidana berat dikenakan sanksi yang lebih berat."
    elif "pembelaan diri" in user_input:
        response = "Pembelaan diri adalah alasan yang sah untuk melakukan tindakan yang biasanya dianggap sebagai kejahatan, jika tindakan tersebut dilakukan untuk melindungi diri dari ancaman nyata."
    elif "hukum pidana" in user_input:
        response = "Hukum pidana adalah cabang hukum yang mengatur tentang perbuatan-perbuatan yang dianggap sebagai tindak pidana..."
    elif "unsur" in user_input:
        response = "Unsur-unsur Hukum Pidana yaitu: Perbuatan, Melawan hukum, Kesalahan, Dipertanggungjawabkan..."
    elif "asas" in user_input:
        response = "Asas-asas Hukum Pidana dalam KHUP: Asas Legalitas, Asas Wilayah atau Teritorial..."
    else:
        response = "Maaf, saya belum bisa menjawab pertanyaan itu."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
