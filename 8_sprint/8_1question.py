"""1 question 8 sprint"""
import unittest


class Product:
    def __init__(self, name: str, price: float, count: int):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    def __init__(self, products=None):
        if products:
            self.products = products
        else:
            self.products = []

    def add_product(self, product: Product):
        self.products.append(product)
        return self.products

    def discount_price(self, product: Product):
        if product.count > 20:
            return product.price * product.count * 0.5
        elif product.count == 20:
            return product.price * product.count * 0.7
        elif product.count >= 10:
            return product.price * product.count * 0.8
        elif product.count >= 7:
            return product.price * product.count * 0.9
        elif product.count >= 5:
            return product.price * product.count * 0.95
        else:
            return product.price * product.count

    def get_total_price(self):
        total_price = sum(self.discount_price(product) for product in self.products)
        return total_price


class CartTest(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()

    def test_add_product(self):
        self.assertTrue(self.cart.add_product(Product("tea", 10, 15)))

    def test_not_discount_price(self):
        for count in range(1, 5):
            with self.subTest(count=count):
                self.assertEqual(self.cart.discount_price(Product("test", 10, count)), 10*count)

    def test_discount_price_5_percent(self):
        for count in range(5, 7):
            with self.subTest(count=count):
                self.assertEqual(self.cart.discount_price(Product("test", 10, count)), 10*count*0.95)

    def test_discount_price_10_percent(self):
        for count in range(7, 10):
            with self.subTest(count=count):
                self.assertEqual(self.cart.discount_price(Product("test", 10, count)), 10 * count * 0.90)

    def test_discount_price_20_percent(self):
        for count in range(10, 19):
            with self.subTest(count=count):
                self.assertEqual(self.cart.discount_price(Product("test", 10, count)), 10 * count * 0.80)

    def test_discount_price_30_percent(self):
        count = 20
        self.assertEqual(self.cart.discount_price(Product("test", 10, count)), 10 * count * 0.70)

    def test_discount_price_50_percent(self):
        count = 21
        self.assertEqual(self.cart.discount_price(Product("test", 10, count)), 10 * count * 0.50)

    def test_get_total_price(self):
        self.cart.products = [Product("test", 10, 2), Product("test1", 10, 5), Product("test1", 10, 20)]
        self.assertEqual(self.cart.get_total_price(), 207.5)

    def tearDown(self) -> None:
        self.cart = None


if __name__ == '__main__':
    products = (Product('p1', 10, 4),
                Product('p2', 100, 5),
                Product('p3', 200, 6),
                Product('p4', 300, 7),
                Product('p5', 400, 9),
                Product('p6', 500, 10),
                Product('p7', 1000, 20))
    cart = Cart(products)
    print(cart.get_total_price())
    unittest.main()
