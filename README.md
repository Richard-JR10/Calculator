# Calculator Application

This is a Python-based calculator with support for various mathematical operations, including basic arithmetic and advanced functions like square root, factorial, and logarithm. The calculator is built using the Tkinter library for the GUI, and it has been converted into an executable using PyInstaller.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, and division.
- **Advanced Operations**:
  - Square root (`sqrt`)
  - Factorial (`fact(n)`)
  - Exponentiation
  - Logarithm (`log`)
  - Rounding (`ceil`, `floor`)
- **Error Handling**: Displays error messages for invalid inputs or operations.

## Installation

1. **Download the Executable**: You can download the pre-built executable from the [Releases](https://github.com/your-username/calculator/releases) section of this repository.
   
2. **Run the Executable**:
   - Double-click the `.exe` file to launch the calculator.
   - No installation is required.

3. **Alternatively, Run the Source Code**:
   - Clone the repository:
     ```bash
     git clone https://github.com/your-username/calculator.git
     cd calculator
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the Python script:
     ```bash
     python yourscript.py
     ```

## Usage

1. **Basic Calculations**: Enter the numbers and use the buttons for addition, subtraction, multiplication, or division.
   
2. **Factorial**: Use the syntax `fact(n)` where `n` is the number whose factorial you want to calculate.

3. **Advanced Functions**: Click the corresponding buttons for advanced operations like square root, logarithm, etc.

## Example

To calculate the factorial of 100, input:

```plaintext
fact(100)
```

For the square root of 25:

```plaintext
sqrt(25)
```

## Known Issues

- Very large numbers may exceed the computation limits for certain operations (like `fact(n)` with extremely large `n`). Use `sys.set_int_max_str_digits()` to increase limits if necessary.

## Building the Executable

To build the executable yourself, follow these steps:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the executable:
   ```bash
   pyinstaller --onefile -w yourscript.py
   ```

The resulting executable will be in the `dist` folder.

## License

This project is licensed under the MIT License.
## Authors

- [@Richard-JR10](https://github.com/Richard-JR10)

