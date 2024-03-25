from django.test import TestCase
from .models import filterTag, template


class filterTagsTestCase(TestCase):

    def setUp(self):
        # print("setUp: Run once for every test method to set up clean data.")
        filterTag.objects.create(name="painting")
        filterTag.objects.create(name="sketching")
        pass

    def test_fetchAll_filterTags(self):
        # set up

        # exercise and verify
        self.assertEqual(2, len(filterTag.objects.all()))


class viewsTest(TestCase):

    def test_view_main(self):
        # set up
        template.objects.create()

        # exercise
        response=self.client.get('/main')

        # verify
        self.assertEqual(200, response.status_code)
        self.assertInHTML('Edit portfolio', response.content.decode())

    def test_view_firstMain(self):
        # set up

        # exercise
        response=self.client.get('/main')

        # verify
        self.assertEqual(200, response.status_code)
        self.assertInHTML('Create your portfolio', response.content.decode())
