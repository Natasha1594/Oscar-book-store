from django.test import TestCase
from .models import Category
# Create your tests here.
class CategoryTest(TestCase):
    def setUp(self):
        self.Category = Category(name='Thiller')
        self.Category.save_category()
    def test_instance(self):
        self.assertTrue(isinstance(self.Category,Category))
	#name = models.CharField(max_length = 100)
	#slug = models.SlugField(max_length = 150, unique=True ,db_index=True)
	#icon = models.FileField(upload_to = "category/")
	#create_at = models.DateTimeField(auto_now_add = True)
	#updated_at = models.DateTimeField(auto_now_add = True)
