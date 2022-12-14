from decimal import Decimal
from django.db import transaction
from django.db.models.aggregates import Count
from rest_framework import serializers
from .models import Cart, CartItem, Customer, Order, OrderItem, Product, Collection, Review

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']
        read_only_fields = ['product_count']
        
    product_count = serializers.SerializerMethodField(method_name='collection_products')
    
    def collection_products(self, collection: Collection):
        return collection.product_set.count()
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'description', 'inventory', 'unit_price', 'price_with_tax', 'collection']
    
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']
        
    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)


class SimpleProductSeiralzier(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']
    
    
class CartItemSerialzier(serializers.ModelSerializer):
    product = SimpleProductSeiralzier()
    
    total_price = serializers.SerializerMethodField(method_name='cal_total_price')
    
    def cal_total_price(self, cartitem: CartItem):
        return cartitem.product.unit_price * cartitem.quantity
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']
        
    
class CartSeriazlier(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerialzier(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='cal_total_price')
    def cal_total_price(self, cart: Cart):
        return sum([(item.product.unit_price * item.quantity) for item in cart.items.all()])

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']
        

class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    
    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('No product with the given ID was found.')
        return value
    
    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        
        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
            
        return self.instance
    
    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']
        
        
class UpdateCartItemSeriazlier(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']
        

class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'phone', 'membership', 'birth_date']
        
        
class OrderItemsSerializer(serializers.ModelSerializer):
    product = SimpleProductSeiralzier()
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'unit_price', 'quantity']
        
        
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemsSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'customer', 'placed_at', 'payment_status', 'items']
        
        
class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    
    def save(self, **kwargs):
        with transaction.atomic():    
            cart_id = self.validated_data['cart_id']
            
            (customer, created) = Customer.objects.get_or_create(user_id=self.context['user_id'])
            order = Order.objects.create(customer=customer)
            
            cart_items = CartItem.objects.select_related('product').filter(cart_id=cart_id)
            
            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    unit_price=item.product.unit_price,
                    quantity=item.quantity
                ) for item in cart_items
            ]
            
            OrderItem.objects.bulk_create(order_items)
            
            Cart.objects.filter(pk=cart_id).delete()