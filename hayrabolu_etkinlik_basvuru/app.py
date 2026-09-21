from flask import Flask, render_template, request
from supabase import create_client
import os

app = Flask(__name__, template_folder="Templates")


# Supabase bağlantısı
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")

supabase = create_client(supabase_url, supabase_key)


@app.route("/", methods=["GET", "POST"])
def ana_sayfa():

    if request.method == "POST":

        ad_soyad = request.form["ad_soyad"]
        tc = request.form["tc"]
        telefon = request.form["telefon"]
        dogum_tarihi = request.form["dogum_tarihi"]
        kurs = request.form["kurs"]
        aciklama = request.form["aciklama"]

        # Supabase veritabanına kayıt
        supabase.table("basvurular").insert({
            "ad_soyad": ad_soyad,
            "tc": tc,
            "telefon": telefon,
            "dogum_tarihi": dogum_tarihi,
            "kurs": kurs,
            "aciklama": aciklama
        }).execute()

        return render_template("basarili.html")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
