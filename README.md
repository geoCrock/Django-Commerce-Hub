# Django Commerce Hub

The Django Commerce Hub project is an integrated solution for providing secure and convenient online payments in your online store using the Stripe service.

Main functions:

- Multiple products: Ability to add and display various products with their description, price and unique identifier.

- Stripe Checkout: Integration with Stripe API to ensure secure payments. Customers can easily make purchases using payment cards.

- Product Details: View details about the selected product on a separate page, including a description and a "Buy" button to proceed to checkout.

- Streamlined checkout process: Redirect customers to Stripe's convenient and secure Checkout page to complete payment.

- Order Management: Ability to create and manage orders, combining multiple products into one order.

Advantages:

- Easy integration: Easily add payment functionality to your online store with minimal effort.

- Secure transactions: Use Stripe's powerful security tools to protect customer payment information.

- Convenient user experience: Provide your customers with convenience and ease when placing orders.

- This project is built using Django and Stripe API, providing you with a robust and reliable solution for accepting online payments for your online store.

## Usage

First, create `Item` objects

- Use `/item/{id}` to go to the product page.
- Click the `buy` button to proceed to payment for the goods.

- Use `/buy/{id}` to get the session id.

## Launch

Don't forget to create a virtual environment `venv`

1. Copy the repository:

      ```bash
      git clone https://github.com/geoCrock/Django-Commerce-Hub.git
      ```

2. Go to the project root and create a `venv`:

      ```bash
      cd djangocommercehub
      ```

      ```bash
      python -m venv venv
      ```
      or

      ```bash
      source venv/bin/activate
      ```

4. Install dependencies:

      ```bash
      pip install -r requirements.txt
      ```

5. Create a `.env` file and put your Stripe API keys there:

      ```env
      STRIPE_API_KEY_PRIVATE = "STRIPE_API_KEY_PRIVATE"
    
      STRIPE_API_KEY_PUBLIC = "STRIPE_API_KEY_PUBLIC"
      ```


6. Make migrations and run the project:
   
     ```bash
     python manage.py makemigrations
      ```

     ```bash
     python manage.py migrate
      ```

     ```bash
     python manage.py runserver
      ```
   
7. The application is available at http://127.0.0.0:8000.



## Running via Docker

Make sure the following components are installed on your system:

- Docker
- Docker Compose


1. Copy the repository:

      ```bash
      git clone https://github.com/geoCrock/Django-Commerce-Hub.git
      ```

2. Login to the project root:

      ```bash
      cd djangocommercehub
      ```

3. Create a `.env` file and put your Stripe API keys there:

      ```env
      STRIPE_API_KEY_PRIVATE = "STRIPE_API_KEY_PRIVATE"
    
      STRIPE_API_KEY_PUBLIC = "STRIPE_API_KEY_PUBLIC"
      ```
  
4. Create and run Docker containers:

      ```bash
      docker-compose up --build
      ```
