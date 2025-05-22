## 📡 API Endpoints to Test

Please use the following endpoints to test the core functionality of this project:

### 1. Menu Endpoint

- **URL**: `http://localhost:8000/restaurant/menu/`
- **Method**: `GET`
- **Description**: Retrieves a list of available menu items.

---

### 2. Single Menu Endpoint

- **URL**: `http://localhost:8000/restaurant/menu/<id>`
- **Method**: `GET`
- **Description**: Retrieves a single menu item

---

### 3. Booking Endpoint

- **URL**: `http://localhost:8000/restaurant/booking/tables/`
- **Method**: `GET`
- **Description**: Retrieves a list of tables booked.

---

### 4. Single Booking Endpoint

- **URL**: `http://localhost:8000/restaurant/booking/tables/<id>`
- **Method**: `GET`
- **Description**: Retrieves a single table booked.

---


### 5. Table Booking Endpoint

- **URL**: `http://localhost:8000/restaurant/booking/tables/`
- **Method**: `POST`
- **Description**: Books a table for a customer.

**Example Request Body**:
```json
{
  "name": "John Doe",
  "date": "2025-05-25",
  "time": "19:00",
  "guests": 4
}
