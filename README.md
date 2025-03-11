# 🚀 Bidding API  

## 📌 Overview  
Bidding API is a Django-based web application that allows users to register and manage bids on plates. Only staff users have permission to add, edit, and delete plates.  

## 🛠 Features  
- **User Registration** (Both staff & non-staff)  
- **Authentication & Permissions** (Only staff can manage plates)  
- **List & View Plates** (Displays the last 10 plates)  
- **Bootstrap-based UI** for an improved user experience  

## 📦 Installation  
1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-repo/bidding-api.git
   cd bidding-api
   ```

2. **Create a virtual environment & activate it**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (Optional, for admin access)**  
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**  
   ```bash
   python manage.py runserver
   ```

## 🔑 User Roles  
- **Staff Users**: Can add, edit, and delete plates.  
- **Regular Users**: Can register but cannot modify plates.  

## 🖥 API Endpoints  
| Endpoint       | Method | Description |
|---------------|--------|-------------|
| `/register/`  | POST   | User Registration |
| `/plates/`    | GET    | View Last 10 Plates |
| `/plates/add/` | POST  | (Staff Only) Add a New Plate |
| `/plates/edit/{id}/` | PUT | (Staff Only) Edit a Plate |
| `/plates/delete/{id}/` | DELETE | (Staff Only) Delete a Plate |

## 📜 License  
This project is open-source. Feel free to modify and improve it!  

---

Let me know if you need any modifications! 🚀
