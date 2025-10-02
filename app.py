from flask import Flask
from urllib.parse import quote

app = Flask(__name__)

@app.route("/")
def home():
    # Update image filenames to match your downloaded JPEGs
    brands = [
        {"name": "Nike", "image": "/static/nike.jpeg"},
        {"name": "Adidas", "image": "/static/adidas.jpeg"},
        {"name": "Puma", "image": "/static/puma.jpeg"},
        {"name": "Vans", "image": "/static/vans.jpeg"},
        {"name": "New Balance", "image": "/static/newbalance.jpeg"}
    ]
    
    html = """
    <html>
    <head>
        <title>Sneaker Hood</title>
        <style>
            body { font-family: Arial; background:#111; color:#fff; text-align:center; padding:30px; }
            h1 { color:#ffcc00; font-size:3em; margin-bottom:20px; }
            p { font-size:1.2em; }
            .brand-container { display:flex; justify-content:center; flex-wrap:wrap; gap:30px; margin-top:40px; }
            .brand-card { background:#222; border-radius:10px; padding:20px; width:220px; box-shadow:0 0 10px #000; }
            .brand-card img { width:200px; height:200px; object-fit:contain; margin-bottom:15px; }
            .btn { display:inline-block; background:#ffcc00; padding:10px 15px; border-radius:5px; color:#111; font-weight:bold; text-decoration:none; }
            .btn:hover { background:#ffaa00; }
        </style>
    </head>
    <body>
        <h1>Welcome to Sneaker Hood 👟</h1>
        <p>Your one-stop hub for the latest sneakers!</p>
        <div class="brand-container">
    """

    for brand in brands:
        message = f"Hey I'm interested in {brand['name']} sneakers"
        wa_link = f"https://wa.me/917038163608?text={quote(message)}"
        html += f"""
            <div class='brand-card'>
                <img src='{brand['image']}' alt='{brand['name']}'>
                <h3>{brand['name']}</h3>
                <a class='btn' href='{wa_link}' target='_blank'>Shop Now</a>
            </div>
        """
    
    html += """
        </div>
    </body>
    </html>
    """
    
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

