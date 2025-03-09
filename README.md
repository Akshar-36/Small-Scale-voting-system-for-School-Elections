Voting System - Python & MySQL

Description
This is a simple command-line-based Voting System implemented in Python with MySQL as the backend database. The system allows users to register voters, view leaders, cast votes, and display election results.

Features
- View the list of leaders available for voting.
- Register voters with a unique 4-digit voter ID.
- View the list of registered voters.
- Allow registered voters to cast their votes.
- Display election results, including the total votes and the winner.

Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.x
- MySQL Server
- MySQL Connector for Python

Database Setup
Create a MySQL database and the required tables using the following commands:

CREATE DATABASE voting_system;
USE voting_system;

CREATE TABLE LEADER_LIST (
    LEADER_NAME VARCHAR(255) PRIMARY KEY
);

CREATE TABLE VOTER_REGISTERATION (
    ID INT PRIMARY KEY,
    NAME VARCHAR(255)
);

CREATE TABLE VOTING (
    LEADER_NAME VARCHAR(255) PRIMARY KEY,
    VOTES INT DEFAULT 0
);

Installation
1. Clone this repository:
   git clone https://github.com/your-username/voting-system.git
2. Navigate to the project directory:
   cd voting-system
3. Install MySQL Connector for Python if not already installed:
   pip install mysql-connector-python
4. Update the database connection details in the script:
   mycon = sqltor.connect(host='localhost', user='your_username', passwd='your_password', database='voting_system')
5. Run the script:
   python voting_system.py

Usage
1. Start the script and follow the on-screen menu.
2. Choose an option:
   - View Leaders
   - Register Voter
   - View Voters
   - Vote
   - View Results
   - Exit
3. Follow the prompts to perform the desired action.


Notes
- Ensure that the MySQL server is running before executing the script.
- Make sure the LEADER_LIST table has some leader names before voting.
- Each voter can vote only once.

Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.

License
This project is open-source and free to use under the MIT License.

Author
Developed by Akshar Jha
