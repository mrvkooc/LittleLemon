from django.test import TestCase

from restaurant import models

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = models.MenuItem.objects.create(
            title='Ice cream',
            price=5,
            inventory=100,
        )
        self.assertEqual(str(item), 'Ice cream : 5')
