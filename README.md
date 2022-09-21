## E-commerce APIs

This is a provision of API that can do some basic e-commerce functions.



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

* To login users:

Request Type => **POST**
<br>

Authentication and permissions => *None*

<br>

Endpoint => `127.0.0.1:8000/accounts/api/v1/token/login`

<br>
 
<p>Required parameters => username,password </p>

<hr>


### Orders