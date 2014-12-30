```
__________                _____.__.__           ________            ___.    
\______   \_______  _____/ ____\__|  |   ____  /  _____/___________ \_ |__  
 |     ___/\_  __ \/  _ \   __\|  |  | _/ __ \/   \  __\_  __ \__  \ | __ \ 
 |    |     |  | \(  <_> )  |  |  |  |_\  ___/\    \_\  \  | \// __ \| \_\ \
 |____|     |__|   \____/|__|  |__|____/\___  >\______  /__|  (____  /___  /
                                            \/        \/           \/    \/ 
```
by Charlie Hack  
December 2014

Very simple social media scraper for Python. Supply one or more social media uris, get back blocks of text.  

I wrote this little package because all the scraper libraries I found were either way more generalized than what I was looking for, or involved lots of boilerplate. I just wanted to point the scraper to somebody's profile and get the contentful text contained there. Enter ProfileGrab!

Currently ProfileGrab supports Facebook and Twitter.
  
Installation
------------
Cloning the project and running  

`$ python setup.py install`  

should suffice for most users.

Usage
-----
```
    In [1]: from profilegrab import ProfileGrab
    In [2]: pg = ProfileGrab()
    In [3]: charlie_twitter = pg.grab("@c_hack")
    In [4]: charlie_facebook = pg.grab("charlie.hack")
    In [5]: fb_from_id = pg.grab(facebook_id="100000823926890")
    In [6]: tw_from_id = pg.grab(twitter_id="106537958")
    In [7]: multiple = pg.grab("charlie.hack", "KevinDurant", "@drose")
    In [8]: multiple_id = pg.grab(facebook_id=["100000823926890", "81781281654"])
```
You'll get back a python dict in the format  

```
{
	"twitter:@c_hack": u"Check out this cool link! www.example.com [...]",
	"facebook:charlie.hack": u"Today went positively swimmingly [...]",
	[...]
}
```



