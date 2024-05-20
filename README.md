# Trello Backend API

Welcome to the Trello Backend API project! This project provides the backend API for a Trello-like task management application. It allows users to create, manage, and organize tasks and projects efficiently.

## 🚀 Quick Start

### Requirements

- Python (>=3.6)
- Django (>=2.2)
- Django REST Framework (>=3.12)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/VitthalGund/trello-clone-backend.git
   ```

2. Navigate to the project directory:

   ```bash
   cd trello-backend-api
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv env
   ```

4. Activate the virtual environment:

   - For Unix/macOS:

     ```bash
     source env/bin/activate
     ```

   - For Windows:

     ```bash
     .\env\Scripts\activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

Start the Django development server:

```bash
python manage.py runserver
```

The server will start running at `http://127.0.0.1:8000/`.

## 📖 Documentation

For detailed documentation of API endpoints and usage, please refer to the [API Documentation](api-documentation.md) file.

## 💡 Features

- **User Authentication**: Secure user authentication using JWT tokens.
- **Column and Card Management**: Create, update, and delete columns and cards.
- **Efficient Data Structure for Reordering**: Optimized data structure for efficient reordering of cards within columns.
- **API Endpoints**: Comprehensive API endpoints for adding, editing, and deleting cards.

## 🌐 Usage Examples

To interact with the API endpoints, you can use tools like Postman or curl. Here are some examples:

- **Creating a New User Account**:
  ```bash
  curl -X POST http://localhost:8000/api/accounts/register -d '{"username": "user1", "email": "user1@example.com", "password": "password123", "full_name": "John Doe", "bio": "Short bio about the user", "organization": "Organization name"}' -H 'Content-Type: application/json'
  ```

- **Logging in to an Existing User Account**:
  ```bash
  curl -X POST http://localhost:8000/api/accounts/login -d '{"username": "user1", "password": "password123"}' -H 'Content-Type: application/json'
  ```

- **Creating a New Column**:
  ```bash
  curl -X POST http://localhost:8000/api/core/columns -d '{"title": "New Column"}' -H 'Authorization: Bearer <your-token>' -H 'Content-Type: application/json'
  ```

- **Adding a New Card to a Column**:
  ```bash
  curl -X POST http://localhost:8000/api/core/cards -d '{"title": "New Card", "description": "Description of the card", "column": 1}' -H 'Authorization: Bearer <your-token>' -H 'Content-Type: application/json'
  ```

## 📝 Configuration

The project settings can be modified in the `settings.py` file. You can configure database settings, secret keys, logging, and more.

## 📄 License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.
