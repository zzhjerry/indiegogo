# Indiegogo python client

Python wrapper for indiegogo API

##Installation

##Usage

```python
from models import *
from indiegogo.client import Client

client = Client()
client.api_key = '<your api key here>'

result = client.search_campaigns(category='Fashion')

print(result) # see all the result

# get individual fields
result[0].title
result[0].slug
result[0].created_at
result[0].updated_at
result[0].title
result[0].image_types
result[0].currency.iso_num
result[0].collected_funds
result[0].goal
result[0].funding_ends_at
result[0].funding_started_at
result[0].tagline
result[0].funding_days
result[0].funding_type
result[0].baseball_card_image_url
result[0].region_code
result[0].region
result[0].country_code_alpha_2
result[0].country
result[0].city
result[0].contributions_count
result[0].comments_count
result[0].updates_count
result[0].category.name
result[0].forever_funding_active
result[0].perks_available
result[0].team_members[0].name
result[0].latest_updates[0].text
```


##Inspirations

Inspired by helpscout api python wrapper
