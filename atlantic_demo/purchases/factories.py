import factory

from .models import Customer, Product, Purchase


class CustomerFactory(factory.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    street_address = factory.Faker('pystr')
    state = factory.Faker('pystr')
    zip = factory.Faker('pyinst')

    class Meta:
        model = Customer


class ProductFactory(factory.DjangoModelFactory):
    name = factory.Faker('pystr')
    amount = factory.Faker('pyfloat')

    class Meta:
        model = Product


class PurchaseFactory(factory.DjangoModelFactory):
    product = factory.SubFactory(ProductFactory)
    customer = factory.SubFactory(CustomerFactory)


    class Meta:
        model = Purchase
