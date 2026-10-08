# Simple E-commerce Product Management System

A clean and beginner-friendly Product Management System built with Python and Django for an e-commerce store. It allows store administrators to monitor inventory, track stock levels, and perform full CRUD operations (Create, Read, Update, Delete) on products with validation.

---

## 🚀 Technologies Used
* **Backend:** Python 3.12, Django
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
* **Image Processing:** Pillow (for product images)
* **Version Control:** Git & GitHub

---

## 📌 Features & Pages

1. **Authentication (Login & Logout)**
   * Secure admin login with session management.
   * Invalid credential validation messages.
   * Restricted access: only logged-in users can manage products.

2. **Dashboard**
   * Overview cards displaying:
     * **Total Products**
     * **Active Products**
     * **Inactive Products**
     * **Low Stock Products** (items with stock ≤ 5)
   * Quick navigation buttons to all sections.

3. **Product Listing Page**
   * Responsive table displaying product image, name, SKU, category, price, stock, status, and action buttons.
   * **Search bar** to search products by name.
   * **Category filter** dropdown.
   * **Status filter** (Active / Inactive).
   * **Pagination** (10 products per page).
   * **View Modal:** Instant detail popup displaying full product specs and description without leaving the page.
   * **Low Stock Badge:** Automatically flags products with stock ≤ 5.

4. **Add & Edit Product Form**
   * Single reusable form for both creating and editing products.
   * Image upload support.
   * Custom business validations:
     * Product name and SKU required.
     * SKU must be unique.
     * Price must be greater than 0.
     * Stock quantity cannot be negative.
     * Category selection required.

5. **Delete Confirmation**
   * Confirmation page to prevent accidental deletions.

---

## 🔑 Login Credentials

* **Username:** `admin`
* **Password:** `admin123`
* **Login URL:** `http://127.0.0.1:8000/login/`

---

## 💻 How to Install & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/mohdmasooud/ecommerce-product-management.git
cd assproj/product_management
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django pillow
```

### 4. Apply database migrations
```bash
python manage.py migrate
```

### 5. (Optional) Create your own admin account
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Open your browser and navigate to:
**`http://127.0.0.1:8000/`**
