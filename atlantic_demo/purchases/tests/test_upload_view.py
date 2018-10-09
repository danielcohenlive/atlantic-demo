from datetime import datetime

from django.test import TestCase
from django.core.files.base import ContentFile

# Create your tests here.
# Create your tests here.
from ..factories import PurchaseFactory
from ..models import Customer


class TestUploadTransactions(TestCase):
    def test_get_view_renders_a_form(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Please Upload a CSV')
        self.assertContains(response, '<input type="file" name="csv_upload_file"')

    def test_post_creates_new_data(self):
        csv_file = ContentFile('1\tSnake\tPlisken\t123 Fake St.\tAZ\t12345\tnew\t432\tMasthead\t100.12\t2007-04-05T14:30Z')
        csv_file.name = 'csv_file.csv'

        # I would eventually add a self.assertNumQueries here
        response = self.client.post('/', data={'csv_upload_file': csv_file})

        self.assertEqual(response.status_code, 201)

        customer = Customer.objects.get(id=1)
        self.assertEqual(customer.first_name, 'Snake')
        self.assertEqual(customer.last_name, 'Plisken')
        # etc

        self.assertEqual(customer.purchase_set.count(), 1)
        purchase = customer.purchase_set.first()
        self.assertEqual(purchase.status, 'new')
        # etc

        self.assertEqual(purchase.product.name, 'Masthead')
        self.assertEqual(purchase.product.amount, 100.12)

    def test_it_updates_rows_that_already_exist(self):
        purchase = PurchaseFactory(purchase_time=datetime.now())
        csv_file = ContentFile(
            '{}\tSnake\tPlisken\t123 Fake St.\tAZ\t12345\tnew\t{}\tMasthead\t100.12\t{}'.format(
                purchase.customer.id,
                purchase.product.id,
                purchase.purchase_time.isoformat(),
            )
        )
        csv_file.name = 'csv_file.csv'

        # I would eventually add a self.assertNumQueries here
        response = self.client.post('/', data={'csv_upload_file': csv_file})

        self.assertEqual(response.status_code, 201)

        customer = Customer.objects.get(id=1)
        self.assertEqual(customer.first_name, 'Snake')
        self.assertEqual(customer.last_name, 'Plisken')
        # etc

        self.assertEqual(customer.purchase_set.count(), 1)
        purchase = customer.purchase_set.first()
        self.assertEqual(purchase.status, 'new')
        # etc

        self.assertEqual(purchase.product.name, 'Masthead')
        self.assertEqual(purchase.product.amount, 100.12)
