
from django.test import TestCase
from .views import get_index
from .products import Subject
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response


class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual(1 + 2, 3)

    def test_adding_something_isnt_equal(self):
        self.assertNotEqual(1 + 2, 4)


class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

def test_home_page_status_code_is_ok(self):
    home_page = self.client.get('/')
    self.assertEquals(home_page.status_code, 200)


def test_check_content_is_correct(self):
    home_page = self.client.get('/')
    self.assertTemplateUsed(home_page, "index.html")
    home_page_template_output = render_to_response("index.html").content
    self.assertEquals(home_page.content, home_page_template_outputfrom django.test import TestCase
from django.shortcuts import render_to_response
from .models import Subject


class SubjectPageTest(TestCase):

    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects':
Subject.objects.all()}).content
        self.assertEquals(subject_page.content, subject_page_template_output)

