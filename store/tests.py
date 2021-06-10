from django.test import TestCase
from .models import Category
# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='thiller')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0
	#name = models.CharField(max_length = 100)
	#slug = models.SlugField(max_length = 150, unique=True ,db_index=True)
	#icon = models.FileField(upload_to = "category/")
	#create_at = models.DateTimeField(auto_now_add = True)
	#updated_at = models.DateTimeField(auto_now_add = True)
