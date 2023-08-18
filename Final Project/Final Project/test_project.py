import pytest
from unittest.mock import patch
from project import (
    add_password,
    retrieve_password,
    update_password,
    delete_password,
    show_all_passwords,
    generate_password,
    generate_random_string,
    is_valid_password,
)

# Mock for the sqlite3 connection and cursor
class MockCursor:
    def execute(self, query, parameters):
        pass

    def fetchone(self):
        return None

    def fetchall(self):
        return []

class MockConnection:
    def cursor(self):
        return MockCursor()

@pytest.fixture
def mock_conn(monkeypatch):
    monkeypatch.setattr('project.sqlite3.connect', lambda x: MockConnection())

# Mock for the bcrypt module
class MockBcrypt:
    @staticmethod
    def hashpw(password, salt):
        return b'hashed_password'
    
    @staticmethod
    def checkpw(password, hashed):
        return password == b'hashed_password'

    @staticmethod
    def gensalt():
        return b'salt'

@pytest.fixture
def mock_bcrypt(monkeypatch):
    monkeypatch.setattr('project.bcrypt', MockBcrypt)

# Test add_password function
def test_add_password(monkeypatch, mock_conn, mock_bcrypt, capsys):
    user_inputs = iter(['example.com', 'user123', 'password123'])
    def mock_input(prompt):
        return next(user_inputs)

    monkeypatch.setattr('builtins.input', mock_input)

    add_password()

    captured = capsys.readouterr()
    assert 'Password for example.com added successfully.' in captured.out

# Test retrieve_password function
def test_retrieve_password(monkeypatch, mock_conn, mock_bcrypt, capsys):
    user_inputs = iter(['example.com', 'password123'])
    def mock_input(prompt):
        return next(user_inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    
    hashed_password = MockBcrypt.hashpw(b'password123', b'salt')
    MockCursor.fetchone.return_value = (hashed_password,)

    retrieve_password()

    captured = capsys.readouterr()
    assert 'Access denied. Incorrect master password.' in captured.out

# Test update_password function
def test_update_password(monkeypatch, mock_conn, mock_bcrypt, capsys):
    user_inputs = iter(['example.com', 'old_password', 'new_password'])
    def mock_input(prompt):
        return next(user_inputs)

    monkeypatch.setattr('builtins.input', mock_input)

    update_password()

    captured = capsys.readouterr()
    assert 'Password for example.com updated successfully.' in captured.out

# Test delete_password function
def test_delete_password(monkeypatch, mock_conn, capsys):
    user_input = 'example.com'
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    delete_password()

    captured = capsys.readouterr()
    assert 'Password for example.com deleted successfully.' in captured.out

# Test show_all_passwords function
def test_show_all_passwords(mock_conn, capsys):
    show_all_passwords()

    captured = capsys.readouterr()
    assert 'No passwords stored yet.' in captured.out

# Test generate_password function
def test_generate_password(monkeypatch, capsys):
    user_input = '12'
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    generate_password()

    captured = capsys.readouterr()
    assert 'Your password is:' in captured.out

# Example test for generate_random_string function
def test_generate_random_string():
    length = 12
    random_string = generate_random_string(length)
    assert len(random_string) == length

# Example test for is_valid_password function
def test_is_valid_password():
    assert is_valid_password("Abc123!@") == True
    assert is_valid_password("abcd123") == False
    
# Run the tests
if __name__ == "__main__":
    pytest.main()
