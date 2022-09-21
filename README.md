## E-commerce APIs

This is a provision of API that can do some basic e-commerce functions.


## Admin details 

Products can be added from the admin 

`username`:**kal**
`password`:**kal**



### Accounts 

* To register new users:

Request Type => **POST**
<br>
Authentication and permissions => *None*

<br>

Endpoint => `127.0.0.1:8000/accounts/signup`

<br>
 
<p>Required parameters => username,email,password </p>

```
data = {
    "username":"",
    "email":"",
    "first_name":"",
    "last_name":"",
    "country":"",
    "phone":"",
    "is_staff:"",
    "password":"",
}
```

<hr>



* To get logged in user:

Request Type => **GET**
<br>
Authentication and permissions => *Token*

<br>

Endpoint => `127.0.0.1:8000/accounts/user`

<br>


<hr>


* To login users:

Request Type => **POST**
<br>

Authentication and permissions => *None*

<br>

Endpoint => `127.0.0.1:8000/accounts/api/v1/token/login`

<br>
 
<p>Required parameters => username,password </p>

<hr>


* To Edit user details:

Request Type => **PATCH**
<br>
Authentication and permissions => *Token*

<br>

Endpoint => `127.0.0.1:8000/accounts/user-edit`

<br>
 
<p>Required parameters => username,email,password,... </p>

```
data = {
    "username":"",
    "email":"",
    "first_name":"",
    "last_name":"",
    "country":"",
    "phone":"",
    "is_staff:"",
    "password":"",
}
```

<hr>


### Orders

* To Create user Orders:

Request Type => **POST**
<br>
Authentication and permissions => *Token*

<br>

Endpoint => `127.0.0.1:8000/orders/create-order`

<hr>

```

    {
    "paid_amount":float(20000),
    "items":[
        {
            "product":product.id
        }
    ]
    }
```
* To get user Orders:

Request Type => **POST**
<br>
Authentication and permissions => *Token*

<br>

Endpoint => `127.0.0.1:8000/orders/get-user-order`

<hr>
