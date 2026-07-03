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

### 🛍️ Shopping Experience

* Browse all products from the landing page
* Browse all stores
* Add products to cart
* Remove products from cart
* Cart quantity management

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

| URL                 | Description                       |
| ------------------- | --------------------------------- |
| `/`                 | Landing page with latest products |
| `/stores/`          | List of all stores                |
| `/stores/<id>/`     | Store details and products        |
| `/seller/`          | Seller dashboard                  |
| `/customer/`        | Customer dashboard                |
| `/cart/`            | Shopping cart                     |
| `/payment/`         | Wallet top-up page                |
| `/accounts/login/`  | Login page                        |
| `/accounts/signup/` | Registration page                 |

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
* Bootstrap (if used)
* Django Templates

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
* Store Detail Page
* Seller Dashboard
* Customer Dashboard
* Cart Page
* Payment Page

---

## 🎯 Optional Enhancements

* Product Search
* Product Categories
* Product Images Upload
* Inventory Management
* Thank You Page
* Real Payment Gateway Integration
* Product Reviews & Ratings
* REST API with Django REST Framework

---

## 📜 License

This project was developed for educational purposes and demonstrates core Django concepts including authentication, authorization, database modeling, shopping cart implementation, and multi-role application design.
