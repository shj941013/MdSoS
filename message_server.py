from flask import Flask, request
from twilio import twiml
from transit_stopid_geo import get_geo_loc
from business_search import search_yelp

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    message_body_array = []
    message_body_array = message_body.split()
    # print message_body_array[0]
    # print message_body_array[1]
    # print message_body_array[2]

    cta_query_resp, cta_geo_loc = get_geo_loc(message_body_array[0])
    # keyword = message_body_array[1]
    search_key = "dentist"

    resp1 = twiml.Response()

    if cta_query_resp == 200 and len(cta_geo_loc) > 0:
        reply_lat = cta_geo_loc[0]['latitude']
        reply_lon = cta_geo_loc[0]['longitude']
        res1, res2, res3 = search_yelp(search_key, reply_lat, reply_lon)
        resp1.message('The nearest MDSoS doctors are: %s, %s, %s' %(res1, res2, res3))
    else:
        resp1.message('Invalid stop ID or location, try again.')
    return str(resp1)

if __name__ == '__main__':
    app.run()