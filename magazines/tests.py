from django.test import TestCase
from django.shortcuts import render_to_response
from .models import Magazine


class MagazinePageTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('admin@example.com', 'admin@example.com', 'pa55w0rd')
        #adds user to database as link to magazines requires login, so original test would not run


    def test_check_content_is_correct(self):
        self.client.login(username - 'admin@example.com', password = 'pa55w0rd')
        magazine_page = self.client.get('/magazines/')
        self.assertTemplateUsed(magazine_page, "magazines.magazines.html")
        magazines_page_template_output = render_to_response("magazines/magazines.html",{'magazines': Magazine.objects.all()}).content
        self.assertEquals(magazine_page.content, magazines_page_template_output)


#Note: this test will not work unless you amend the IF statement "login" portion of base.html.