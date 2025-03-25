# Requirements for Programming Assignments

### 1. Directory Structure
Students are not permitted to change directory structures, which includes adding new files, removing existing files, and moving files into another directory.

### 2. Program Structure
Students are also not permitted to change types of predefined functions.
All the functions they implement must have the same type as described in the module or module signatures.
However, students can change `let` to `let rec`, or add new functions in existing files, if needed.

### 3. Basic Software Engineering Practices
All source code must be clearly written following basic software engineering practices.
Especially,
- Formatting: All source code must be properly formatted using `ocamlformat`. Students are required to format their source code by using `make fmt` or setting their editor. Ill-formatted source code will be automatically rejected for grading.
- Warning: All source code must not have any warning. Students are required to correct all warnings in their source code before the final submission. For convenience, `make` does not strictly check warnings. However, `make test` will reject any source code with warnings.
- Coverage: Your source code must be well-tested. By running `make coverage`, your code coverage must exceed the specified threshold for each assignment. If your code coverage is below the threshold, your code will not be graded. You can add more tests in the `test` directory and modify the `test/dune` file to enhance coverage. Note that `make coverage` runs for only a minute, so you should maximize your test coverage within this time constraint.

### 4. Value-oriented Programming
We encourage the practice of value-oriented programming.
If you use `ref`, `while`, and `for` in your source code, your code will not be graded.
Refer to the [class introduction](https://github.com/prosyslab-classroom/cs348-information-security?tab=readme-ov-file#%EC%88%99%EC%A0%9C-homework) for more details.

### 5. Checking the Requirements
To check the requirements, we provide a `Makefile` that includes the following commands:
- `make test`: Check the source code for formatting, warnings, and value-oriented programming.
- `make coverage`: Check the source code for code coverage.
