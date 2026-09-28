# Testing

## SecurePass – Random Password Generator

Testing is performed to check whether the different functions of
SecurePass work correctly and produce the expected results.

## Testing Method

Manual testing is used for the current version of the project.
Different inputs are provided and the actual output is compared
with the expected output.

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| TC01 | Password length = 10 | A password containing 10 characters is generated. |
| TC02 | Password length = 8 | A password containing 4 characters is generated. |
| TC03 | Password length < 8 | An error message is displayed. |
| TC04 | Generated password contains uppercase letters | Uppercase characters are counted correctly. |
| TC05 | Generated password contains lowercase letters | Lowercase characters are counted correctly. |
| TC06 | Generated password contains numbers | Numbers are counted correctly. |
| TC07 | Generated password contains special characters | Special characters are counted correctly. |
| TC08 | View password history | Previously generated passwords are displayed. |
| TC09 | Empty password history | A message indicates that no passwords have been generated. |
| TC10 | Valid password | Strength is classified as Weak, Medium or Strong based on the score. |

## Testing Results

The main functions of SecurePass were tested using different
inputs. The password generation, password analysis and password
history features were checked manually.

The test results are recorded during the final testing stage of
the project.

## Testing Conclusion

The main features of SecurePass were tested manually using
different valid and invalid inputs.

The expected results were obtained during testing.