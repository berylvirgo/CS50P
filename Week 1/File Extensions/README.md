# File Extensions

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 1 - File Extensions Problem Set](https://cs50.harvard.edu/python/2022/psets/1/extensions/), named `extensions.py`, simulates the process of determining a file's media type based on its extension. The program prompts the user for a file name, analyzes the file's extension, and then outputs the corresponding media type. It covers common image formats (gif, jpg, jpeg, png), document formats (pdf, txt), and compressed formats (zip). If the file has no recognized extension, it outputs the default media type "application/octet-stream".

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `extensions.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python extensions.py
   ```

4. The program will prompt you to enter a file name. After you press Enter, it will output the corresponding media type based on the file's extension.

## Program Code

```python
# extensions.py

def media_type():
    file_name = input("Enter the file name: ").strip().casefold()

    if file_name.endswith(".gif"):
        return "image/gif"
    elif file_name.endswith((".jpg", ".jpeg")):
        return "image/jpeg"
    elif file_name.endswith(".png"):
        return "image/png"
    elif file_name.endswith(".pdf"):
        return "application/pdf"
    elif file_name.endswith(".txt"):
        return "text/plain"
    elif file_name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

if __name__ == "__main__":
    print(media_type())
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various file names, including those with recognized extensions (gif, jpg, jpeg, png, pdf, txt, zip) and those with unrecognized extensions.
3. The program should output the corresponding media type for recognized extensions or the default "application/octet-stream" for unrecognized extensions.

## Sample Test Cases

1. **File Name:** happy.jpg
   **Media Type:** image/jpeg

2. **File Name:** document.pdf
   **Media Type:** application/pdf

## Additional Notes

Remember to save the `extensions.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.