# LittlelemonAPI project

## Introduction
This is a back-end api project for the final project of Meta APIs course https://www.coursera.org/learn/apis/ 

This project provides API endpoints for the following functions, aiming for the management of Littlelemon resturant:
1. User registration and token generation endpoints 
2. Category and menu-items endpoints
3. User group management endpoints
4. Cart management endpoints 
5. Order management endpoints

This project is currently written in function views, the current code is a little bit messy and the DRY principle is not fully applied.

## Current Users
Admin: (Admin is also a manager)
>Username: admin

>Password: 123

>Token: 7d7f9cb36eb663519d0ea4e9eec003c4a7a300fc

Manager:
>Username: manager1

>Password: lemon@123!

>Token: d49508708b06eaf1a5355222df8b5e0309df0eb3

Customer:
>Username: customer1

>Password: lemon@123!

>Token: a88aaf06a40c65c65685ea7d54b94fa3ece84382

Delivery crew:
>Username: delivery1

>Password: lemon@123!

>Token: 8d5a192946e31cab37e8babc5c7483c10845804f

## Fields needed for some POST methods:
The API routes are working the same as described in https://www.coursera.org/learn/apis/supplement/Ig5me/project-structure-and-api-routes

Here are some notice about the fields needed and accepted type when using POST, PUT or PATCH methods via certain endpoints. They are tested in Insomnia.

```/api/users ```
- **username**: string 
- **email**: email 
- **password**: string

```/api/token/login/ ```
- **username**: string 
- **password**: string

```/api/category```
- **slug**: string 
- **title**: string

```/api/menu-items```
- **title**: string 
- **price**: decimal
- *featured*: (opt.) boolean, default=False
- **category**: integer (you can check the category id via ```/api/category``` endpoint, currently there are 3 categories)

```/api/groups/manager/users```

```/api/groups/delivery-crew/users```
- **username**: string (you can check all the usernames via ```/api/users ``` endpoints with manager token)

```/api/cart/menu-items```
- **menuitem**: integer (you can check teh menuitem id via ```/api/menu-items``` endpoint, currently there are 9 items)
- **quantity**: integer

```/api/orders/{orderId}```
1. Manager: (PATCH is recommended than PUT)
- **delivery_crew**: integer (you can check delivery user_id via ```/api/groups/delivery-crew/users``` endpoint with a manager token)

2. Delivery crew: (PATCH only)
- **status**: boolean
