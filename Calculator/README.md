# Calculator 🧮

This is a simple yet versatile Python calculator with two modes:  
**Basic arithmetic** and **comparative operations**.

## Features

- Two calculator models:
  - **Basic**: Supports `+`, `-`, `*`, `/`, `**`, `%`
  - **Comparative**: Supports `>`, `<`, `>=`, `<=`, `==`, `!=`
- Handles invalid operator or model inputs gracefully

## How It Works

1. The user selects a model: `basic` or `comparative`
2. Inputs two numbers and an operator
3. The result is printed accordingly

## Example

```bash
Please choose a calculator model (basic/comparative): basic  
Enter first number: 5  
Enter + - * ** % / : **  
Enter second number: 3  
125.0
```

```bash
Please choose a calculator model (basic/comparative): comparative  
Enter first number: 10  
Enter > < >= <= == != : <  
Enter second number: 20  
True
```