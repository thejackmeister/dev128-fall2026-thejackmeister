# Starting file for Lab 3 - product_viewer.py
# Include your name, class, and date in the assignment comment header

#Jack Bull
#Dev 128
#10/25/26

from objects import Product, Media, Book, Movie, Album

def show_products(products):
    print("PRODUCTS")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.getDescription()}")
    print()

def show_product(product):
    w=18
    print("PRODUCT DATA")
    print(f"{'Name:':{w}}{product.name}")
    if isinstance(product, Book):
        print(f"{'Author:':{w}}{product.author}")
    if isinstance(product, Movie):
        print(f"{'Year:':{w}}{product.year}")
    # add the Album class to the display
    if isinstance(product, Album):
        print(f"{'Artist:':{w}}{product.artist}")
    # prints the format attribute from the Media class
    if isinstance(product, Media):
        print(f"{'Format:':{w}}{product.format}")
    print(f"{'Discount price:':{w}}{product.getDiscountPrice():.2f}")
    print()

def main():
    print("The Product Viewer program")
    print()

    # store "DVD" as the format attribute for Movie, add "Hardcover" as a format attribute for Book, add the Album to the products list
    products = (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
                Book("The Big Short", 15.95, 34, "Hardcover", "Michael Lewis"),
                Movie("The Holy Grail", 14.99, 68, "DVD", 1975),
                Album("Rubber Soul", 20, 50, "CD", "The Beatles"),
                Movie("The Secret Life Of Walter Mitty", 15, 25, "VHS", 2013),
                Album("Paradise", 22, 10, "Vinyl", "Lana Del Rey"))
    
    show_products(products)

    choice = "y"
    while choice.lower() == "y":
        number = int(input("Enter product number: "))
        print()

        product = products[number-1]
        show_product(product)

        choice = input("View another product? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()
