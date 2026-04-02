import requests
from flask import Flask, render_template, request

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1489272849935106129/uxqY2Bl5G7XfW39zU6IeSSz70bHnhJ-OuZ6S8gR4YdnkF0HngUjLiL0pw54J8zssNLjj"
REVOLUT_LINK = "https://revolut.me/ceciliaadriana77"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/trimite', methods=['POST'])
def trimite():
    email = request.form.get('email_utilizator')
    steam = request.form.get('steam_link')
    pachet = request.form.get('pachet')
    
    # Setăm prețul și numele pachetului conform noilor cerințe
    pret = "1 RON" if pachet == "5_rep" else "5 RON"
    nume_pachet = "5 +REP" if pachet == "5_rep" else "25 +REP"

    # Notificare Discord
    data = {
        "embeds": [{
            "title": "⚡ COMANDĂ NOUĂ ESSK SHOP",
            "color": 4700159,
            "fields": [
                {"name": "Pachet", "value": f"**{nume_pachet}**", "inline": False},
                {"name": "Preț", "value": f"**{pret}**", "inline": False},
                {"name": "Email", "value": email, "inline": True},
                {"name": "Steam", "value": steam, "inline": True}
            ]
        }]
    }
    requests.post(WEBHOOK_URL, json=data)
    
    return f"""
    <body style="background:#0b0e11; color:white; text-align:center; padding-top:100px; font-family: sans-serif;">
        <div style="border: 1px solid #66c0f4; display: inline-block; padding: 40px; border-radius: 15px; background: #1b2838;">
            <h1>Comandă înregistrată! 🔥</h1>
            <p>Pachet: <b>{nume_pachet}</b></p>
            <p>Sumă de trimis: <b style="font-size:26px; color:#66c0f4;">{pret}</b></p>
            <br>
            <a href="{REVOLUT_LINK}/{pret.split()[0]}" target="_blank" 
               style="background:#fff; color:#000; padding:15px 30px; text-decoration:none; border-radius:10px; font-weight:bold; font-size:18px;">
               💳 TRIMITE BANII PE REVOLUT
            </a>
            <p style="margin-top:20px; color:#acb2b8;">Comanda se livrează imediat ce primim notificarea de plată.</p>
        </div>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True)
