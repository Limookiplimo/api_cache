# Cache Api Responses
Wrote a python script to insert excel data into a postgresql database, and then developed apis to retrieve the data from the database and rendered them on a simple html template. To minimise calls to the database each time an endpoint is hit, I used requests_cache library to cache the api responses.
