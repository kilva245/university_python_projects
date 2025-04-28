# Height Checker

This is a simple Python program that checks a person's height based on their gender.

## How It Works

- The user is asked to input their gender (`male` / `female`) and their height in centimeters.
- Based on the input:
  - For **women**, a height of 165 cm or above is considered tall.
  - For **men**, a height of 175 cm or above is considered tall.
  - Heights lower than the tall threshold but above a minimum value are considered normal.
  - Heights below the minimum value trigger a special response.
- If the gender input is invalid, an error message is shown.

## Example

```bash
Enter your gender: female
Enter your height(150cm): 170
you are tall!
