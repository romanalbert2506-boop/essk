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
    
    # Corecție prețuri și pachete
    pret = "1" if pachet == "5_rep" else "5"
    nume_pachet = "5 +REP-uri" if pachet == "5_rep" else "25 +REP-uri"

    # Notificare Discord
    data = {
        "embeds": [{
            "title": "🎮 NOUĂ COMANDĂ ESSK SHOP",
            "color": 5763719,
            "fields": [
                {"name": "📦 Pachet", "value": nume_pachet, "inline": True},
                {"name": "💰 Sumă", "value": f"{pret} RON", "inline": True},
                {"name": "📧 Email", "value": email, "inline": False},
                {"name": "🔗 Steam", "value": steam, "inline": False}
            ]
        }]
    }
    requests.post(WEBHOOK_URL, json=data)
    
    # Pagina de confirmare a plății
    return f"""
    <body style="background:#0b0e11; color:white; text-align:center; padding-top:100px; font-family: sans-serif;">
        <div style="border: 2px solid #66c0f4; display: inline-block; padding: 40px; border-radius: 20px; background: #1b2838; box-shadow: 0 0 20px #66c0f4;">
            <h1 style="color:#66c0f4;">Comandă înregistrată! 🔥</h1>
            <p>Pachet: <b>{nume_pachet}</b></p>
            <p>Sumă de trimis: <b style="font-size:24px;">{pret} RON</b></p>
            <br>
            <a href="{REVOLUT_LINK}/{pret}" target="_blank" 
               style="background:#fff; color:#000; padding:15px 30px; text-decoration:none; border-radius:10px; font-weight:bold; font-size:18px; display:inline-block;">
               💳 TRIMIT BANII PE REVOLUT
            </a>
            <p style="margin-top:20px; color:#acb2b8;">Verificăm plata și livrăm în maxim 30 min!</p>
        </div>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True)
