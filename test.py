import holidayapi
key = '3fea9852-6653-49c3-94f0-ed12cddbac0f'
hapi = holidayapi.v1(key)
holidays = hapi.holidays({
  'country': 'US',
  'year': '2025',
})