# Indiegogo python client

Python wrapper for indiegogo API

##Installation

Caution: installation with `setup.py` is not fully built yet.

##Usage

###Basic

```python
from indiegogo.client import Client

client = Client()
client.api_key = '<your api key here>'

result = client.search_campaigns(category='Fashion')

print(result) # see all the result

# get individual fields of the first result
print( result[0].title )
print( result[0].slug )
print( result[0].created_at )
print( result[0].updated_at )
print( result[0].title )
print( result[0].image_types )
print( result[0].currency.iso_num )
print( result[0].collected_funds )
print( result[0].goal )
print( result[0].funding_ends_at )
print( result[0].funding_started_at )
print( result[0].tagline )
print( result[0].funding_days )
print( result[0].funding_type )
print( result[0].baseball_card_image_url )
print( result[0].region_code )
print( result[0].region )
print( result[0].country_code_alpha_2 )
print( result[0].country )
print( result[0].city )
print( result[0].contributions_count )
print( result[0].comments_count )
print( result[0].updates_count )
print( result[0].category.name )
print( result[0].forever_funding_active )
print( result[0].perks_available )
print( result[0].team_members[0].name )
print( result[0].latest_updates[0].text )
```

###Get continuous pages of the result:

```python
# set up
from indiegogo.client import Client
client = Client
client.api_key = '<your api key here>'

# get search result of page 1
result = client.search_campaign(category="Fashion")
# see the page status
print(result.caller_status)

# get search result of page 2
result = client.search_campaign(category="Fashion")
# see the page status
print(result.caller_status)
```

###Construct different searching criterias

Please see official documentation Indiegogo give out for a full reference
of query choices

```python
# set up
from indiegogo.client import Client
client = Client
client.api_key = '<your api key here>'

# construct query criteria from function arguments
result = client.search_campaign(category="Technology", sort="popular_all", status="open")

# construct query criteria from dictionary
query = {
  "category" : "Technology",
  "sort"     : "popular_all",
  "status"   : "open"
}
result = client.search_campaign(**query)
```


##Reference

###Models

####`Campaign`
Attributes
- `.id` : id of the campaign
- `.slug` : a unique slug field in url
- `.created_at`
- `.updated_at`
- `.title`
- `._image_types` : an instance of `ImageTypes` model
- `._currency` : an instance of `Currency` model
- `.collected_funds`
- `.goal`
- `.funding_ends_at`
- `.funding_started_at`
- `.tagline`
- `.funding_days`
- `.funding_type`
- `.baseball_card_image_url`
- `.region_code`
- `.region`
- `.country_code_alpha_2`
- `.country`
- `.city`
- `.contributions_count`
- `.comments_count`
- `.updates_count`
- `._category` : an instance of `Category` model
- `.forever_funding_active`
- `.perks_available`
- `._team_members` : a list of instance of `TeamMember` model
- `._latest_updates` : a list of instance of `LasestUpdate` model

####`ImageTypes`
Attributes
- `.baseball_card`
- `.small`
- `.medium`
- `.large`
- `.original`

####`Currency`
Attributes
- `.iso_num`
- `.iso_code`
- `.symbol`

####`Category`
Attributes
- `.id`
- `.name`
- `.text`

####`TeamMember`
Attributes
- `.id`
- `.name`
- `.status`
- `.owner`
- `.avatar_url`
- `._factbook` : See the `Factbook` model
- `.account_id`
- `.user_type`

####`Facebook`
Attributes
- `.verified`
- `.friends_count`

####`Account`
- `.id`
- `.firstname`
- `.lastname`
- `.avatar_url`
- `.name`


##Inspirations

Inspired by helpscout api python wrapper
