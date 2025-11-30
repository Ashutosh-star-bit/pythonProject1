
🚌 Bus Reservation System
A Python-based desktop application for managing bus ticket reservations. This system provides a comprehensive platform for user authentication, bus searching, ticket booking, and reservation management.

✨ Features
User Authentication: Secure Sign-up, Sign-in, and Password Reset functionality.

Bus Search: Easily find buses between two locations (e.g., Mirzapur to Prayagraj).

Ticket Booking: Input passenger details (Name, Gender, Age, Date of Journey, Bus Type) to book a ticket.

Multiple Payment Options: Support for various payment modes including popular UPI/Wallet services and Cash on Delivery (simulated).

My Booking: View detailed information about existing reservations by providing Passenger Name and Date of Journey.

Cancel Booking: Cancel a confirmed reservation using passenger details and journey information.

User Profile: Display logged-in user's profile information (Username and Email).

Contact Us: A dedicated page for users to submit comments and queries.

About Us: Information about the bus reservation service.

💻 Technologies Used
The application is built using Python for the backend logic and a MySQL database for data persistence.

Component	Technology	Description
GUI	tkinter	Standard Python interface toolkit.
GUI Enhancement	customtkinter	Modern appearance for the Tkinter interface.
Database	PyMySQL	Used for connecting and interacting with the MySQL database.
Date Picker	tkcalendar	Provides a date selection widget for the journey date.
Image Handling	Pillow (PIL)	Used for loading and manipulating images/icons in the GUI.
Other	json, subprocess, re	Used for inter-script data transfer, running external scripts, and string operations.
🛠️ Prerequisites
Before running the application, ensure you have the following installed:

Python 3.x

MySQL Database Server

🚀 Installation
Follow these steps to set up the project locally:

1. Clone the Repository
Bash
git clone https://github.com/your-username/bus-reservation-system.git
cd bus-reservation-system
2. Install Python Dependencies
Install the required Python libraries using pip:

Bash
pip install -r requirements.txt
# If you don't have a requirements.txt, manually install:
pip install customtkinter Pillow PyMySQL tkcalendar
3. Database Setup
The application is configured to connect to a local MySQL server.

Default Connection: The Python scripts use host='localhost', user='root', and password='tiger' to connect to MySQL.

If your MySQL credentials are different, you must update the pymysql.connect() call in the following files:

signup.py

signin.py

mybooking.py

cancelbooking.py

detailpng.py

paymentpng.py

contactpng.py

Database and Tables: The application will attempt to create the userdata database and the necessary tables (data, passenger, commentdata) if they do not exist, upon the first execution of signup.py or other database-related functions.

🚦 Usage
To start the application, run the main file:

Bash
python main.py
The application will launch a splash screen, followed by the User Login page, from where you can proceed to Sign Up or log in with existing credentials. 

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or encounter any bugs, please feel free to open an issue or submit a pull request.
