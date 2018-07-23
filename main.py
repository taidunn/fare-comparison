# Imports
import webapp2
import os
import jinja2
import lyft_rides
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import uber

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape = True,
)

def get_uber_estimate():
    # This is currently giving a 500 error, but should be working
    # Ultimately, coordinates would be passed into this function to get an estimate, perhaps
    uber_session = Session(server_token=uber.server_token)
    uber_client = UberRidesClient(uber_session)
    uber_response = uber_client.get_price_estimates(
        start_latitude=37.770,
        start_longitude=-122.411,
        end_latitude=37.791,
        end_longitude=-122.405,
        seat_count=2
    )
    estimate = uber_response.json.get('prices')
    return estimate

class GreetingsPage(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_env.get_template("templates/index.html")
        self.response.write(home_template.render())# Home Page

    def post(self):
        pass # Results Page

app = webapp2.WSGIApplication([
    ('/', GreetingsPage)
], debug=True)
