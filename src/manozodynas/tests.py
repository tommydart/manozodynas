# encoding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from manozodynas.testutils import StatefulTesting
from manozodynas.models import Word, Translation


class IndexTestCase(StatefulTesting):
    def test_index_page(self):
        self.open(reverse('index'))
        self.assertStatusCode(200)

class CreateWordTest(StatefulTesting):
    def test_word_create(self):
        self.open(reverse('new_word'))
        self.assertStatusCode(200)
        all_words = Word.objects.all()
        self.assertFalse(all_words.filter(word='testavimas').exists())
        self.selectForm('#CreateWord')
        self.submitForm({
        'word': 'testavimas'
        })
        self.assertStatusCode(302)
        self.assertTrue(all_words.filter(word='testavimas').exists())

    def test_word_translation_create(self):
        word = Word()
        word.word = 'testas'
        word.save()
        self.open(reverse('word_view', args=(word.id, )))
        self.assertStatusCode(200)
        self.selectForm('#NewTranslation')
        self.submitForm({
            'translation': 'testavimas'
        })
        self.assertStatusCode(302)
        self.assertTrue(Translation.objects.filter(translation='testavimas').exists())
class LoginTestCase(StatefulTesting):

    fixtures = ['test_fixture.json']

    def test_login_page(self):
        self.open(reverse('login'))
        self.assertStatusCode(200)

    def test_good_login(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': 'test',
            'password': 'test',
        })
        self.assertStatusCode(302)

    def test_bad_login(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': 'bad',
            'password': 'bad',
        })
        self.assertStatusCode(200)
        self.selectOne('.errorlist')

    def test_no_input(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': '',
            'password': '',
        })
        self.assertStatusCode(200)
        self.selectMany('.errorlist')

    def test_no_username(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': '',
            'password': 'test',
        })
        self.assertStatusCode(200)
        self.selectOne('.errorlist')

    def test_no_password(self):
        self.open(reverse('login'))
        self.selectForm('#login')
        self.submitForm({
            'username': 'test',
            'password': '',
        })
        self.assertStatusCode(200)
        self.selectOne('.errorlist')
