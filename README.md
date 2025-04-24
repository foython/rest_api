1. login api: http://127.0.0.1:8000/auth/login/
2. user api: http://127.0.0.1:8000/auth/user/
3. product api: http://127.0.0.1:8000/product/api/
4. order api: http://127.0.0.1:8000/orders/api/

order post JSON formet
 {
        "id": 2,
        "customer": 1,
        "status": "ACTIVE",
        "total": 20,
        "order_items": [
            {
                "id": 10,
                "product_id": 4,                
                "quantity": 2
                
            }
        ]
    }
