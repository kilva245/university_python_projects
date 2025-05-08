# Calculator 🧮

This is a simple yet versatile Python calculator with two modes:  
**Basic arithmetic**, **comparative operations** and **engineering calculations**.

## Features

- Three calculator models:
  - **Basic**: Supports `+`, `-`, `*`, `/`, `**`, `%`
  - **Comparative**: Supports `>`, `<`, `>=`, `<=`, `==`, `!=`
  - **Engineering**: Supports advanced mathematical functions such as: 
    - `sin`, `cos`, `tan` `cot`
    - `pi`, `e`,   
    - `ceil`, `floor`, `log`, `log10`, `log2`
    - `round`, `sqrt`, `abs`
- Handles invalid operator or model inputs gracefully

## How It Works

1. The user selects a model: `basic`, `comparative` or `engineering`
2. Inputs two numbers and an operator (for basic/comparative) or one number (for engineering)
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

```bash
Please choose a calculator model (basic/comparative/engineering): engineering  
Enter your number: 3.14  
Enter [sin, cos, tan, cot, pi, e, ceil, floor, log, log10, log2, round, sqrt, abs]: sin  
0.00159265291
```