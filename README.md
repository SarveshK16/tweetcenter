# TweetCenter

**TweetCenter** is a Django-based web app to manage and analyze tweets. It helps organize tweets, explore and search by keywords or hashtags.

---

## 🚀 Features

- ✅ Tweet CRUD operations (Create, Read, Update, Delete)
- 🔍 Keyword & hashtag-based search
- 🔐 User authentication
- 📱 Mobile-friendly UI with Bootstrap

---

## 🛠️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/SarveshK16/tweetcenter.git
cd tweetcenter
```
2. **Create a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt
```
4. **Apply migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```
5. **Run the development server:**

```bash
python manage.py runserver
```
6. **Access the application:** Open your browser and navigate to http://localhost:8000/

---

## 📁 Project Structure

```bash
tweetcenter/
├── tweetcenter/        # Main Django Project
├── media/              # Store media files, user uploaded images
├── tweet/              # Django app for tweet functionalities
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, images)
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── .prettierignore     # Prettier ignore file  
└── .gitignore          # Git ignore file
```

---

## 📄 License
This project is licensed under the MIT License.

---

## 📬 Contact
For any inquiries or feedback, please reach out to sskulkarni161@gmail.com
