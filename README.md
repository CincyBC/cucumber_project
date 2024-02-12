Added Dockerfile to run the app in a container setting it to run on port 4000. After building the image, the container can be run with the following command:
`docker run -p 4000:4000 -d <image_id>`

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
- inventory
  - GET: list
    - shows inventory for all products with quantities
  - GET: by product id
  - POST create
    - sets name, id and quantity
  - PUT: update
    - update name and quantity (+/-)
