import requests

cta_url = 'http://data.cityofchicago.org/resource/793i-qyz3.json?stop_id='
ERR = "Sorry, we did not find a CTA bus stop location with that term, try again."


def get_geo_loc(stp_id):
    cta_url_query = cta_url + str(stp_id)
    response = requests.get(cta_url_query)
    #print response.status_code
    resp_json = response.json()
    return response.status_code, resp_json


ret_code, ret_content = get_geo_loc("14145")

if ret_code == 200:
    print ret_content[0]['latitude']
    print ret_content[0]['longitude']
else:
    print "got error."
