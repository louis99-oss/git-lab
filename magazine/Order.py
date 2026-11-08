import magazine.utils


class Order:
    def __init__(self, products):
        self.products = products

    def total(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        lines = [f"- {product}" for product in self.products]
        lines.append(f"Razem: {magazine.utils.format_price(self.total())}")
        return "\n".join(lines)
