import yaml
import unittest
import requests
import twitter
from mock import MagicMock, Mock
from pattern.web import Facebook, FacebookResult, NEWS, COMMENTS

from profilegrab import ProfileGrab
from profilegrab.scrapers import get_facebook_text
from profilegrab.scrapers import get_twitter_text


class BaseTestScraper(unittest.TestCase):

    def setUp(self):
        super(BaseTestScraper, self).setUp()
        self.profilegrab      = ProfileGrab(**yaml.load(open('credentials.yaml', 'r')))
        self.twitter          = self.profilegrab.twitter
        self.facebook         = self.profilegrab.facebook
        self.twitteruser      = self.profilegrab.twitter.GetUser(screen_name='c_hack')
        self.twittertimeline  = self.profilegrab.twitter.GetUserTimeline(user_id=self.twitteruser.id)
        self.facebookuser     = self.profilegrab.facebook.search('100000823926890', type=NEWS, count=10)


class TestTwitterScraper(BaseTestScraper):

    def setUp(self):
        super(TestTwitterScraper, self).setUp()
        twitter.Api.GetUser         = MagicMock(return_value=self.twitteruser)
        twitter.Api.GetUserTimeline = MagicMock(return_value=self.twittertimeline)

    def test_numeric_id(self):
        twitter_text = get_twitter_text(1234, self.twitter)
        self.assertIsNotNone(twitter_text)
        self.assertGreater(len(twitter_text), 140)
        twitter.Api.GetUser.assert_called_with(user_id=1234)

    def test_string_id(self):
        twitter_text = get_twitter_text('1234', self.twitter)
        self.assertIsNotNone(twitter_text)
        self.assertGreater(len(twitter_text), 140)
        twitter.Api.GetUser.assert_called_with(user_id=u'1234')

    def test_screen_name(self):
        twitter_text = get_twitter_text('c_hack', self.twitter)
        self.assertIsNotNone(twitter_text)
        self.assertGreater(len(twitter_text), 140)
        twitter.Api.GetUser.assert_called_with(screen_name=u'c_hack')

    def test_screen_name_with_at(self):
        twitter_text = get_twitter_text('@c_hack', self.twitter)
        self.assertIsNotNone(twitter_text)
        self.assertGreater(len(twitter_text), 140)
        twitter.Api.GetUser.assert_called_with(screen_name=u'@c_hack')


class TestFacebookScraper(BaseTestScraper):

    fbreturn = {
           "id": "100000823926890",
           "first_name": "Charlie",
           "gender": "male",
           "last_name": "Hack",
           "locale": "en_US",
           "name": "Charlie Hack",
           "username": "charlie.hack"
        }

    def setUp(self):
        super(TestFacebookScraper, self).setUp()
        Facebook.search = MagicMock(return_value=self.facebookuser)
        FacebookResult = Mock(text='asdf')
        requests.get = MagicMock(return_value=requests.models.Response())
        requests.models.Response.json = MagicMock(return_value=self.fbreturn)

    def test_numeric_id(self):
        facebook_text = get_facebook_text(1234, self.facebook)
        self.assertIsNotNone(facebook_text)
        self.assertGreater(len(facebook_text), 140)
        Facebook.search.assert_called_with(1234, count=100, type='news')

    def test_string_id(self):
        facebook_text = get_facebook_text('1234', self.facebook)
        self.assertIsNotNone(facebook_text)
        self.assertGreater(len(facebook_text), 140)
        Facebook.search.assert_called_with('1234', count=100, type='news')

    def test_screen_name(self):
        facebook_text = get_facebook_text('charlie.hack', self.facebook)
        self.assertIsNotNone(facebook_text)
        self.assertGreater(len(facebook_text), 140)
        Facebook.search.assert_called_with('100000823926890', count=100, type='news')
        requests.get.assert_called_with(url=u'http://graph.facebook.com/charlie.hack')
        requests.models.Response.json.assert_called_once()















