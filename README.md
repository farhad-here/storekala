# 🛒 Django Online Shop

A multi-role e-commerce web application built with Django, where sellers can create and manage stores, and customers can browse products, maintain a shopping cart, and perform demo purchases through a balance-based payment system.

---

## ✨ Features

### 👤 Authentication & Authorization

* User registration and login
* Secure logout
* Role-based access control
* Django Admin integration

### 🏪 Store Management

* Sellers can create and manage their own stores
* Store detail pages with product listings
* Seller dashboard for store administration

### 📦 Product Management

* Create and manage products
* Product descriptions and pricing
* Store-specific product catalog
* Products displayed by newest first
* Product Categories
* Product Search
* Product Images Upload

### 🛍️ Shopping Experience

* Browse all products from the landing page
* Browse all stores
* Add products to cart
* Remove products from cart
* Cart quantity management
* Inventory Management

### 💳 Demo Payment System

* Customer wallet/balance
* Balance top-up page
* Checkout functionality
* Automatic balance deduction
* Demo revenue transfer to sellers

### 📜 Order Management

* Order history
* Order items tracking
* Purchase records

---

## 🏗️ System Architecture

### User Roles

#### Administrator

* Full access through Django Admin
* Manage users, stores, products, and orders

#### Seller

* Create stores
* Add and manage products
* View and manage owned stores

#### Customer

* Browse stores and products
* Add items to cart
* Manage wallet balance
* Place demo orders
* View order history

---

## 📄 Pages

| URL                 | Description                       | VIEW
| ------------------- | --------------------------------- | ---------------------------------
| `/`                 | Landing page with latest products | class HomePageView - get_queryset -> GET
| `/stores/`          | List of all stores                | stores_list -> GET
| `/stores/<id>/`     | Store details and products        | store_detail -> GET
| `/seller/`          | Seller dashboard                  | class SellerPanelView - get_queryset -> GET
| `/customer/`        | Customer dashboard                | customer_panel -> GET
| `/cart/`            | Shopping cart                     | cart -> GET
| `/payment/`         | Wallet top-up page                | payment_view -> GET , form.is_valid -> POST
| `/accounts/login/`  | Login page                        | login_view -> GET , form.is_valid -> POST
| `/accounts/signup/` | Registration page                 | signup_view -> GET , form.is_valid -> POST

---

## 🗃️ Database Models

### CustomerProfile

Stores customer-specific information:

```text
User
Phone Number
Balance
```

### SellerProfile

```text
User
```

### Store

```text
Name
Owner
Description
```

### Product

```text
Name
Price
Description
Image
Store
Created At
```

### CartItem

```text
Customer
Product
Quantity
```

### Order

```text
Customer
Total Amount
Created At
```

### OrderItem

```text
Order
Product
Quantity
Price
```

---

## 🔄 Checkout Flow

1. Customer adds products to cart
2. Customer proceeds to checkout
3. Total order amount is calculated
4. Customer balance is validated
5. Balance is deducted from customer account
6. Order and OrderItems are created
7. Seller receives demo revenue
8. Cart is cleared

---

## 🛠️ Tech Stack

* Python 3
* Django
* SQLite
* HTML5
* CSS3
* Django Templates
* JS

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/django-online-shop.git
cd django-online-shop
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

### Run Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Start Development Server

```bash
python manage.py runserver
```

---

## 📷 Screenshots

Add screenshots of:

* Landing Page
  <img width="2042" height="941" alt="digi1" src="https://github.com/user-attachments/assets/6219c760-f9bc-435c-ad69-46e5ef63d7f2" />

* Store Detail Page
  <img width="1436" height="687" alt="digi7" src="https://github.com/user-attachments/assets/e30c0bac-9332-468c-bab8-2e93f7935732" />

  
* Seller Dashboard
  <img width="1783" height="430" alt="digi6" src="https://github.com/user-attachments/assets/f398ac06-bbf1-4dc3-8254-2d464401538a" />

  
* Customer Dashboard
  <img width="1928" height="791" alt="digi" src="https://github.com/user-attachments/assets/f65af08d-a176-4dbe-aac9-e0be0a93406c" />

  
* Cart Page
  <img width="1768" height="489" alt="digi2" src="https://github.com/user-attachments/assets/fb1b10c7-0b33-4000-bd9b-84419c609b32" />

  
* Payment Page
  <img width="1850" height="561" alt="digi3" src="https://github.com/user-attachments/assets/d734a8cd-8825-478c-b7f9-40dfcbc4255b" />
  <img width="1830" height="750" alt="digi4" src="https://github.com/user-attachments/assets/1a555b64-e386-4c05-9ba2-2d8db89b1493" />

* signup and login
  <img width="2042" height="941" alt="digi1" src="https://github.com/user-attachments/assets/42d00b91-a314-400f-b10a-c5393b70fede" />
  <img width="2054" height="946" alt="digi2" src="https://github.com/user-attachments/assets/14a0ac0c-71d2-47b6-b525-7ff166fc2b49" />




---

## 📜 License

This project was developed for educational purposes and demonstrates core Django concepts including authentication, authorization, database modeling, shopping cart implementation, and multi-role application design.
