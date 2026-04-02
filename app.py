import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# --- CONFIGURARE ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1489272849935106129/uxqY2Bl5G7XfW39zU6IeSSz70bHnhJ-OuZ6S8gR4YdnkF0HngUjLiL0pw54J8zssNLjj"
REVOLUT_LINK = "https://revolut.me/ceciliaadriana77"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/trimite', methods=['POST'])
def trimite():
    email = request.form.get('email_utilizator')
    steam = request.form.get('steam_link')
    pachet = request.form.get('pachet') # Luăm pachetul ales (1 RON sau 25 RON)
    pret = "1 RON" if pachet == "5_rep" else "25 RON"
    nume_pachet = "5 +REP-uri" if pachet == "5_rep" else "5 +REP-uri"

    # Notificare Discord
    data = {
        "embeds": [{
            "title": "💰 COMANDĂ NOUĂ - ESSK SHOP",
            "color": 3066993, # Verde Steam
            "fields": [
                {"name": "📦 Pachet Ales", "value": f"**{nume_pachet} ({pret})**", "inline": False},
                {"name": "📧 Email", "value": email, "inline": True},
                {"name": "🔗 Steam/ID", "value": steam, "inline": True}
            ],
            "footer": {"text": "Verifică Revolut pentru plată!"}
        }]
    }
    requests.post(WEBHOOK_URL, json=data)
    
    # Pagina de plată după comandă
    return f"""
    <body style="background:#0b0e11; color:white; text-align:center; padding-top:100px; font-family: sans-serif;">
        <div style="border: 2px solid #66c0f4; display: inline-block; padding: 40px; border-radius: 20px; background: #1b2838;">
            <h1>Comandă Înregistrată! 🚀</h1>
            <p>Ai ales: <b>{nume_pachet}</b></p>
            <p>Suma de plată: <b style="font-size:24px; color:#66c0f4;">{pret}</b></p>
            <br>
            <a href="{REVOLUT_LINK}/{pret.split()[0]}" target="_blank" 
               style="background:#fff; color:#000; padding:15px 30px; text-decoration:none; border-radius:10px; font-weight:bold;">
               💳 PLĂTEȘTE ACUM
            </a>
            <p style="margin-top:20px; font-size:12px; color:#acb2b8;">Dupa plată, procesăm comanda în max. 30 min.</p>
        </div>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True)