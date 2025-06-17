
```markdown
# 🧾 Receipt Generator

A lightweight Django web application that allows small businesses to quickly generate and email professional receipts without requiring user authentication. Just fill out a simple form with service/product details and buyer info — and you're done!

---

## 🚀 Features

- 📋 Input details for products/services, charges, tax rate, and buyer information
- 📄 Instantly generate a clean PDF receipt
- 📧 Automatically email the receipt to the buyer
- ✅ No login or authentication required — super simple and fast
- 🎯 Designed specifically for small businesses, freelancers, and local vendors

---

## ⚙️ Tech Stack

- **Backend**: [Django]
- **PDF Generation**: `xhtml2pdf`
- **Frontend**: HTML5, CSS3, Bootstrap, JS
- **Email Service**: Django's built-in email support (SMTP)
- **Deployment**: PythonAnywhere

---

## 📂 Project Structure

```

Receipt\_Generator/
├── form2pdf/        # Django project settings
├── formpdf/        # Django app that handles form logic and PDF generation
├── templates/       # HTML templates for forms and receipt display
├── manage.py

````

---

## 💻 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hardik450/Receipt_Generator.git
   cd Receipt_Generator
````

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the server**

   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit:
   `http://127.0.0.1:8000/`

---

## 📸 Screenshots

> *(Insert screenshots of the form page and a sample receipt PDF here)*

---

## 📬 Email Setup

To enable receipt emailing:

* Configure SMTP settings in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourprovider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_password'
```

> ⚠️ Use environment variables or Django's `decouple` library to keep credentials safe.

---

## 📌 Use Cases

* Small retailers
* Tuition teachers
* Freelancers
* Local service providers (e.g., electricians, tailors, consultants)

---

## 🚧 Future Improvements

* Mobile responsive design
* Multi-language PDF support
* Receipt number tracking/history
* Dark mode 😎

---

## 👤 Author

**Hardik Jain**
🧠 Passionate Django Developer
🔗 [LinkedIn](https://www.linkedin.com/in/hardik-jain-harsora-08b75a1b8)
📧 [hardikjainharsora@gmail.com](mailto:hardikjainharsora@gmail.com)

---

## 📄 License

This project is licensed under the [Apache License](LICENSE).

---

## 🌟 Support This Project

If you find this tool useful, consider giving it a ⭐️ on GitHub and sharing it with others!
