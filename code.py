import mysql.connector as sql
import pickle

db=sql.connect(host="localhost",user="root",password="admin",database="bank")
cursor=db.cursor()

def main():
    print("Main Menu:-")
    print("1. Insert Record")

    print("2. Display Records as per Account Number")
    print("a. Sorted As Per Account Number")
    print("b. Sorted As Per Customer Name")
    print("c. Sorted As Per Customer Balance")
    print("3. Search Record Details as per Account Number")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Transactions Debit/Credit from the account")
    print("a. Debit/Withdraw from the account")
    print("b. Credit into the account")
    print("7. Exit")

def Insert():
    Acc = int(input("Enter Acc No: "))
    Name = input("Enter Name: ")
    Mob = input("Enter Mob No: ")
    email = input("Enter Email Address: ")
    Add = input("Enter Address: ")
    City = input("Enter City Name: ")
    Country = input("Enter Country Name: ")
    Bal = int(input("Enter Balance: "))
    Rec = [Acc, Name, Mob, email, Add, City, Country,Bal]
    Cmd = "insert into BANK values (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(Cmd, Rec)
    db.commit()
    print(cursor.rowcount, 'record inserted')

def sortacc():
	try:
		cmd = "SELECT * FROM bank ORDER BY  accno"
		cursor.execute(cmd)
		x = "%15s %15s %15s %15s %15s %15s %15s %15s"
		print(x % ("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "COMPLETE ADDRESS", "CITY", "COUNTRY", "BALANCE"))
		
		for i in cursor:
			for a in i:
				print("%14s" % a, end=" ")
			print()
		print("="*125)
	except:
		print("Table Doesn't exist")


def sortname():
	try:
		cmd = "select * from bank order by name"
		cursor.execute(cmd)
		x = "%15s %15s %15s %15s %15s %15s %15s %15s"
		print(x % ("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "COMPLETE ADDRESS", "CITY", "COUNTRY", "BALANCE"))
		
		for i in cursor:
			for a in i:
				print("%14s" % a, end=" ")
			print()
		print("="*125)
	except:
		print("Table doesnt exist")


def sortbal():
	try:
		cmd= "SELECT * FROM bank ORDER BY balance"
		cursor.execute(cmd)
		x = "%15s %15s %15s %15s %15s %15s %15s %15s"
		print(x % ("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "COMPLETE ADDRESS", "CITY", "COUNTRY", "BALANCE"))
		
		for i in cursor:
			for a in i:
				print("%14s" % a, end=" ")
			print()
		print("=" * 125)
	except:
		print("Table doesnt exist")


def searchacc():
	try:
		cmd= "SELECT * FROM bank"
		cursor.execute(cmd)
		ch= input("Enter the accno to be searched: ")

		for i in cursor:
			if i[0] == ch:
				print('='*125)
				x = "%15s %15s %15s %15s %15s %15s %15s %15s"
				print(x % ("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "COMPLETE ADDRESS", "CITY", "COUNTRY", "BALANCE"))
				
				for a in i:
					print('%14s' % a, end=' ')
				print()
				break
			else:
				print("Record Not Found")
	except:
		print("Table Doesnt Exist")

def update():
		cmd= "SELECT * FROM bank"
		cursor.execute(cmd)
		a = int(input("Enter the accno whose details have to be updated: "))
		for i in cursor:
			i = list(i)
			if int(i[0]) ==a:
				ch= input("Change name?(Y/N): ")
				if ch.upper() == 'Y':
					i[1] = input("Enter name: ")
					i[1] = i[1].upper()

				ch = input("Change mobile no?(Y/N): ")
				if ch.upper() == 'Y':
					i[2] = input("Enter mobile no: ")
					i[2] = i[2].upper()

				ch = input("Change email?(Y/N): ")
				if ch.upper() == 'Y':
					i[3] = input("Enter email: ")
					i[3] = i[3].upper()

				ch = input("Change Address?(Y/N): ")
				if ch.upper() == 'Y':
					i[4] = input("Enter address: ")
					i[4] = i[4].upper()

				ch = input("Change City?(Y/N): ")
				if ch.upper() == 'Y':
					i[5] = input("Enter City: ")
					i[5] = i[5].upper()

				ch = input("Change Country?(Y/N): ")
				if ch.upper() == 'Y':
					i[6] = input("Enter Country: ")
					i[6] = i[6].upper()

				ch = input("Change Balance?(Y/N): ")
				if ch.upper() == 'Y':
					i[7] = int(input("Enter Balance: "))
				cmd= "UPDATE BANK SET NAME= %s, MOBILE= %s, EMAIL= %s, ADDRESS= %s, CITY= %s, COUNTRY= %s, BALANCE= %s WHERE ACCNO= %s"
				val= (i[1], i[2], i[3], i[4], i[5], i[6], i[7], int(i[0]),)
				cursor.execute(cmd, val)
				db.commit()
				print("Account Updated")
				break

			else:
				print("Record Not Found")


def create():
	try:
		cursor.execute("CREATE TABLE bank(ACCNO int(14) primary key, NAME varchar(30), MOBILE varchar(10), EMAIL varchar(30), ADDRESS varchar(30), CITY varchar(20), COUNTRY varchar(10), BALANCE int(10))")
		print("Table Created")
		Insert()
	except:
		Insert()

def delete():
		cmd= "SELECT * FROM bank"
		cursor.execute(cmd)
		a = int(input("Enter the account no whose details need to be deleted: "))
		for i in cursor:
			i= list(i)
			if int(i[0]) == a:
				cmd= "DELETE FROM bank WHERE accno = %s"
				val = (int(i[0]), )
				cursor.execute(cmd, val)
				db.commit()
				print("Account Deleted")
				break
		else:
			print("Record Not Found")


def debit():
		cmd= "SELECT * FROM bank"
		cursor.execute(cmd)
		print("Please Note that the money can only be debited if min balance of Rs 5000 exists")
		acc= int(input("Enter the accno from which the money is to be debited: "))
		for i in cursor:
			i= list(i)
			if int(i[0]) == acc:
				Amt= int(input("Enter the amount to be withdrawn: "))
				if ((int(i[7])-Amt)) >= 5000:
					i[7] = int(i[7])
					i[7] -= Amt
					cmd= "UPDATE bank SET BALANCE = %s WHERE accno = %s"
					val = (int(i[7]), int(i[0]))
					cursor.execute(cmd, val)
					db.commit()
					print("Amount Debited")
					break
				else:
					print("There must be at least Rs 5000 in the balance")
					break
		else:
			print("Record Not Found")


def credit():
		cmd= "SELECT * FROM bank"
		cursor.execute(cmd)
		acc= int(input("Enter the accno from which the money is to be debited: "))
		for i in cursor:
			i= list(i)
			if int(i[0])== acc:
				Amt= int(input("Enter the amount to be credited: "))
				i[7] = int(i[7])
				i[7] += Amt
				cmd= "UPDATE BANK SET BALANCE = %s WHERE accno = %s"
				val= (int(i[7]), int(i[0]))
				cursor.execute(cmd, val)
				db.commit()
				print("Amount Credited")
				break
		else:
			print("Record Not Found")


while True:
	main()
	ch= input("Enter your choice: ")
	if ch == '1':
		Insert()
	elif ch == '2':
		while True:
			ch1= input("Enter your choice(a/b/c/d): ")
			if ch1=="a":
				sortacc()
			elif ch1=="b":
				sortname()
			elif ch1=="c":
				sortbal()
			elif ch1=="d":
				print("Back to main menu")
				break
			else:
				print("Invalid choice")
	elif ch == '3':
		searchacc()
	elif ch == '4':
		update()
	elif ch == '5':
		delete()
	elif ch == '6':
		while True:
			ch1= input("Enter a choice (a/b/c): ")
			if ch1.upper() == "A":
				debit()
			elif ch1.upper() == "B":
				credit()
			elif ch1.upper() == "C":
				print("Back to Main Menu")
				break
			else:
				print("Invalid Choice")
	elif ch == '7':
		print("Exiting the menu.")
		break
	else:
		print("Wrong Choice Entered")