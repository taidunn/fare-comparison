# Imports
import webapp2
import os
import jinja2

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape = True,
)

class GreetingsPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello world")

app = webapp2.WSGIApplication([
    ('/', GreetingsPage)
], debug=True)
