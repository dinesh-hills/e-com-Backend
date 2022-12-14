from random import randint
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(0.01, 0.02)
    
    @task(3)
    def viewing_products(self):
        collection_id = randint(2, 6)
        self.client.get(f'/store/products/?collection_id={collection_id}', name='/store/products')


    @task(5)
    def view_product(self):
        product_id = randint(1,1000)
        self.client.get(f'/store/products/{product_id}', name='/store/products/:id')


    @task(2)
    def add_to_cart(self):
        product_id = randint(1, 15)
        response =  self.client.post(
            f'/store/carts/{self.cart_id}/items/', 
            name='/store/cart/items',
            json={'product_id': product_id, 'quantity':1}
        )

    def on_start(self):
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result['id']