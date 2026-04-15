# ### Task: Order Management System for an Online Store

# Your task is to write a Python program that simulates an order management
# system for an online store. The program will read order data from a CSV file,
# process the orders, and create a daily report with information about the
# number of processed products and profits.

# #### Requirements:
# 1. **CSV File**: Orders in the CSV file use a semicolon (`;`) as the
#    separator. The file contains the following columns:
#    - `Order ID`: Unique order number
#    - `Product Name`: Product name
#    - `Quantity`: Number of ordered products
#    - `Price`: Unit price of the product
#    - `Order Type`: Order type (can be `Physical`, `Digital`, or `Subscription`)
#    - `Buyer Name`: Buyer's first and last name
#    - `Phone`: Buyer's phone number
#    - `Email`: Buyer's email address
#    - `Shipping Address`: Shipping address (for physical products)
#    - `Additional Info`: Additional information, e.g. download link or
#      subscription duration.

# 2. **Product Classes**:
#    - `Order` class: base class representing a generic order. Each order
#      should have attributes such as `order_id`, `product_name`, `quantity`,
#      `price`, `buyer_name`, `phone`, `email`, and `status`, which defaults
#      to `PENDING`.
#    - Derived classes:
#      - `PhysicalProduct`: inherits from `Order`, additionally has a
#        `shipping_address` attribute and changes status to
#        `SHIPPED_TO_ADDRESS` after processing.
#      - `DigitalProduct`: inherits from `Order`, additionally has a
#        `download_link` attribute and changes status to `EMAIL_SENT`
#        after processing.
#      - `SubscriptionProduct`: inherits from `DigitalProduct`, additionally
#        has a `subscription_duration` attribute (subscription length).

# 3. **Order Processing**:
#    - Each order should have a `process_order` method that changes the order
#      status and prints the relevant information (e.g. shipping address or
#      download link).

# 4. **Report Generation**:
#    - The `OrdersHandler` class should be iterable, and its `daily_report`
#      method should generate a CSV file with information about:
#      - The number of shipped physical products, digital products, and
#        activated subscriptions.
#      - Total revenue from all orders.
#    - The report file should be saved with a name containing today's date,
#      e.g. `daily_report_2024-10-16.csv`.

# 5. **Sample Data**:
#    - The CSV file should contain approximately 15 sample orders, with
#      different product types and Polish customer data.