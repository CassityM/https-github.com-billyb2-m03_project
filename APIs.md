# Item API
Both the `/view_item` and the `/search` API return one or more JSON objects with the following parameters:

- `item_id`: A integer for the unique ID given to each item 
- `name`: The item's name
- `price`: How much the item costs
- `description`: A short description about what the item is

## /view_item
The `/view_item` API returns a single Item JSON object and takes the following parameters:

- `/view_item/[item_id]`
	- Returns a single Item JSON object whos ID matches the item_id given
	- Ex: `/view_item/3`

## /search
The `/search` API returns a list of the Item JSON object and takes the following parameters:

- `/search/[name]`
	- Searches only for items whose name contains the `[name]` parameter
	- Case insensitive
	- Example: /search/bike
- `/search/[name]?price=[price]&price_search_type=[price_search_type]`
	- The `[price]` parameter can be any positive decimal number
	- The `[price_search_type]` parameter has four options
		- `less_than`, finds any items with a price less than or equal to `[price]`
		- `greater_than`, finds any items with a price greater than or equal to `[price]`
		- `equal_to`, finds any items with a pric eequal to `[price]`
		- `range`, finds any prices greater than `[price]`, with an additional parameter `high_price` being required for the upper limit of the price
	- Ex: /search/bike?price_search_type=lower_than&price=50.0 - searches for a bike with a price of less than or equal to $50.00
	- Ex: /search/bike?price_search_type=range&price=50.0&high_price=200.0 - searches for a bike within the price range of $50.00 and $200.00 inclusive

