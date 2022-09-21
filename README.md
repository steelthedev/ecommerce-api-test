## E-commerce APIs

This is a provision of API that can do some basic e-commerce functions.



### Accounts 

* To register new users:

Request Type => **POST**
<br>
Authentication and permissions => *None*
Endpoint => `127.0.0.1:8000/accounts/signup`
Required parameters => username,email,password

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


