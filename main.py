# Imports
import webapp2
import os
import jinja2
import lyft_rides
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape = True,
)

class GreetingsPage(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_env.get_template("templates/index.html")
        self.response.write(home_template.render())# Home Page

    def post(self):
        pass # Results Page

app = webapp2.WSGIApplication([
    ('/', GreetingsPage)
], debug=True)
