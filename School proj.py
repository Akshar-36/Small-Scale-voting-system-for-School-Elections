# Voting System - Python & MySQL
# Requirements:
# - MySQL database with the following tables:
#   1. LEADER_LIST (LEADER_NAME VARCHAR(255) PRIMARY KEY)
#   2. VOTER_REGISTERATION (ID INT PRIMARY KEY, NAME VARCHAR(255))
#   3. VOTING (LEADER_NAME VARCHAR(255) PRIMARY KEY, VOTES INT DEFAULT 0)
# - Ensure MySQL server is running and accessible.

import mysql.connector as sqltor

# Connect to the MySQL database
mycon = sqltor.connect(host='localhost', user='root', passwd='aksharjha2105', database='akshar')
cursor = mycon.cursor()

# Function to fetch and display the list of leaders
def view_leaders():
    cursor.execute('SELECT LEADER_NAME FROM LEADER_LIST')
    leaders = cursor.fetchall()
    if leaders:
        for row in leaders:
            print(row[0])
    else:
        print("No leaders found.")

# Function to register new voters with a unique 4-digit ID
def register_voter():
    for _ in range(int(input("Number of voters to register: "))):
        while True:
            try:
                voter_id = int(input("4-digit Voter ID: "))
                if 1000 <= voter_id <= 9999:
                    cursor.execute("SELECT ID FROM VOTER_REGISTERATION WHERE ID = %s", (voter_id,))
                    if not cursor.fetchone():
                        break  # Valid and unique ID
                print("Invalid or duplicate ID.")
            except ValueError:
                print("Enter a valid 4-digit number.")
        name = input("Name: ").strip()
        cursor.execute("INSERT INTO VOTER_REGISTERATION (ID, NAME) VALUES (%s, %s)", (voter_id, name))
        mycon.commit()

# Function to display all registered voters
def view_voters():
    cursor.execute('SELECT ID, NAME FROM VOTER_REGISTERATION')
    voters = cursor.fetchall()
    if voters:
        for row in voters:
            print(row[0], row[1])
    else:
        print("No voters found.")

# Function to allow registered voters to cast their votes
def vote():
    cursor.execute('SELECT LEADER_NAME FROM LEADER_LIST')
    leaders = [row[0] for row in cursor.fetchall()]
    cursor.execute('SELECT ID FROM VOTER_REGISTERATION')
    voters = {row[0] for row in cursor.fetchall()}  # Using a set for fast lookup
    
    if not leaders or not voters:
        print("Voting cannot proceed. Check leader/voter records.")
        return
    
    while voters:
        try:
            voter_id = int(input("Voter ID: "))
            if voter_id not in voters:
                print("Invalid ID or already voted.")
                continue
        except ValueError:
            print("Enter a valid ID.")
            continue
        
        # Display leader options
        for i, leader in enumerate(leaders, start=1):
            print(i, leader)
        
        try:
            choice = int(input("Vote: "))
            if 1 <= choice <= len(leaders):
                cursor.execute("INSERT INTO VOTING (LEADER_NAME, VOTES) VALUES (%s, %s) ON DUPLICATE KEY UPDATE VOTES = VOTES + 1", (leaders[choice - 1], 1))
                mycon.commit()
                voters.remove(voter_id)  # Remove voter from set to prevent duplicate voting
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a valid number.")
    
    display_results()

# Function to display election results
def display_results():
    cursor.execute('SELECT LEADER_NAME, VOTES FROM VOTING ORDER BY VOTES DESC')
    results = cursor.fetchall()
    
    if results:
        total_votes = sum(row[1] for row in results)
        winner = results[0][0]
        percentage = (results[0][1] / total_votes) * 100 if total_votes else 0
        
        for row in results:
            print(row[0], row[1])
        print("Winner:", winner, f"{percentage:.2f}%")
    else:
        print("No votes recorded.")

# Main program loop - Displays menu and executes corresponding functions
while True:
    print("\n==============================")
    print("        VOTING SYSTEM        ")
    print("==============================")
    print("1. View Leaders")
    print("2. Register Voter")
    print("3. View Voters")
    print("4. Vote")
    print("5. View Results")
    print("6. Exit")
    print("==============================")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        view_leaders()
    elif choice == "2":
        register_voter()
    elif choice == "3":
        view_voters()
    elif choice == "4":
        vote()
    elif choice == "5":
        display_results()
    elif choice == "6":
        mycon.close()
        print("Thank you for using the Voting System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
