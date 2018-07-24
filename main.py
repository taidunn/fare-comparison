# Imports
import webapp2
import os
import jinja2
import lyft_rides
import uber
from uber_rides.session import Session as uSession
from uber_rides.client import UberRidesClient
import lyft
from lyft_rides.auth import ClientCredentialGrant
from lyft_rides.session import Session as lSession
from lyft_rides.client import LyftRidesClient

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape = True,
)

def get_uber_estimate():
    # This is currently giving a 500 error, but should be working
    # Ultimately, coordinates would be passed into this function to get an estimate, perhaps
    uber_session = uSession(server_token=uber.server_token)
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

def get_lyft_estimate():
    auth_flow = ClientCredentialGrant(
        lyft.client_id,
        lyft.client_secret,
        ['public']
    )

    session = auth_flow.get_session()
    client = LyftRidesClient(session)
    response = client.get_ride_types(37.7833, -122.4167)
    ride_types = response.json.get('ride_types')
    return ride_types

class GreetingsPage(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_env.get_template("templates/index.html")
        self.response.write(home_template.render())# Home Page
        try:
            print get_uber_estimate()
            print get_lyft_estimate()
        except Exception as e:
            print e

    def post(self):
        result_template = jinja_env.get_template("templates/results.html")
        self.response.write(result_template.render())# Home Page

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        results_page = jinja_env.get_template('templates/results.html')
        self.response.write(results_page.render())

class TestPage(webapp2.RequestHandler):
    def get(self):
        test_template = jinja_env.get_template("templates/api-test.html")
        self.response.write(test_template.render())

app = webapp2.WSGIApplication([
    ('/', GreetingsPage),
    ("/test", TestPage),
    ('/results', ResultsPage)
], debug=True)
