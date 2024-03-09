

Library Management System v1 
It is a multi-user app (one required librarian and other general users/students)
- Used for issuing e-books to users
- User can request, read, return e-books
- Librarian can add new sections/e-books, issue/revoke access for a book.

Each Section may have: ID, Name, Date created, Description
Each book will have: ID, Name, Content, Author(s), Date issued, Return date.
Every section can have a number of books.
System will automatically show recently added sections/books or based on certain rating
Base requirements:Librarian’s Dashboard, General User Profile, Section Management, Book Management, Search functionality for section/e-books

General User functionalities: 
- Login/Register
- View all the existing Sections/e-books
- Request/Return Books (content)
- A user can request for a maximum of 5 e-books 
- A user can access a book for a specific period of time (say N hours/days/weeks).For e.g. if N = 7 days, user can return a book before 7 days. If he/she fails to do so, the access for that will be automatically revoked after 7 days.
- User can give feedback for an e-book

Librarian functionalities
- Issue one or multiple e-book(s) to a user
- Revoke access for one or multiple e-book(s) from a user. Storage should handle multiple languages - usually UTF-8 encoding is sufficient for this
- Edit an existing section/e-book. Change content, author name,  no. of pages/volume etc.
- Remove an existing section/e-book
- Assign a book to a particular section
- A librarian can monitor current status of each e-book and the user it is issued to
- Available e-books in the Library

Search for e-books/sections
- Ability to search for a particular section.
- Ability to search e-books based on section, author etc

Download e-books as PDF for a price 
- APIs for interaction with sections and books. CRUD on e-books, Additional APIs for getting the creating graphs for librarian dashboard
- Validation:All form inputs fields - text, numbers, dates etc. with suitable messages.Backend validation before storing / selecting from database


Library Management System v2
Core Functionality:
This will be graded
Base requirements:
- Librarian Dashboard
- General User signup and login (using RBAC)
- Mandatory Librarian Login (using RBAC)
- General User Profile
- Section Management
- e-book Management
- Search functionality for sections/e-books
Backend Jobs
- Export Jobs
- Reporting Jobs
- Alert Jobs
Backend Performance


Core - Librarian and User Login
User and admin should be authenticated using username or email and password
Use Flask Security or JWT based Token Based Authentication only
Registration form for General User is required.
New librarian cannot be created.
Suitable model for general user (model that stores all the type of users and
differentiates them correctly based on their role)
The application should have only one librarian.

Core - General User functionalities
Login/Register
View all the existing Sections/e-books
Request/Return Books (content)
A user can request for a maximum of 5 e-books
A user can access a book for a specific period of time (say N hours/days/weeks).
For e.g. if N = 7 days, user can return a book before 7 days. If he/she fails to do so, the access
for that will be automatically revoked after 7 days.
User can give feedback for an e-book

Core - Librarian functionalities
Issue one or multiple e-book(s) to a user
Revoke access for one or multiple e-book(s) from a user
Edit an existing section/e-book
Storage should handle multiple languages - usually UTF-8 encoding is sufficient for this
Change content, author name, no. of pages/volume etc.
Remove an existing section/e-book
Assign a book to a particular section
A librarian can monitor current status of each e-book and the user it is issued to
Available e-books in the Library


Core - Search for sections/e-books
Ability to search for a particular section.
Ability to search e-books based on section, author etc.

Core - Daily Reminder Jobs
Scheduled Job - Daily reminders on Google Chat using webhook or SMS or Email
In the evening, every day (you can choose time of your choice)
Check if the user has visited the app.
If no, then send the alert asking them to visit

Core - Scheduled Job - Monthly Activity Report
Scheduled Job - Monthly Activity Report
Come Up with a monthly progress report in HTML or PDF (email)
The monthly activity report is meant for a user
The activity report can consist of sections & e-books issued, ratings received on
sections/e-books etc.
On the first day of the month
- Start a job
- Create a report
- Send it as email

Recommended (graded)
Download e-books as PDF for a price
APIs for interaction with sections and books
- CRUD on e-books
- Additional APIs for getting the creating graphs for librarian dashboard
Validation
- All form inputs fields - text, numbers, dates etc. with suitable messages
- Backend validation before storing / selecting from database

Optional
Styling and Aesthetics
Proper login system
Subscriptions or paid versions of the app, become author etc
Ability of app to read books for a user (text-to-speech)


# Library Management System v2

## Project Requirements

Here's a structured project guideline for the Library Management System:

1. User Authentication and Authorization
   - Implement user registration and login functionality using Flask Security or JWT-based token authentication
   - Use Role-Based Access Control (RBAC) to differentiate between librarian and general users
   - Only one librarian account should exist in the system

2. General User Functionalities
   - View all existing sections and e-books
   - Request and return e-books (maximum of 5 e-books per user)
   - Access e-books for a specific period (e.g., 7 days) with automatic revocation after the period ends
   - Provide feedback for an e-book

3. Librarian Functionalities
   - Issue and revoke access to e-books for users
   - Edit existing sections and e-books (content, author name, pages/volume, etc.)
   - Remove sections and e-books
   - Assign books to sections
   - Monitor the current status of each e-book and the user it is issued to
   - View available e-books in the library

4. Search Functionality
   - Implement search functionality for sections and e-books based on section, author, etc.

5. Backend Jobs
   - Implement export, reporting, and alert jobs
   - Daily Reminder Job: Check if users have visited the app and send alerts via Google Chat webhook, SMS, or email
   - Monthly Activity Report Job: Generate a monthly progress report in HTML or PDF format and send it to users via email

6. Backend Performance
   - Optimize backend performance for efficient handling of requests and data processing

7. Core Features
   - Librarian Dashboard: Provide an overview of the library system for the librarian
   - General User Profile: Allow users to view and update their profile information
   - Section Management: Enable the librarian to add, edit, and remove sections
   - E-book Management: Allow the librarian to add, edit, and remove e-books

8. Recommended Features (Optional)
   - Download e-books as PDF for a price
   - APIs for interaction with sections and books (CRUD operations)
   - Additional APIs for generating graphs for the librarian dashboard
   - Form validation for all input fields with suitable messages
   - Backend validation before storing or retrieving data from the database

9. Optional Features
   - Styling and aesthetics to enhance the user interface
   - Proper login system with additional security measures
   - Subscription or paid versions of the app with additional features (e.g., become an author)
   - Text-to-speech functionality for reading e-books to users

10. Storage and Encoding
    - Ensure the storage system handles multiple languages (UTF-8 encoding is usually sufficient)

11. Documentation and Deployment
    - Prepare comprehensive documentation for the system, including user guides and technical documentation
    - Deploy the Library Management System on a suitable hosting platform

Remember to follow best practices for software development, including version control, testing, and code organization. Use appropriate frameworks and libraries to streamline the development process and ensure a robust and scalable system.