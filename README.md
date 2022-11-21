# Private Expenses Management System (PEMS)

## PEMS
Private Expenses Management System (PEMS) is a software that allows its users to manage their expenses.  
PEMS users can log all their expenses with their corresponding dates and currency. These logs are stored in a private database for PEMS that contains several tables all linked together (DB Schema will be shown at a private section).  
DBConnector is the script used to perform the Database CRUD Operations between PEMS and MySQL RDBMS.  
PEMS can handle hundreds of users working together on the DB, each user has his/her own credentials: User_ID, Username and Password. All the credentials and sensitive information are managed and protected (from SQL Injection...)   
The functions are designed to operate given a user_id once the user signs in.  
PEMS Features:  
-	Users can sign-in to their accounts (or create an account if they do not already operate on PEMS) to Expense several expenses with their corresponding currency, date and other dependencies.
-	Users can Track all their Expenses.
-	PEMS allows the users to filter on their expenses using several filtering criteria such as Currency Filtering, Date Filtering and Expensed Amounts Filtering. 
-	PEMS allows over 10+ Expenses Filtering Combinations available to the user.
-	Users can insert Upcoming Expenses (in future dates) to the system with some dependencies to each upcoming expense: Date, Currency, Amount and a Comment for each expense.
-	Users can alter the status of their upcoming expenses to “EXPENSED” or “NOT TO BE EXPENSED” upon their request at any given time in the session.
-	If the users change the status of their upcoming expenses to “EXPENSED”, then automatically each expense will be moved to the EXPENSES table, (where it contains all the expenses of the users) and thus if the user chooses to track the expenses, this Upcoming Expense will now be a regular Expense.
-	Users can opt to view their upcoming expenses at any time: the Date, Amount, Currency and Comment of the Upcoming Expenses are fetched to the user.
-	When the user chooses to view any upcoming expenses, the program will surf through all the Upcoming Expenses linked to this specific user and will catch all Upcoming Expenses that are expired. (Expired Upcoming Expenses are all expenses that have a date lower than the session’s date i.e. today’s date) 
-	For all expired upcoming expenses, the user is prompted to change their statuses from “UNEXPENSED” to either “EXPENSED” or “NOT TO BE EXPENSED”. Also in this case, if the user opts to EXPENSE any Expired Upcoming Expense, this specific expense with its dependencies will automatically be moved to the User’s Expenses Table.




## DBConnector
DBConnector is a python script that allows the users to interact with the MySQL RDBMS through python functions.  
It is built using the mysql.conenctor library, some of the DBConnector features:    
### DBConnector Testing:  
-	Tests the Database connection in an environment, given:   
      1. Host
      2. Database Name
      3. User
      4. Password
-	The Test provides a feedback loop to inform the user whether the connection to the database was established successfully, if the databases in MySQL are fetched properly and it chooses the specific database.
-	If errors arise during the connection to the database, DBConnector will capture the error using mysql.connector.Error and shows it to the user.

### DBConnector CRUD Operations:  
-	Inserts values to the chosen database given the host, database, user, password, and an SQL Insertion Query (Insert Statement).
-	Queries Insertion Error Handling: In case the insertion fails, the insertion errors are captured and printed to the user.
-	Obtain values from the database given the host, database, user, password, and an SQL Selection Query (Select Statement).
-	Queries Retrieving Error Handling: In case the query response fails, the selection errors are captured and printed to the user.


## PEMS Database Schema
PEMS's Database is constituted of three tables: USERS, EXPENSES and UPCOMING EXPENSES.

### USERS Table
USERS Table contains:
1. USER_ID
2. USERNAME
3. PASSWORD  

Values Restrictions:  
- Only Unique instances of user_id and username.  
- Null values are prohibited.  
Users are uniquely identified by their IDs (USER_ID) which is the Primary Key of table: USERS  

![USERS TABLE SCHEMA](https://user-images.githubusercontent.com/98900886/202930566-441330a4-e2a1-41c3-83a5-2da2ea014d56.png)

---

### EXPENSES Table
EXPENSES Table contains:
1. AMOUNT: Expense Amount
2. CURRENCY: Expense Currency
3. DATE: Expense Date  

Expenses are uniquely identified by the Expense ID (XID) which is the Primary Key of the table: EXPENSES  

Values Restrictions:
- Only Unique instances of user_id and username
- Null values are prohibited.  
Relationship with the USERS table is via the USER_ID Foreign Key.  

![EXPENSES TABLE SCHEMA](https://user-images.githubusercontent.com/98900886/202930528-dcf4dfd2-3aad-4b08-ae2e-3a4dcfe49130.png)
---
### UPCOMING EXPENSES Table
UPCOMING EXPENSES Table contains:
1. DATE: Upcoming Expense date
2. AMOUNT: Upcoming Expense amount
3. CURRENCY: Upcoming Expense currency
4. COMMENT: Upcoming Expense comment
5. STATUS: Upcoming Expense status 
6. USER_ID: Upcoming Expense User ID  

Values Restrictions:  
- Only Unique instances of user_id and username  
- Null values are prohibited.   

Upcoming Expenses are uniquely identified by their Upcoming Expense ID (UID) which is the Primary Key of the table: Upcoming Expenses.  
Relationship with the USERS table is via the USER_ID Foreign Key.  

![UPCOMING EXPENSES TABLE SCHEMA](https://user-images.githubusercontent.com/98900886/202930579-c8191e11-260a-453f-9717-5cc337ad9b16.png)

## Upcoming features (Under development) :
- PEMS will become a cross-platform application available on: MacOS, Windows, Android and iOS.
- Front-End Development: An integrated GUI that adjusts its size and pixels dynamically to fit most screens. (Using Kivy)
- Back-End Development: Addition of Expenses CSV Report Generator and ability to send it by mail to specific recipients.
- Back-End Development: Expenses Chart Generator
