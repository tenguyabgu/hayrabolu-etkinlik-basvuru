from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def ana_sayfa():

    if request.method == "POST":

        ad_soyad = request.form["ad_soyad"]
        tc = request.form["tc"]
        telefon = request.form["telefon"]
        dogum_tarihi = request.form["dogum_tarihi"]
        kurs = request.form["kurs"]
        aciklama = request.form["aciklama"]

        with open("basvurular.txt", "a", encoding="utf-8") as dosya:

            dosya.write("YENİ BAŞVURU\n")
            dosya.write("------------------------------\n")
            dosya.write(f"Ad Soyad: {ad_soyad}\n")
            dosya.write(f"T.C. Kimlik No: {tc}\n")
            dosya.write(f"Telefon: {telefon}\n")
            dosya.write(f"Doğum Tarihi: {dogum_tarihi}\n")
            dosya.write(f"Kurs: {kurs}\n")
            dosya.write(f"Açıklama: {aciklama}\n")
            dosya.write("------------------------------\n\n")

        return render_template("basarili.html")

    return render_template("index.html")


if __name__ == "__main__":

    print("ÇALIŞAN KLASÖR:", os.getcwd())
    print("LOGO VAR MI:", os.path.exists("static/images/belediye-logo.png"))

    app.run(debug=True)