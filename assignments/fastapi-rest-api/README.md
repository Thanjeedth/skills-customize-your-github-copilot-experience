# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement RESTful APIs using the FastAPI framework in Python. You will practice creating endpoints, handling requests and responses, and working with data models.

## 📝 Tasks

### 🛠️ Create a Simple FastAPI Application

#### Description
Set up a basic FastAPI application that runs a web server and responds to HTTP requests.

#### Requirements
Completed program should:
- Start a FastAPI server on localhost
- Provide a root endpoint (`/`) that returns a welcome message (e.g., `{"message": "Welcome to FastAPI!"}`)

### 🛠️ Implement CRUD Endpoints for a Resource

#### Description
Add endpoints to manage a collection of items (e.g., books, users, or tasks) with Create, Read, Update, and Delete (CRUD) operations.

#### Requirements
Completed program should:
- Define a Pydantic model for the resource (e.g., Book with `id`, `title`, `author`)
- Implement endpoints:
  - `GET /items` - List all items
  - `POST /items` - Add a new item
  - `GET /items/{item_id}` - Get a single item by ID
  - `PUT /items/{item_id}` - Update an item by ID
  - `DELETE /items/{item_id}` - Delete an item by ID
- Store items in an in-memory list (no database required)

Example:
```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald"
}
```

### 🛠️ (Optional) Add Data Validation and Error Handling

#### Description
Enhance your API with input validation and proper error responses.

#### Requirements
Completed program should:
- Validate input data using Pydantic
- Return appropriate HTTP status codes and error messages for invalid requests
