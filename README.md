Added Dockerfile to run the app in a container setting it to run on port 4000. After building the image, the container can be run with the following command:
`docker run -p 4000:4000 -d <image_id>`

I have also added a docker-compose file to run the app and the database together. The app is set to run on port 4000 and the database on port 5432. The app is set to wait for the database to be ready before starting. The app can be run with the following command: `docker-compose --env-file .env up`

Here is an example of the .env file:

````POSTGRES_USER='cucumber'
POSTGRES_PASSWORD='admingres'
POSTGRES_DB='cucumber'
PGDATA='/data/postgres-cucumber'```

I have also added a separate Dockerfile_behave and Dockerfile_pytest if you want to run those tests separately. They are all set up to run upon a merge to the main branch or PR to the main branch.

ENDPOINTS

- orders
  - POST create
    - sets basic info about the order: customer name, address, list of product ids, quantities and status
  - PUT update
    - change information about the order
    - used to fill order:
      - update product status to "filled" will decrement stock
      - once all products are "filled" order is marked as completed
      - NOTE: we should talk about the statuses
  - GET by id
    - shows order details
- inventory
  - GET: list
    - shows inventory for all products with quantities
  - GET: by product id
  - POST create
    - sets name, id and quantity
  - PUT: update
    - update name and quantity (+/-)
````
