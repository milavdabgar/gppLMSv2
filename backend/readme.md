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


function wise it should work. but class borrowed_book sounds odd. Can we use some other name or may be refactor totally the way library management system and its class work, like  bookrequest or transaction or account or any other. you may refactor database as far as you want.

for newer perspective. can you just try to completely refactor database model for library management system. 

just keep in mind that this lms is only going to be used for ebooks, but don't mention ebook, just use word book, keeping in mind further expansion. 

i don't want you to change this
User has subclasses- member, librarian
member has - staff & student
and staff has other types.

try to come up with refactored database model with completely new perspective.
Didn't get response due to network issues, please regenerate 

create database models.py for flask book portal having flavours from audible, amazon books goodreads etc
User Types: Member, Librarian, Admin
Membership Types: Silver, Gold, Platinum
membership duration: monthly, yearly, Lifetime


book has types Physical book, ebook, audiobook
a book can belong to multiple genres, wishlists, collections
admin/librarian manages book genres

a new member is by default a silver member
user/member manages wishlist and collections
Member can Rent book: max_boks_allowed, duration, renewals etc depends on Membership Type
Members can buy/purchase books, different discounts depending on membership type Silver, Gold, Platinum 
Free access books = different set of books based on membership type Silver, Gold, Platinum 
transaction types - buy, rent etc
members can create and manage wishlists
members can arrange books in books collections of books available in his library. either purchased, rented or having free access.


