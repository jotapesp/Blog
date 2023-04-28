from django.test import TestCase

from blog.models import Blogger

# Create your tests here.
class BloggerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blogger.objects.create(name='Flatula', bio='Is happy.')

    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass
    #
    # def test_false_is_false(self):
    #     print("Method: test_false_is_false.")
    #     self.assertFalse(False)
    #
    # def test_false_is_true(self):
    #     print("Method: test_false_is_true.")
    #     self.assertTrue(False)

    def test_name_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_birth_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('birth').verbose_name
        self.assertEqual(field_label, 'birth date')

    def test_name_max_length(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_name(self):
        blogger = Blogger.objects.get(id=1)
        expected_object_name = f'{blogger.name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        self.assertEqual(blogger.get_absolute_url(), 'blogs/bloggers/1')
