# Recipe Hub

A simple Recipe Management CRUD application built using Python and Django.

## Features

- Add new recipes
- View all recipes
- Retrieve individual recipe details
- Update existing recipes
- Delete recipes

## Recipe Details

Each recipe includes:
- Recipe name
- Ingredients
- Instructions
- Category
- Preparation time (minutes)
- Cooking time (minutes)
- Number of servings
- Created date

## Tech Stack

- Python
- Django
- SQLite
- JSON

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/recipes/add/` | Add a recipe |
| GET | `/recipes/` | View all recipes |
| GET | `/recipes/<id>/` | View recipe details |
| PUT | `/recipes/update/<id>/` | Update a recipe |
| DELETE | `/recipes/delete/<id>/` | Delete a recipe |

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/recipe-hub.git
   ```

2. Navigate to the project directory:

   ```bash
   cd recipe-hub
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **Mac/Linux:**
   ```bash
   source venv/bin/activate
   ```

5. Install Django:

   ```bash
   pip install django
   ```

6. Apply migrations:

   ```bash
   python manage.py migrate
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Testing

API endpoints can be tested using Thunder Client or the VS Code REST Client extension.

