import maskpass
import DBConnector
import datetime
import pandas as pd
host="localhost"
database="expenses"
user="root"
# specify passsword as a variable 

documentation_message = '''
'E' for Expensing
'T' for Tracking Expenses
'IUE' to Insert an Upcoming Expense
'IPUE' to Insert a Periodic Upcoming Expense (Not Implemented Yet)
'SUE' to Show Upcoming Expenses
'AUE' to Alter Upcoming Expenses'''


currency_dict = {
    'ALL': 'Albania Lek',
    'AFN': 'Afghanistan Afghani',
    'ARS': 'Argentina Peso',
    'AWG': 'Aruba Guilder',
    'AUD': 'Australia Dollar',
    'AZN': 'Azerbaijan New Manat',
    'BSD': 'Bahamas Dollar',
    'BBD': 'Barbados Dollar',
    'BDT': 'Bangladeshi taka',
    'BYR': 'Belarus Ruble',
    'BZD': 'Belize Dollar',
    'BMD': 'Bermuda Dollar',
    'BOB': 'Bolivia Boliviano',
    'BAM': 'Bosnia and Herzegovina Convertible Marka',
    'BWP': 'Botswana Pula',
    'BGN': 'Bulgaria Lev',
    'BRL': 'Brazil Real',
    'BND': 'Brunei Darussalam Dollar',
    'KHR': 'Cambodia Riel',
    'CAD': 'Canada Dollar',
    'KYD': 'Cayman Islands Dollar',
    'CLP': 'Chile Peso',
    'CNY': 'China Yuan Renminbi',
    'COP': 'Colombia Peso',
    'CRC': 'Costa Rica Colon',
    'HRK': 'Croatia Kuna',
    'CUP': 'Cuba Peso',
    'CZK': 'Czech Republic Koruna',
    'DKK': 'Denmark Krone',
    'DOP': 'Dominican Republic Peso',
    'XCD': 'East Caribbean Dollar',
    'EGP': 'Egypt Pound',
    'SVC': 'El Salvador Colon',
    'EEK': 'Estonia Kroon',
    'EUR': 'Euro Member Countries',
    'FKP': 'Falkland Islands (Malvinas) Pound',
    'FJD': 'Fiji Dollar',
    'GHC': 'Ghana Cedis',
    'GIP': 'Gibraltar Pound',
    'GTQ': 'Guatemala Quetzal',
    'GGP': 'Guernsey Pound',
    'GYD': 'Guyana Dollar',
    'HNL': 'Honduras Lempira',
    'HKD': 'Hong Kong Dollar',
    'HUF': 'Hungary Forint',
    'ISK': 'Iceland Krona',
    'INR': 'India Rupee',
    'IDR': 'Indonesia Rupiah',
    'IRR': 'Iran Rial',
    'IMP': 'Isle of Man Pound',
    'ILS': 'Israel Shekel',
    'JMD': 'Jamaica Dollar',
    'JPY': 'Japan Yen',
    'JEP': 'Jersey Pound',
    'KZT': 'Kazakhstan Tenge',
    'KPW': 'Korea (North) Won',
    'KRW': 'Korea (South) Won',
    'KGS': 'Kyrgyzstan Som',
    'LAK': 'Laos Kip',
    'LVL': 'Latvia Lat',
    'LBP': 'Lebanon Pound',
    'LRD': 'Liberia Dollar',
    'LTL': 'Lithuania Litas',
    'MKD': 'Macedonia Denar',
    'MYR': 'Malaysia Ringgit',
    'MUR': 'Mauritius Rupee',
    'MXN': 'Mexico Peso',
    'MNT': 'Mongolia Tughrik',
    'MZN': 'Mozambique Metical',
    'NAD': 'Namibia Dollar',
    'NPR': 'Nepal Rupee',
    'ANG': 'Netherlands Antilles Guilder',
    'NZD': 'New Zealand Dollar',
    'NIO': 'Nicaragua Cordoba',
    'NGN': 'Nigeria Naira',
    'NOK': 'Norway Krone',
    'OMR': 'Oman Rial',
    'PKR': 'Pakistan Rupee',
    'PAB': 'Panama Balboa',
    'PYG': 'Paraguay Guarani',
    'PEN': 'Peru Nuevo Sol',
    'PHP': 'Philippines Peso',
    'PLN': 'Poland Zloty',
    'QAR': 'Qatar Riyal',
    'RON': 'Romania New Leu',
    'RUB': 'Russia Ruble',
    'SHP': 'Saint Helena Pound',
    'SAR': 'Saudi Arabia Riyal',
    'RSD': 'Serbia Dinar',
    'SCR': 'Seychelles Rupee',
    'SGD': 'Singapore Dollar',
    'SBD': 'Solomon Islands Dollar',
    'SOS': 'Somalia Shilling',
    'ZAR': 'South Africa Rand',
    'LKR': 'Sri Lanka Rupee',
    'SEK': 'Sweden Krona',
    'CHF': 'Switzerland Franc',
    'SRD': 'Suriname Dollar',
    'SYP': 'Syria Pound',
    'TWD': 'Taiwan New Dollar',
    'THB': 'Thailand Baht',
    'TTD': 'Trinidad and Tobago Dollar',
    'TRY': 'Turkey Lira',
    'TRL': 'Turkey Lira',
    'TVD': 'Tuvalu Dollar',
    'UAH': 'Ukraine Hryvna',
    'GBP': 'United Kingdom Pound',
    'USD': 'United States Dollar',
    'UYU': 'Uruguay Peso',
    'UZS': 'Uzbekistan Som',
    'VEF': 'Venezuela Bolivar',
    'VND': 'Viet Nam Dong',
    'YER': 'Yemen Rial',
    'ZWD': 'Zimbabwe Dollar'
}



def create_new_user():
    active = True
    while active == True:
        new_username = input("\n--- Sign-Up Page---\nEnter a username to sign up: ")
        registered_username = new_username.lower()
        sql_selection_query = f"SELECT * FROM USERS where username ='{registered_username}';"
        symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '"', '*', '|', ',', '&', '<', '`', '}', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
        contains_special_character = False
        for character in registered_username:
            if character in symbols:
                contains_special_character = True
        if len(DBConnector.obtain_values(host, database, user, password, sql_selection_query)) >= 1:
            print(f"{registered_username} Already Exists. Please choose another username.")
        elif len(registered_username) > 18 or len(registered_username) <4:
            print(f"Invalid Username. The Username should be between 4 and 18 characters!")
        elif contains_special_character == True:
            print("Invalid Username. The Username can only contain - or . or _ as a special character.")

        else:
            new_password = maskpass.askpass(prompt="Choose New Password: ", mask = "*")
            new_password_2 = maskpass.askpass(prompt="Verify Password: ", mask = "*")
            if (new_password==new_password_2):
                active = False
                print(f"\nSigning {registered_username} Up to Expenses Management System.")

                #Generating USER_ID
                sql_selection_query = "SELECT USER_ID FROM USERS ORDER BY USER_ID DESC"
                latest_id = DBConnector.obtain_values(host,database,user,password,sql_selection_query)[0][0]
                new_id = latest_id + 1

                #Adding USER_ID, USERNAME and PASSWORD to the USERS Table
                sql_insertion_query = f"INSERT INTO USERS VALUES({new_id},'{registered_username}','{new_password}');"
                DBConnector.insert_values(host,database,user,password,sql_insertion_query)

            else:
                print("Passwords do not match! Sign up again!")


def sign_in():
    sign_in_username = input("--- Sign In Page ---\nEnter Username: ")
    sql_selection_query = f"SELECT * FROM USERS WHERE USERNAME ='{sign_in_username.lower()}';"
    if len(DBConnector.obtain_values(host, database, user, password, sql_selection_query)) == 1:
        sign_in_password = maskpass.askpass()
        sql_selection_query = f"SELECT PASSWORD FROM USERS WHERE USERNAME ='{sign_in_username.lower()}';"
        actual_password = DBConnector.obtain_values(host,database,user,password,sql_selection_query)[0][0]
        if sign_in_password == actual_password:
            print(f"Welcome {sign_in_username}!")
            sql_selection_query = f"SELECT USER_ID FROM USERS WHERE USERNAME = '{sign_in_username.lower()}';"
            user_id = DBConnector.obtain_values(host,database,user,password,sql_selection_query)[0][0]
            return sign_in_username.lower(), user_id
        else:
            print("Wrong Password!")
            return None, None
            

    else:
        print("Invalid Username!")
        return None,None
        


def expensing(username, user_id, amount_to_expense=None, currency_code=None, date=None):
    if (amount_to_expense==None and currency_code==None and date==None):
        amount_to_expense, currency_code = input("Specify amount to expense followed by the currency. Example: 100-USD\n=> ").split("-")
        date = input("Enter the date of the expense in the format 'YYYY-MM-DD' or 'Today' for today's date: ")
        if date.lower() == 'today':
            date = str(datetime.date.today())
        amount_to_expense = float(amount_to_expense)
        currency_code = currency_code.upper()

    if currency_code in currency_dict.keys():
        if amount_to_expense > 0:
            sql_selection_query = f"SELECT XID FROM ExpensesTable ORDER BY XID DESC"
            latest_xid = DBConnector.obtain_values(host,database,user,password,sql_selection_query)[0][0]
            new_xid = latest_xid + 1
            sql_insertion_query = f"INSERT INTO ExpensesTable VALUES({new_xid},'{date}',{amount_to_expense},'{currency_code}',{user_id});"
            DBConnector.insert_values(host, database, user, password, sql_insertion_query)
        else:
            print("\n Amount to expense is invalid. Please expense an amount greater than 0.")
    else:
        print("\nCurrency used is invalid. Please use a valid currency code.")


def date_filtering():
    date_filtering = input("\nEnter 'ALL' for All Dates or Specify a Date Range.\nExample: 2022-01-01 to 2022-01-30\nSpecify Date:")
    try:
        startDate, endDate = date_filtering.split(" to ")
    except:
        startDate, endDate = None, None
    finally:
        if (startDate!=None) and (endDate != None):
            print(f"Date Filtering is from {startDate} to {endDate}")
        else:
            print("Date Filtering is: ALL DATES") 
    return startDate, endDate 


def amount_filtering():
    amount_filtering = input("\nEnter 'ALL' for All Amounts or Specify an Amount Range.\nExample: 100 to 1000\nSpecify Amount: ")
    try:
        startAmount, endAmount = int(amount_filtering.split(" to ")[0]),int(amount_filtering.split(" to ")[1])
    except:
        startAmount, endAmount = None, None
    finally:
        if (startAmount!=None) and (endAmount != None):
            print(f"Amount Filtering is from {startAmount} to {endAmount}")
        else:
            print("Amount Filtering is: ALL AMOUNTS")
    return startAmount, endAmount


def currency_filtering():
    currency_filtering = input("\nEnter 'ALL' for ALL Currencies or Specify one or a list of currencies.\nExample: USD-GBP-EUR\nSpecify Currency/Currencies: ")
    currency_list = currency_filtering.split("-")
    if (len(currency_list) == 1) and (currency_list[0].lower()=="all"):
        print("Currency Filtering is: ALL CURRENCIES")

    elif (len(currency_list)==1):
        if currency_list[0].upper() in currency_dict.keys():
            currency_list = [currency_list[0].upper()]
            print(f"Currency Filtering is: {currency_list[0]}")
        else:
            currency_list=["all"]
            print(f"Currency {currency} is invalid. \nCurrency Filter set to None. Thus, Filtering on ALL Currencies")


    elif(len(currency_list)>1):
        for currency in currency_list:
            if currency not in currency_dict.keys():
                print(f"Currency provided: {currency} is not valid.")
                print("Currency Filtering is set to: ALL CURRENCIES")
                currency_list = ["ALL"]
                break
        print(f"Currency Filtering is: {currency_list}")
    return currency_list

def query_expenses(user_id):
    print("\n--User Defined Filtering Criteria--")
    startDate, endDate = date_filtering()
    startAmount, endAmount = amount_filtering()
    currency_list = currency_filtering()

    # Filtering Criteria: DATE, AMOUNT, CURRENCY.
    # 12 Combinations of Filtering are available, each requires a Customized SQL QUERY. 
    # Filtering #1 on: Date, Amount and several Currencies.
    if( (startDate != None) and (endDate != None) and (startAmount != None) and (endAmount != None) and (len(currency_list) > 1) ):
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY FROM ExpensesTable
                            WHERE DATE BETWEEN 
                            '{startDate}'
                            AND
                            '{endDate}'
                            AND
                            AMOUNT BETWEEN
                            {startAmount}
                            AND
                            {endAmount}
                            AND
                            CURRENCY in {tuple(currency for currency in currency_list)}
                            AND
                            USER_ID = {user_id};
                            """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
        
    # Filtering #2 on: Date, Amount, One Currency Only.
    elif( (startDate != None) and (endDate != None) and (startAmount != None) and (endAmount != None) and (len(currency_list) == 1) and (currency_list[0].lower() != "all") ):
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY FROM ExpensesTable
                            WHERE DATE BETWEEN 
                            '{startDate}'
                            AND
                            '{endDate}'
                            AND
                            AMOUNT BETWEEN
                            {startAmount}
                            AND
                            {endAmount}
                            AND
                            CURRENCY = '{currency_list[0]}'
                            AND
                            USER_ID = {user_id};
                            """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)

    # Filtering #3 on: Date, Amount.
    elif( (startDate != None) and (endDate != None) and (startAmount != None) and (endAmount != None) and (len(currency_list) == 1) and (currency_list[0].lower() == "all") ):
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY FROM ExpensesTable
                            WHERE DATE BETWEEN 
                            '{startDate}'
                            AND
                            '{endDate}'
                            AND
                            AMOUNT BETWEEN
                            {startAmount}
                            AND
                            {endAmount}
                            AND
                            USER_ID = {user_id};
                            """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)

    # Filtering #4 on Amount and One Currency Only.
    elif( (startDate == None) and (endDate == None) and (startAmount != None) and (endAmount != None) and (len(currency_list) == 1) and (currency_list[0].lower() != "all") ):
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY FROM ExpensesTable
                            WHERE 
                            AMOUNT BETWEEN
                            {startAmount}
                            AND
                            {endAmount}
                            AND
                            CURRENCY = '{currency_list[0]}' 
                            AND
                            USER_ID = {user_id};
                            """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
    # Filtering #5 on Amount and Several Currencies.
    elif( (startDate == None) and (endDate == None) and (startAmount != None) and (endAmount != None) and (len(currency_list) > 1) ):
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY FROM ExpensesTable
                            WHERE 
                            AMOUNT BETWEEN
                            {startAmount}
                            AND
                            {endAmount}
                            AND
                            CURRENCY in {tuple(currency for currency in currency_list)}
                            AND
                            USER_ID = {user_id};
                            """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
    # Filtering #6 on Amount Only.
    elif( (startDate == None) and (endDate == None) and (startAmount != None) and (endAmount != None) and (len(currency_list) == 1) and (currency_list[0].lower() == "all") ):
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY FROM ExpensesTable
                            WHERE 
                            AMOUNT BETWEEN
                            {startAmount}
                            AND
                            {endAmount}
                            AND
                            USER_ID = {user_id};
                            """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
    # Filtering #7 on Date and One Currency Only.
    elif( (startDate != None) and (endDate != None) and (startAmount == None) and (endAmount == None) and (len(currency_list) == 1) and (currency_list[0].lower() != "all") ):
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY FROM ExpensesTable
                            WHERE DATE BETWEEN 
                            '{startDate}'
                            AND
                            '{endDate}'
                            AND
                            CURRENCY = '{currency_list[0]}'
                            AND
                            USER_ID = {user_id};
                            """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
    # Filtering #8 on Date Only.
    elif( (startDate != None) and (endDate != None) and (startAmount == None) and (endAmount == None) and (len(currency_list) == 1) and (currency_list[0].lower() == "all") ):
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY FROM ExpensesTable
                            WHERE DATE BETWEEN 
                            '{startDate}'
                            AND
                            '{endDate}'
                            AND
                            USER_ID = {user_id};
                            """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
    # Filtering #9 on Date and Several Currencies.
    elif( (startDate != None) and (endDate != None) and (startAmount == None) and (endAmount == None) and (len(currency_list) > 1) ):
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY FROM ExpensesTable
                            WHERE DATE BETWEEN 
                            '{startDate}'
                            AND
                            '{endDate}'
                            AND
                            CURRENCY in {tuple(currency for currency in currency_list)}
                            AND
                            USER_ID = {user_id};
                            """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
    # Filtering #10 on One Currency Only.
    elif( (startDate == None) and (endDate == None) and (startAmount == None) and (endAmount == None) and (len(currency_list) == 1) and (currency_list[0].lower() != "all")):
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY FROM ExpensesTable
                            WHERE 
                            CURRENCY = '{currency_list[0]}'
                            AND
                            USER_ID = {user_id};
                            """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
    # Filtering #11 on Several Currencies.
    elif( (startDate == None) and (endDate == None) and (startAmount == None) and (endAmount == None) and (len(currency_list) > 1)):
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY FROM ExpensesTable
                            WHERE 
                            CURRENCY in {tuple(currency for currency in currency_list)}
                            AND
                            USER_ID = {user_id};
                            """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
    # Filtering #12 on nothing. (Retrieve All Results)
    elif( (startDate == None) and (endDate == None) and (startAmount == None) and (endAmount == None) and (len(currency_list) == 1) and (currency_list[0].lower() == "all")):
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY FROM ExpensesTable
                            WHERE 
                            USER_ID = {user_id};
                            """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
    else:
        print("Invalid Filtering Criteria!")
        query = None

    return query

def show_expenses_query(query_result,mode):
    date_list=list()
    amount_list=list()
    currency_list=list()
    if mode.lower()=="regular":
        # This is designed for the expenses table
        for row in query_result:
            date_list.append(row[0])
            amount_list.append(row[1])
            currency_list.append(row[2])
        query_dict = {"Date":date_list, "Amount":amount_list, "Currency":currency_list}
    elif mode.lower()=="upcoming":
        # This is designed for the upcoming expenses table
        comment_list = list()
        status_list = list()
        for row in query_result:
            date_list.append(row[0])
            amount_list.append(row[1])
            currency_list.append(row[2])
            comment_list.append(row[3])
            status_list.append(row[4])
        query_dict = {"Date":date_list, "Amount":amount_list, "Currency":currency_list, "Comment":comment_list, "Status":status_list}
    elif mode.lower() == "upcoming-alter":
        # This is intended to change the status of an upcoming expense whether its date became expired or regular usage.
        uid_list = list()
        comment_list = list()
        status_list = list()
        for row in query_result:
            uid_list.append(row[0])
            date_list.append(row[1])
            amount_list.append(row[2])
            currency_list.append(row[3])
            comment_list.append(row[4])
            status_list.append(row[5])
        query_dict = {"UPCOMING EXPENSES ID":uid_list,"Date":date_list, "Amount":amount_list, "Currency":currency_list, "Comment":comment_list, "Status":status_list}

    df = pd.DataFrame(data=query_dict)
    print(df)

    
def insert_upcoming_expenses(user_id):
    upcoming_expense_request = input("Enter the upcoming expense as the following format: YYYY-MM-DD/AMOUNT/CURRENCY/COMMENT \n => ") 
    try:
        date,amount,currency,comment = upcoming_expense_request.split("/")
    except:
        print("Invalid Input. Please enter the upcoming expense as the following format: YYYY-MM-DD/AMOUNT/CURRENCY/COMMENT")
        print("Example to define an upcoming expense of 2000$ for house rent on 2023-01-01 type: 2023-01-01/2000/USD/HOUSE RENT")
    else:
        amount = float(amount)
        currency = currency.upper()
        if currency in currency_dict.keys():
            if amount > 0:
                sql_selection_query = f"SELECT UID FROM UpcomingExpenses ORDER BY UID DESC"
                latest_uid = DBConnector.obtain_values(host,database,user,password,sql_selection_query)[0][0]
                new_uid = latest_uid + 1
                year,month,day = date.split("-")
                date_evaluation = datetime.date(int(year),int(month),int(day))
                if (date_evaluation >= datetime.date.today()):
                    status = "UNEXPENSED"
                    sql_insertion_query = f"INSERT INTO UpcomingExpenses VALUES({new_uid},'{date}',{amount},'{currency}','{comment}','{status}',{user_id});"
                    DBConnector.insert_values(host, database, user, password, sql_insertion_query)
                else:
                    print("Invalid Input: Date Entered is in the past ")
            else:
                print("Invalid Input: Amount Entered is Invalid.")
        else:
            print("Invalid Input: Currency Entered is Invalid.")
  
def alter_upcoming_expenses_status(user_id,query=None):
    active=True
    if query==None:
        sql_selection_query = f"""SELECT UID,DATE, AMOUNT, CURRENCY, COMMENT, STATUS FROM UpcomingExpenses
                    WHERE
                    STATUS = 'UNEXPENSED'
                    AND
                    USER_ID = {user_id};
                    """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
        show_expenses_query(query,mode="upcoming-alter")
        if len(query) == 0:
            active=False
    elif query != None:
        show_expenses_query(query,mode="upcoming-alter")

    while active:
        print("\nSpecify the Upcoming Expense ID and choose whether to 'EXPENSED' or 'NOT TO BE EXPENSED' || Enter X anytime to Stop")
        print("Example: 1-NOT TO BE EXPENSED")
        request = input(" => ")
        if request.lower() == 'x':
            active = False
        else:
            try:
                uid,status = request.split("-")
            except:
                print("Invalid Input.")
            else:
                # Validating Given Status
                if status.lower() != 'expensed'  and status.lower() != 'not to be expensed':
                    valid_status = False
                    print("Invalid Status.")

                else:
                    valid_status = True

                # Grabbing UIDs
                if valid_status == True:
                    sql_selection_query = f"""SELECT UID FROM UpcomingExpenses
                                            WHERE 
                                            STATUS = 'UNEXPENSED'
                                            AND
                                            USER_ID = {user_id}
                                            ORDER BY UID DESC"""
                    all_queried_uid = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
                    all_uid = list()
                    for queried_uid in all_queried_uid:
                        all_uid.append(queried_uid[0])
                    uid = int(uid)
                    if uid in all_uid:
                        sql_insertion_query = f"""UPDATE UpcomingExpenses
                                                    SET STATUS = '{status.upper()}'
                                                    WHERE UID = {uid}
                                                    AND
                                                    USER_ID = {user_id};"""
                        DBConnector.insert_values(host, database, user, password, sql_insertion_query)
                        print(f"Changed UID#{uid} status to {status}")
                        
                        if status.lower() == "expensed":
                            sql_selection_query = f"""SELECT DATE,AMOUNT,CURRENCY FROM UpcomingExpenses
                                                    WHERE
                                                    STATUS = 'EXPENSED'
                                                    AND
                                                    UID = {uid}
                                                    AND
                                                    USER_ID = {user_id};"""
                            query = DBConnector.obtain_values(host, database, user, password, sql_selection_query)
                            for row in query:
                                date = row[0]
                                amount_to_expense = row[1]
                                currency_code = row[2]
                            amount_to_expense = float(amount_to_expense)
                            currency_code = currency_code.upper()
                            expensing(username, user_id, amount_to_expense=amount_to_expense, currency_code=currency_code, date=date)                       
                    else:
                        print("Invalid UID")

                       


def fetch_upcoming_expenses(user_id):
    # Check if some upcoming expenses have a date lower than today's date
    expired_upcoming_expenses = False
    todays_date = str(datetime.date.today())
    sql_selection_query = f"""SELECT UID, DATE, AMOUNT, CURRENCY, COMMENT, STATUS FROM UpcomingExpenses
                        WHERE 
                        DATE < '{todays_date}'
                        AND
                        STATUS = 'UNEXPENSED'
                        AND
                        USER_ID = {user_id}
                        """
    query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
    if (len(query) >= 1 ):
        expired_upcoming_expenses=True
        show_expenses_query(query,mode="upcoming-alter")
        print("\n[WARNING] Upcoming Expenses with Expired Date and status as 'UNEXPENSED'  are caught.")
        print("[WARNING] These statuses should be changed.")
        alter_upcoming_expenses_status(user_id,query)

    # If no upcoming expenses have an expired date, show all upcoming expenses.
    if expired_upcoming_expenses == False:
        sql_selection_query = f"""SELECT DATE, AMOUNT, CURRENCY, COMMENT, STATUS FROM UpcomingExpenses
                    WHERE 
                    USER_ID = {user_id}
                    ORDER BY DATE ASC;
                    """
        query = DBConnector.obtain_values(host,database,user,password,sql_selection_query)
        show_expenses_query(query,mode="upcoming")






# Main Method
request = input("Hello. Please Enter 'Sign-In' if you already have an account.\n'Sign-Up' If you do not have an account\n=> ")
if request.lower()=="sign-in":
    username,user_id = sign_in()

elif request.lower() =="sign-up":
    create_new_user()
    username,user_id = sign_in()
active = True
while (  (active==True) and (username != None) and (user_id != None)    ):
    request = input(f"\n{username}, Please specify you request or 'D' for Documentation and 'X' to exit:  ")
    if request.lower() == 'e':
        expensing(username, user_id, amount_to_expense=None, currency_code=None, date=None)
    elif request.lower() == 't':
        query = query_expenses(user_id)
        show_expenses_query(query,"regular")
    elif request.lower() =='iue':
        insert_upcoming_expenses(user_id)
    elif request.lower() == 'sue':
        fetch_upcoming_expenses(user_id)
    elif request.lower() == 'aue':
        alter_upcoming_expenses_status(user_id,query=None)
    elif request.lower() == 'x':
        print("Thank you for using the Expenses Management System (EMS) By NS.")
        active=False
    elif request.lower() == 'd':
        print(documentation_message)
    else:
        print("Invalid Input.") 
