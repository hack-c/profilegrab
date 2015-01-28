import yaml
import unittest
import requests
import twitter
from mock import MagicMock
from pattern.web import Facebook, FacebookResult, NEWS, COMMENTS

from profilegrab import ProfileGrab
from profilegrab.scrapers import get_facebook_text
from profilegrab.scrapers import get_twitter_text


class BaseTestGrab(unittest.TestCase):

    def setUp(self):
        super(BaseTestGrab, self).setUp()
        self.profilegrab      = ProfileGrab(**yaml.load(open('credentials.yaml', 'r')))
        self.twitter          = self.profilegrab.twitter
        self.facebook         = self.profilegrab.facebook
        self.twitteruser      = self.profilegrab.twitter.GetUser(screen_name='c_hack')
        self.twittertimeline  = self.profilegrab.twitter.GetUserTimeline(user_id=self.twitteruser.id)
        self.facebookuser     = self.profilegrab.facebook.search('100000823926890', type=NEWS, count=100)
        twitter.Api.GetUser         = MagicMock(return_value=self.twitteruser)
        twitter.Api.GetUserTimeline = MagicMock(return_value=self.twittertimeline)



class TestGrab(BaseTestGrab):

    def setUp(self):
        super(TestGrab, self).setUp()

    def test_output_keys_consistent(self):
        output = self.profilegrab.grab(twitter_id='c_hack')
        self.assertEqual(output.keys(), ['twitter:c_hack'])










