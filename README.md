# OrangeHRM Automation Project
  This project automates core functionalities of the OrangeHRM system using Selenium and Python. It includes test cases for login, employee management (add/search/edit/delete), and other modules supported by OrangeHRM.## 🔧 Technologies Used- Python 3.x
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Git/GitHub

📁 Project Structureorangehrm_automation/
│
├── pages/ # Page Object Model classes
│ ├── login_page.py
│ ├── pim_page.py
│ └── ...
│
├── tests/ # Test cases
│ ├── test_login.py
│ ├── test_pim.py
│ └── ...
│
├── utilities/ # Support files, drivers
│ └── config.py
│
├── conftest.py # Pytest fixtures
├── requirements.txt # Python dependencies
└── README.md##

 ✅ Features Covered- Login to OrangeHRM
- Add New Employee
- Search Employee
- Edit Employee Details
- Delete Employee
- Logout## 🚀 How to Run1. Clone this repo:git clone https://github.com/DeviS369/AT_Project_1.git
cd AT_Project_2
Create and activate a virtual environment (optional but recommended):
python -m venv env
env\Scripts\activate       # On Windows
Install dependencies:
pip install -r requirements.txt
Run tests using pytest:
pytest
💡 Example Usage
To test employee addition:
pytest tests/test_pim.py::test_add_employee
🧑 Author
Devi Sudhaka
rGitHub: @DeviS369
Feel free to contribute or suggest improvements
Let me know if you want to include screenshots, badges, or CI setup.
