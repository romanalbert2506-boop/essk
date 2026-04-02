import requests
from flask import Flask, render_template, request

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1489272849935106129/uxqY2Bl5G7XfW39zU6IeSSz70bHnhJ-OuZ6S8gR4YdnkF0HngUjLiL0pw54J8zssNLjj"
REVOLUT_LINK = "https://revolut.me/ceciliaadriana77"
NUMAR_TELEFON = "07xx xxx xxx" # Pune aici numărul tău de Revolut/BT Pay
IBAN_BANCAR = "ROxx XXXX XXXX XXXX XXXX XXXX" # Pune IBAN-ul tău dacă vrei transfer bancar

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/trimite', methods=['POST'])
def trimite():
    email = request.form.get('email_utilizator')
    steam = request.form.get('steam_link')
    pachet = request.form.get('pachet')
    
    pret = "1 RON" if pachet == "5_rep" else "5 RON"
    nume_pachet = "5 +REP" if pachet == "5_rep" else "25 +REP"

    # Notificare Discord
    data = {"embeds": [{"title": "🔥 COMANDĂ NOUĂ", "color": 65535, 
                        "fields": [{"name": "Pachet", "value": nume_pachet}, 
                                   {"name": "Email", "value": email}, 
                                   {"name": "Steam", "value": steam}]}]}
    requests.post(WEBHOOK_URL, json=data)
    
    return f"""
    <body style="background:#0b0e11; color:white; font-family:sans-serif; text-align:center; padding:50px;">
        <div style="background:#1b2838; padding:30px; border-radius:15px; display:inline-block; border:1px solid #2a475e; max-width:400px;">
            <h2 style="color:#66c0f4;">🛒 Finalizare Plată: {pret}</h2>
            <p style="color:#acb2b8;">Alege metoda preferată:</p>
            
            <div style="text-align:left; margin-top:20px;">
                <a href="{REVOLUT_LINK}/{pret.split()[0]}" style="display:block; background:#fff; color:#000; padding:12px; margin-bottom:10px; text-decoration:none; border-radius:8px; font-weight:bold; text-align:center;">💳 Plătește cu Revolut (Link)</a>
                
                <div style="background:#101822; padding:15px; border-radius:8px; border:1px solid #2a475e; margin-bottom:10px;">
                    <small style="color:#66c0f4;">📱 TRANSFER TELEFON (Revolut/BT Pay):</small><br>
                    <b>{NUMAR_TELEFON}</b>
                </div>

                <div style="background:#101822; padding:15px; border-radius:8px; border:1px solid #2a475e;">
                    <small style="color:#66c0f4;">🏦 TRANSFER BANCAR (IBAN):</small><br>
                    <span style="font-size:12px;">{IBAN_BANCAR}</span>
                </div>
            </div>
            
            <p style="font-size:11px; color:#acb2b8; margin-top:20px;">După plată, trimite un screenshot pe Discord!</p>
        </div>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True)
