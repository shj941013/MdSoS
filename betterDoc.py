import requests
import os

def insurance():
    """Show Insurance Information"""
    insurances = {}
    query_params = {'user_key': '363931b37b31af63d168cfee07845ca8',
                    'limit': '10'
                    }

    response = requests.get("https://api.betterdoctor.com/2016-03-01/insurances", params=query_params)
    num_responses = response.json()['meta'].get('total')

    print "number of insurances: ", num_responses

    for num in range(0, num_responses, 100):
        print "num", num
        query_params = {'user_key': '363931b37b31af63d168cfee07845ca8',
                    'skip': str(num),
                    'limit': '100'
                    }
        r_insurance = requests.get("https://api.betterdoctor.com/2016-03-01/insurances", params=query_params).json()

        insurance_plans = r_insurance['data']


        for insurance in insurance_plans:
            insurance_id = insurance.get('plans')[0].get('uid')
            insurance_name = insurance.get('plans')[0].get('name')
            insurances[insurance_id] = insurance_name

    print insurances
    return insurances

insurance()