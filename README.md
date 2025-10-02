# Sneaker Hood

Sneaker Hood is a simple **Flask web application** showcasing popular sneaker brands like **Nike, Adidas, Puma, Vans, and New Balance**. Users can click **Shop Now** to directly message via WhatsApp.

---

## 🚀 Features
- Display sneaker brands with images
- "Shop Now" button redirects to WhatsApp
- Built with Python Flask and Gunicorn
- Responsive layout with inline HTML & CSS

---

## 🛠 Tech Stack
- **Backend:** Python Flask  
- **Server:** Gunicorn  
- **Frontend:** Inline HTML & CSS rendered by Flask  
- **Other:** EC2 deployment, static images

---

## 📂 Project Structure
sneaker-hood/
├─ app.py # Main Flask application
├─ README.md # Project documentation
├─ static/ # Images & static assets
│ ├─ nike.jpeg
│ ├─ adidas.jpeg
│ ├─ puma.jpeg
│ ├─ vans.jpeg
│ └─ new_balance.jpeg

## ⚙️ Installation & Local Setup

1. **Clone the Repository**
```bash
git clone git@github.com:vinittippanawar/sneaker-hood.git
cd sneaker-hood

Install Python Dependencies

python3 -m venv myenv
source myenv/bin/activate

Run the App Locally

python app.py
# or using Gunicorn
gunicorn -b 0.0.0.0:5000 app:app --daemon

Access the Site

http://<EC2-PUBLIC-IP>:5000

📡 Deployment on AWS EC2

Launch an EC2 Amazon Linux 2023 instance

Open port 5000 in Security Group

Install Python & dependencies

Copy project files to EC2

Run with Gunicorn as shown above

✍️ Author: Vinit T
