# Password Manager

This Python program is an implementation to [CS50’s Introduction to Programming with Python Final Project - Password Manager](https://cs50.harvard.edu/python/2022/project/). The **Password Manager** is a simple command-line tool built in Python that allows users to store, retrieve, update, and delete passwords for different websites or services securely. It employs the bcrypt library for password hashing and provides functionalities to generate strong random passwords as well. This README will guide you through the functionality of the Password Manager and provide instructions on how to run and test the code.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Adding a Password](#adding-a-password)
  - [Retrieving a Password](#retrieving-a-password)
  - [Updating a Password](#updating-a-password)
  - [Deleting a Password](#deleting-a-password)
  - [Displaying All Passwords](#displaying-all-passwords)
  - [Generating a Password](#generating-a-password)
  - [Video Demo](#video-demo)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Features

The Password Manager offers the following features:

- Securely store passwords for different websites or services.
- Hash passwords using the bcrypt library before storing them.
- Retrieve passwords by verifying the master password.
- Update existing passwords.
- Delete passwords.
- Display a list of all stored websites and usernames.
- Generate strong random passwords.

## Prerequisites

- Python 3.7 or higher
- A terminal or command prompt
- Virtual environment (optional, but recommended)

## Installation

1. Clone the repository or download the files:

   ```bash
   git clone https://github.com/codenameberyl/CS50P.git
   ```

2. Navigate to the project directory:

   ```bash
   cd "Final Project"/"Final Project"
   ```

3. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Navigate to the project directory and run the `project.py` script to use the Password Manager:

```bash
python3 project.py
```

![Password Manager](https://i.imgur.com/UxuT0j4.png)

### Adding a Password

1. Choose option `1` from the menu to add a password.
2. Enter the website or service name.
3. Enter your username.
4. Enter your password.

### Retrieving a Password

1. Choose option `2` from the menu to retrieve a password.
2. Enter the website or service name.
3. Enter your master password.

### Updating a Password

1. Choose option `3` from the menu to update a password.
2. Enter the website or service name.
3. Enter the old password.
4. Enter the new password.

### Deleting a Password

1. Choose option `4` from the menu to delete a password.
2. Enter the website or service name.

### Displaying All Passwords

Choose option `5` from the menu to display a list of all stored websites and usernames.

### Generating a Password

1. Choose option `6` from the menu to generate a random password.
2. The default length of the generated password is 12.

## Video Demo

Check out the video demonstration of the Password Manager:

[![Password Manager Demo](https://i.imgur.com/BdJPV3t.png)](https://youtu.be/o0y_mwtYgnk)

Click the image above or [here](https://youtu.be/o0y_mwtYgnk) to watch the demo video.

## Running Tests

To run the unit tests for the Password Manager, make sure you have the required dependencies installed. Then, execute the following command:

```bash
pytest test_project.py
```

## Contributing

Contributions to this project are welcome! If you find any bugs or want to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
