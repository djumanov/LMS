# Learning Management System Backend

This README provides an overview of the backend for a Learning Management System (LMS) built using the Django framework. The LMS backend serves as the core component responsible for managing courses, user authentication, enrollment, and other essential functionalities.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [API Endpoints](#api-endpoints)
3. [Authentication](#authentication)

## Prerequisites

Before getting started, make sure you have the following prerequisites installed on your development environment:

- Python 3.9
- Django==4.2.7
- djangorestframework==3.14.0

## API Endpoints

The LMS backend provides a set of API endpoints for managing courses, users, enrollments, and more. You can explore the API documentation by accessing the `/api/docs/` endpoint in your browser after running the server.

## Authentication

The backend includes authentication mechanisms, and it can be extended to support various authentication methods, including token-based authentication, OAuth, or social logins.

The default authentication method used in this project is token-based authentication. Users can obtain an access token by providing valid credentials (username and password) and use this token to authenticate subsequent API requests.
