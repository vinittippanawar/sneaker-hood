echo "# Sneaker Hood

Sneaker Hood is a simple Flask web application showcasing popular sneaker brands like Nike, Adidas, Puma, Vans, and New Balance.
Users can click **Shop Now** to directly message via WhatsApp.

## Features
- Display sneaker brands with images
- Shop Now button redirects to WhatsApp
- Built with Python Flask and Gunicorn

## How to Run
\`\`\`bash
cd sneaker-hood
gunicorn -b 0.0.0.0:5000 app:app --daemon
\`\`\`
Access the site at: http://<Your-EC2-IP>:5000
" > README.md
