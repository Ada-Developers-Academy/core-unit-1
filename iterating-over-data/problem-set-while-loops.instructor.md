# Instructor: Notes About Problem Set: While Loops

- `silly_sum`
    - The tests for this method rely on simulating user input with lists. If the student's solution reads too far, they will encounter a custom `ReadTooManyInputsError` (rethrown from the standard `StopIteration`). The hope is that the error name will be enough to point students in the right direction. So if they ask about this error, it means they aren't terminating their loop soon enough.
    - sample error output  
      `test_methods.ReadTooManyInputsError: Your loop has read beyond the end of the user input!`