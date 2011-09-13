## Object Oriented Coding

These challenges are designed to test an understanding of Object-Oriented design and coding.  Please focus on strong Object-Oriented principles.

---

Write a class, in Ruby, that implements a **letter** grading system.  I.e., 'A+', 'A', 'A-', 'B+', ....

The constructor if the class should take a String, representing the grade, and the class should fulfill the following requirements.

  - It should validate the string provided.
  - It should compare properly.
    - e.g. `Grade.new('b') < Grade.new('A') => true`
  - It should sort properly.
    - e.g. `[Grade.new('b'), Grade.new('A'), Grade.new('F')].sort` should work as expected.
  - It should ignore case, and represent itself as upper-case (e.g., Grade.new('a+').to_s should equal 'A+').

---
