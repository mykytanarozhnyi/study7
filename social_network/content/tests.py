from django.test import TestCase

from content.models import Post

class PostTests(TestCase):

    def test_of_test(self):
        self.assertTrue(True)

    def test_post_title(self):
        post = Post(text='Test post')
        post.save()
        self.assertEqual(post.title,"No Title")
