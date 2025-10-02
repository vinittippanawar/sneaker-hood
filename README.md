# 👟 Sneaker Hood

Sneaker Hood is a simple **Flask web application** showcasing popular sneaker brands. Users can click **Shop Now** to directly message via WhatsApp.

---

## 🚀 Features

- Display sneaker brands with images  
- Shop Now button redirects to WhatsApp  
- Built with Python Flask and Gunicorn  
- Easy deployment on AWS EC2  

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** Inline HTML & CSS (rendered by Flask)  
- **Server:** Gunicorn  
- **Deployment:** AWS EC2  

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


---

## ⚙️ Installation & Local Setup

### Clone the Repository

git clone git@github.com:vinittippanawar/sneaker-hood.git
cd sneaker-hood

Install Python Dependencies
bash

python3 -m venv myenv
source myenv/bin/activate

Run the App Locally

python app.py
# or using Gunicorn
gunicorn -b 0.0.0.0:5000 app:app --daemon


Access the Site
http://<EC2-PUBLIC-IP>:5000

-------

📡 Deployment on AWS EC2

Launch an Amazon Linux 2023 EC2 instance

Open port 5000 in Security Group

Install Python & dependencies

Copy project files to EC2

Run with Gunicorn as shown above

--------

✍️ Author
Vinit Tippanawar
