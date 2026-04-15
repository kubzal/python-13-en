import csv
from datetime import datetime

class Order:
    def __init__(self, order_id, product_name, quantity, price, buyer_name, phone, email):
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.buyer_name = buyer_name
        self.phone = phone
        self.email = email

    def process_order(self):
        print(f"Processing order #{self.order_id} for {self.quantity} of {self.product_name}.")
        self.status = "PROCESSED"


class PhysicalProduct(Order):
    def __init__(self, order_id, product_name, quantity, price, buyer_name, phone, email, shipping_address):
        super().__init__(order_id, product_name, quantity, price, buyer_name, phone, email)
        self.shipping_address = shipping_address

    def process_order(self):
        super().process_order()
        self.status = "SHIPPED_TO_ADDRESS"
        print(f"Shipping to: {self.shipping_address}")


class DigitalProduct(Order):
    def __init__(self, order_id, product_name, quantity, price, buyer_name, phone, email, download_link):
        super().__init__(order_id, product_name, quantity, price, buyer_name, phone, email)
        self.download_link = download_link

    def process_order(self):
        super().process_order()
        self.status = "EMAIL_SENT"
        print(f"Download link: {self.download_link}")


class SubscriptionProduct(DigitalProduct):
    def __init__(self, order_id, product_name, quantity, price, buyer_name, phone, email, download_link, subscription_duration):
        super().__init__(order_id, product_name, quantity, price, buyer_name, phone, email, download_link)
        self.subscription_duration = subscription_duration

    def process_order(self):
        super().process_order()
        print(f"Subscription for {self.subscription_duration} month(s)")


class OrdersHandler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.orders = self.load_orders()

    def load_orders(self):
        orders = []
        with open(self.file_name, mode="r") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                order = self.create_order(row)
                if order:
                    orders.append(order)
        return orders

    def create_order(self, row):
        try:
            order_id = int(row["Order ID"])
            product_name = row["Product Name"]
            quantity = int(row["Quantity"])
            price = float(row["Price"])
            buyer_name = row["Buyer Name"]
            phone = row["Phone"]
            email = row["Email"]
            shipping_address = row["Shipping Address"]
            order_type = row["Order Type"]
            additional_info = row["Additional Info"]
        except KeyError as e:
            print(f"Error: Some field in the file is missing: {e}")
            exit()

        if order_type == "Physical":
            return PhysicalProduct(
                order_id,
                product_name,
                quantity,
                price,
                buyer_name,
                phone,
                email,
                shipping_address
            )

        elif order_type == "Digital":
            download_link = additional_info
            return DigitalProduct(
                order_id,
                product_name,
                quantity,
                price,
                buyer_name,
                phone,
                email,
                download_link
            )


        elif order_type == "Subscription":
            download_link, subscription_duration = additional_info.split(" - ")
            return SubscriptionProduct(
                order_id,
                product_name,
                quantity,
                price,
                buyer_name,
                phone,
                email,
                download_link,
                subscription_duration
            )

        return None

    def __iter__(self):
        return iter(self.orders)

    def daily_report(self):
        total_physical = 0
        total_digital = 0
        total_subscription = 0
        total_revenue = 0.0

        for order in self.orders:
            if order.status == "SHIPPED_TO_ADDRESS":
                total_physical += order.quantity

            elif order.status == "EMAIL_SENT":
                if isinstance(order, SubscriptionProduct):
                    total_subscription += order.quantity
                else:
                    total_digital += order.quantity
            total_revenue += order.quantity * order.price

            report_file_name = f"daily_report_{datetime.now().strftime('%Y-%m-%d')}.csv"
            with open(report_file_name, mode="w", newline="") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(
                    [
                        "Total Physical Product Shipped",
                        "Total Digital Product Sent",
                        "Total Subscription Activated",
                        "Total Revenue",
                    ]
                )
                writer.writerow(
                    [
                        total_physical,
                        total_digital,
                        total_subscription,
                        f"${total_revenue:.2f}"
                    ]
                )
            print(f"Daily report saved to {report_file_name}")
            print(f"Summary:\n"
                  f"\t - Physical: {total_physical}\n"
                  f"\t - Digital: {total_digital}\n"
                  f"\t - Subscription: {total_subscription}\n"
                  f"\t - Revenue: ${total_revenue:.2f}")

if __name__ == "__main__":
    # Create OrdersHandler and load all the orders
    orders_handler = OrdersHandler("orders.csv")

    # Process all the orders (call .process_order() method for each)
    for order in orders_handler:
        order.process_order()
        print()

    # Create a report
    orders_handler.daily_report()