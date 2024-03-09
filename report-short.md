# Library Management System v2

## Code Block Descriptions

This new_report.md provides a detailed description of each code block in the Library Management System, including the backend requirements, configuration, models, schemas, forms, API endpoints, routes, and frontend components and services. It gives an overview of the purpose and functionality of each file in the project.

### backend/requirements.txt

This file lists the required Python packages and their versions for the backend of the Library Management System. It includes packages such as Flask, Flask-RESTful, Flask-Security-Too, Flask-SQLAlchemy, and others that are necessary for building the application.

### backend/main.py

This is the entry point of the Flask application. It creates an instance of the Flask app using the `create_app()` function from the `app` package and runs the application.

### backend/config.py

This file contains the configuration classes for the Flask application. It defines the `Config` base class and the `LocalDevelopmentConfig` class for local development settings. The configuration includes settings for the database, mail server, security, and other application-specific settings.

### backend/app/\__init__.py

This file is the entry point of the `app` package. It creates the Flask application, initializes extensions (such as the database, migration, security, and admin), and registers blueprints for different routes. It also sets up the user datastore and creates the necessary database tables.

### backend/app/extensions.py

This file defines the Flask extensions used in the application, such as SQLAlchemy for database management, Migrate for database migrations, Flask-Security for authentication and authorization, and others. These extensions are initialized without any specific Flask app instance.

### backend/app/models.py

This file contains the database models for the Library Management System. It defines the `CRUDMixin` class for CRUD operations, and various models such as `Role`, `User`, `Admin`, `Librarian`, `Member`, `Membership`, `Wishlist`, `Collection`, `Genre`, `Author`, `Book`, `BookLoan`, `Purchase`, and `Review`. These models represent the entities in the system and their relationships.

### backend/app/schemas.py

This file defines the Marshmallow schemas for serializing and deserializing the database models. It includes schemas for `Role`, `User`, `Librarian`, `Member`, `Membership`, `Wishlist`, `Collection`, `Genre`, `Author`, `Book`, `BookLoan`, `Purchase`, and `Review`. These schemas are used for data validation and conversion between JSON and Python objects.

### backend/app/forms.py

This file contains the Flask-WTF form classes used in the application. It defines forms for managing books, authors, genres, users, members, and book loans. These forms include fields for inputting and validating data, and they are used in the routes for rendering HTML templates and handling form submissions.

### backend/app/apis/crud.py

This file defines the CRUD API endpoints using Flask-RESTful. It includes a `BaseApi` class that provides generic CRUD operations for database models, and specific API classes for `User`, `Member`, `Librarian`, `Book`, `Genre`, `Author`, and `BookLoan`. The API endpoints allow for retrieving, creating, updating, and deleting records, as well as filtering and sorting the results.

### backend/app/apis/main.py

This file defines the main API endpoints for the application. It includes endpoints for selecting user roles, retrieving book loans by member or book, approving loans, returning loans, and retrieving the currently logged-in user. These endpoints handle specific actions related to the library management system.

### backend/app/routes/crud_api_calls.py

This file contains the routes for making API calls to the CRUD API endpoints. It defines routes for managing books, genres, authors, users, members, and book loans. These routes utilize forms for data input and validation, and they interact with the CRUD API endpoints to perform the corresponding operations.

### backend/app/routes/librarian.py

This file defines the routes for the librarian functionality. It includes routes for the librarian dashboard, displaying users, adding users, editing users, and deleting users. These routes handle the librarian-specific actions and render the corresponding HTML templates.

### backend/app/routes/main.py

This file contains the main routes for the application. It defines the routes for the home page and the role selection page. The role selection route is protected by authentication and handles the selection of user roles (librarian or member) based on the submitted form.

### backend/app/routes/member.py

This file defines the routes for the member functionality. It includes routes for the member dashboard, requesting a book, viewing loans, and returning a book. These routes handle the member-specific actions and interact with the API endpoints to perform the corresponding operations.

### frontend/src/main.js

This is the entry point of the Vue.js frontend application. It creates a new Vue instance, mounts the root component (`App.vue`), and initializes the router and store.

### frontend/src/store.js

This file defines the Vuex store for the frontend application. It includes the state, mutations, actions, and getters related to user authentication and management. The store handles user registration, login, logout, and fetching user data from the backend API.

### frontend/src/App.vue

This is the root component of the Vue.js application. It defines the main template structure, including the navigation menu and the router view component. It also includes styles for the application.

### frontend/src/router/index.js

This file defines the Vue Router configuration for the frontend application. It sets up the routes for different views and components, such as the home page, librarian dashboard, member dashboard, user authentication pages, and book/genre/author management pages.

### frontend/src/services/BookService.js

This file contains the BookService, which is responsible for making API requests related to books. It includes methods for creating, retrieving, updating, and deleting books using the corresponding API endpoints.

### frontend/src/services/BookLoanService.js

This file contains the BookLoanService, which is responsible for making API requests related to book loans. It includes methods for creating, retrieving, updating, deleting, and approving book loans using the corresponding API endpoints.