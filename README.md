# HouseshareMap

Issue:
- Very hard to find share house in gumtree.
- Lack of filter in realestate map view

Solution:
- Interactive map interface with price message popup
- On click, navigate to the item.
Good example can be Airbnb: https://www.airbnb.com.au/s/Sydney--Australia/homes?adults=1&tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Sydney%2C%20New%20South%20Wales%2C%20Australia&ne_lat=-33.86191500906213&ne_lng=151.22262497634887&sw_lat=-33.889884815866615&sw_lng=151.1787225791931&zoom=15&search_by_map=true&search_type=unknown

Approach:
1. Web crawler to get
- Name
- Address
- Price

2. Get location coordinates based on address

3. Put the markers based on address

4. Good?

# Learning Process
- 14/08/2020
Found AirMapView[https://airbnb.io/projects/airmapview/]. Can this be added to web dev (react)?
Well might not. it focuses on Android dev. Lets see if I can scafold the website.
Let's start with web crawling than.
