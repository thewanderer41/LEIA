import json
import sqlite3
import urllib
import urllib2

url_params = {}
url_params['type'] = 'restaurant'
url_params['where'] = 'Troy,NY'
url_params['publisher'] = 'test'
url_params['format'] = 'json'
url_params['rpp'] = '5'

host = 'api.citygridmedia.com/content/places/v2'
where_path = '/search/where'
detail_path = '/detail'
encoded_params = urllib.urlencode(url_params)

url = 'http://%s%s?%s' %(host,where_path,encoded_params)
print 'URL: %s' % (url,)

conn = urllib2.urlopen(url, None)
response = json.loads(conn.read())
conn.close()

conn = sqlite3.connect('LEIA.db')
c = conn.cursor()

locations = response['results']['locations']
for restaurant in locations:
	address = restaurant['address']
	c.execute('''insert into location values(NULL, ?, ?, ?, ?, ?, ?)''', (address['city'], address['postal_code'], address['state'], address['street'], restaurant['latitude'], restaurant['longitude']))
	c.execute('''insert into restaurant values(NULL, ?, ?, last_insert_rowid(), ?, ?)''', (restaurant['name'], restaurant['rating'], restaurant['phone_number'], restaurant['business_operation_status']))

c.execute('''select * from location''')
print 'locations:'
for i in c:
	print "  "+str(i)
print ''

c.execute('''select * from restaurant''')
print 'restaurants:'
for i in c:
	print "  "+str(i)
print ''

conn.commit()
conn.close()
#print json.dumps(response, sort_keys=True, indent=2)
