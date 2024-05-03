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



### Trello Core API Endpoints

#### Default Route

- **Route**: `GET /api/core`
- **Request Type**: `GET`
- **Description**: Welcome message indicating successful connection to the Trello API.
- **Input Fields**: None
- **Authentication**: Not required
- **Response**: 
  - `200 OK`: Returns a welcome message.
  
- **Example (Thunder Client)**:
  ```json
  {}
  ```

#### Columns

##### List/Create Columns

- **Route**: `GET /api/core/columns/` (List Columns), `POST /api/core/columns/` (Create Column)
- **Request Type**: `GET` (List Columns), `POST` (Create Column)
- **Description**: Endpoint to list all columns or create a new column.
- **Input Fields**: 
  - For `POST` request: 
    - `title` (string, required): Title of the new column.
- **Authentication**: Required (Bearer token)
- **Response**: 
  - `GET`:
    - `200 OK`: Returns a list of columns.
  - `POST`:
    - `201 Created`: Returns the created column.
    - `400 Bad Request`: Invalid input or missing required fields.
  
- **Example (Postman/Thunder Client)**:
  - **GET Request**:
    ```json
    {}
    ```
    - **Headers**:
      ```
      Authorization: Bearer <token>
      ```
  - **POST Request**:
    ```json
    {
      "title": "New Column"
    }
    ```
    - **Headers**:
      ```
      Authorization: Bearer <token>
      ```

##### Retrieve/Update/Delete Column

- **Route**: `GET /api/core/columns/{column_id}/` (Retrieve Column), `PUT /api/core/columns/{column_id}/` (Update Column), `DELETE /api/core/columns/{column_id}/` (Delete Column)
- **Request Type**: `GET` (Retrieve Column), `PUT` (Update Column), `DELETE` (Delete Column)
- **Description**: Endpoint to retrieve, update, or delete a specific column.
- **Input Fields**:
  - For `PUT` request: 
    - `title` (string, optional): Updated title of the column.
- **Authentication**: Required (Bearer token)
- **Response**: 
  - `GET`:
    - `200 OK`: Returns the column details.
  - `PUT`:
    - `200 OK`: Returns the updated column.
    - `400 Bad Request`: Invalid input or missing required fields.
  - `DELETE`:
    - `204 No Content`: Column successfully deleted.
  
- **Example (Thunder Client)**:
  - **GET Request**:
    ```json
    {}
    ```
    - **Headers**:
      ```
      Authorization: Bearer <token>
      ```
  - **PUT Request**:
    ```json
    {
      "title": "Updated Column Title"
    }
    ```
    - **Headers**:
      ```
      Authorization: Bearer <token>
      ```
  - **DELETE Request**:
    ```json
    {}
    ```
    - **Headers**:
      ```
      Authorization: Bearer <token>
      ```

##### Reorder Columns

- **Route**: `POST /api/core/columns/reorder/`
- **Request Type**: `POST`
- **Description**: Endpoint to reorder columns based on user-defined order.
- **Input Fields**:
  - `order` (list of integers, required): List of column IDs in the desired order.
- **Authentication**: Required (Bearer token)
- **Response**: 
  - `200 OK`: Returns the reordered list of columns.
  - `400 Bad Request`: Invalid input or missing required fields.
  
- **Example (Postman/Thunder Client)**:
  ```json
  {
    "order": [3, 1, 2]
  }
  ```
  - **Headers**:
    ```
    Authorization: Bearer <token>
    ```

#### Cards

##### List/Create Cards

- **Route**: `POST /api/core/cards/` (Create Card)
- **Request Type**: `POST`
- **Description**: Endpoint to create a new card.
- **Input Fields**: 
  - `title` (string, required): Title of the new card.
  - `description` (string, optional): Description of the new card.
  - `column` (integer, required): ID of the column to which the card belongs.
- **Authentication**: Required (Bearer token)
- **Response**: 
  - `201 Created`: Returns the created card.
  - `400 Bad Request`: Invalid input or missing required fields.
  
- **Example (Thunder Client)**:
  ```json
  {
    "title": "New Card",
    "description": "Description of the new card.",
    "column": 1
  }
  ```
  - **Headers**:
    ```
    Authorization: Bearer <token>
    ```

##### Retrieve/Update/Delete Card

- **Route**: `GET /api/core/cards/{card_id}/` (Retrieve Card), `PUT /api/core/cards/{card_id}/` (Update Card), `DELETE /api/core/cards/{card_id}/` (Delete Card)
- **Request Type**: `GET` (Retrieve Card), `PUT` (Update Card), `DELETE` (Delete Card)
- **Description**: Endpoint to retrieve, update, or delete a specific card.
- **Input Fields**:
  - For `PUT` request: 
    - `title` (string, optional): Updated title of the card.
    - `description` (string, optional): Updated description of the card.
    - `column` (integer, optional): ID of the column to which the card belongs.
- **Authentication**: Required (Bearer token)
- **Response**: 
  - `GET`:
    - `200 OK`: Returns the card details.
  - `PUT`:
    - `200 OK`: Returns the updated card.
    - `400 Bad Request`: Invalid input or missing required fields.
  - `DELETE`:
    - `204 No Content`: Card successfully deleted.
  
- **Example (Thunder Client)**:
  - **GET Request**:
    ```json
    {}
    ```
    - **Headers**:
      ```
      Authorization: Bearer <token>
      ```
  - **PUT Request**:
    ```json
    {
      "title": "Updated Card Title",
      "description": "Updated description...",
      "column": 2
    }
    ```
    - **Headers**:
      ```
      Authorization: Bearer <token>
      ```


  - **DELETE Request**:
    ```json
    {}
    ```
    - **Headers**:
      ```
      Authorization: Bearer <token>
      ```

##### Move Card

- **Route**: `POST /api/core/cards/move/{card_id}/`
- **Request Type**: `POST`
- **Description**: Endpoint to move a card from one column to another.
- **Input Fields**:
  - `column` (integer, required): ID of the target column.
- **Authentication**: Required (Bearer token)
- **Response**: 
  - `200 OK`: Returns the updated card details.
  - `400 Bad Request`: Invalid input or missing required fields.
  
- **Example (Postman/Thunder Client)**:
  ```json
  {
    "column": 2
  }
  ```
  - **Headers**:
    ```
    Authorization: Bearer <token>
    ```

