## Basic Programming

Write a method that reverses a String (without using a built-in language method like String#reverse in Ruby).  Ideally, do this without allocating memory for another String.

    e.g. string_reverse("the_string") => "gnirts_eht"

---

Write a program that finds the longest repeating substring in a given text.

    $ echo "phenomenal" | find_largest_repeating_string.rb
    en

---

Write a method that returns the n'th integer in the Fibonacci sequence.

    find_fib(1) => 0
    find_fib(5) => 3

---

Write a program that parses the access logs found in the *mediacast_access.log.gz* file and produces the following information:

  - A breakdown of request counts by response code.
  - A list of the top 5 URLs hit (with counts).
  - The average and median request size.

The logs in that file follow this format:

    <remote_ip> [<timestamp>] "<request>" <status> <size> <duration> "<referer>" "<user_agent>" "<forwarded_for>"
