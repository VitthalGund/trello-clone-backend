## 📖 API Documentation - Accounts App

Welcome to the API documentation for the accounts endpoints in the Trello Backend API. This API provides endpoints for user authentication and management.

### Authentication Endpoints

#### Register User

- **Route**: `POST /api/accounts/register`
- **Request Type**: `POST`
- **Description**: Register a new user account.
- **Input Fields**:
  - `username` (string): User's username.
  - `email` (string): User's email address.
  - `password` (string): User's password.
  - `full_name` (string, optional): User's full name.
  - `avatar` (file, optional): User's avatar image.
  - `bio` (string, optional): User's biography.
  - `organization` (string, optional): User's organization.
- **Response**: 
  - `201 Created`: User account created successfully.
  - `400 Bad Request`: Invalid input or missing required fields.
  
- **Example (Postman/Thunder Client)**:
  ```json
  {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "password123",
    "full_name": "John Doe",
    "avatar": "<file>",
    "bio": "Lorem ipsum dolor sit amet...",
    "organization": "Example Inc."
  }
  ```

#### Login User

- **Route**: `POST /api/accounts/login`
- **Request Type**: `POST`
- **Description**: Log in an existing user.
- **Input Fields**:
  - `username` (string): User's username.
  - `password` (string): User's password.
  
- **Response**: 
  - `200 OK`: Successful login, returns JWT tokens.
  - `400 Bad Request`: Invalid username or password.
  
- **Example (Thunder Client)**:
  ```json
  {
    "username": "john_doe",
    "password": "password123"
  }
  ```

#### Refresh Token

- **Route**: `POST /api/accounts/refresh`
- **Request Type**: `POST`
- **Description**: Refresh the access token.
- **Input Fields**:
  - `refresh_token` (string): Refresh token obtained during login.
  
- **Response**: 
  - `200 OK`: New access token generated successfully.
  - `401 Unauthorized`: Invalid refresh token.

#### Logout User

- **Route**: `POST /api/accounts/logout`
- **Request Type**: `POST`
- **Description**: Log out the currently authenticated user.
- **Input Fields**: None
- **Authentication**: Required (Bearer token)
- **Response**: 
  - `204 No Content`: User successfully logged out.
  - `401 Unauthorized`: User not authenticated.
  
- **Example (Thunder Client)**:
  ```json
  {}
  ```
  - **Headers**:
    ```
    Authorization: Bearer <token>
    ```

#### Update Profile

- **Route**: `PUT /api/accounts/profile`
- **Request Type**: `PUT`
- **Description**: Update the profile information of the currently authenticated user.
- **Input Fields**:
  - `full_name` (string, optional): User's full name.
  - `avatar` (file, optional): User's avatar image.
  - `bio` (string, optional): User's biography.
  - `organization` (string, optional): User's organization.
- **Authentication**: Required (Bearer token)
- **Response**: 
  - `200 OK`: Profile updated successfully.
  - `400 Bad Request`: Invalid input or missing required fields.
  - `401 Unauthorized`: User not authenticated.
  
- **Example (Postman/Thunder Client)**:
  ```json
  {
    "full_name": "John Doe",
    "avatar": "<file>",
    "bio": "Updated biography...",
    "organization": "New Organization Inc."
  }
  ```
  - **Headers**:
    ```
    Authorization: Bearer <token>
    ```

#### Get User Info

- **Route**: `GET /api/accounts/user/{username}/`
- **Request Type**: `GET`
- **Description**: Get the profile information of a specific user.
- **Input Fields**: None
- **Authentication**: Optional (Bearer token)
- **Response**: 
  - `200 OK`: Returns the user's profile information.
  - `404 Not Found`: User not found.
  
- **Example (Thunder Client)**:
  ```json
  {}
  ```
  - **Headers** (optional):
    ```
    Authorization: Bearer <token>
    ```
