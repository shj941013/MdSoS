from yelpapi import YelpAPI

yelp_api = YelpAPI('w0Tplfadr2wTECOfR51acQ', 'qRLjgpc5UsdiDKSUvMuYJ9PUDLyvCGby7ncE8Yar6BhPiQXI22B8OeyAysB7hlk6')


def search_yelp(keyword, lat, lon):

    response_biz = yelp_api.search_query(term=keyword, latitude=lat, longitude=lon, sort_by='distance', limit=3)

    res1yelp = response_biz['businesses'][0]['name'] + ', ' + response_biz['businesses'][0]['display_phone']
    res2yelp = response_biz['businesses'][1]['name'] + ', ' + response_biz['businesses'][1]['display_phone']
    res3yelp = response_biz['businesses'][2]['name'] + ', ' + response_biz['businesses'][2]['display_phone']

    return res1yelp, res2yelp, res3yelp


res1, res2, res3 = search_yelp("dentist","41.981962","-87.808408")
print res1
print res2
print res3

