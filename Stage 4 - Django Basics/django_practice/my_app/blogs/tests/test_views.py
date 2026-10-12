from django.test import TestCase
from django.urls import reverse

class BlogViewTest(TestCase):
    
    def test_home_view_load_successfully(self):
        """Test blogs home screen response"""
        response = self.client.get(reverse("home"))
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"home.html")
        # self.assertTemplateUsed(response,"my_home.html")
        
     