from ecommerce.inventory.models import Product

def test_create_product(single_product):
    new_product=single_product
    get_product=Product.objects.all().first()
    assert new_product.id==get_product.id
