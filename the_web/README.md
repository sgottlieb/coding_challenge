## Web Programming

Web technology is the heart of RealGravity.  It is important to have a good understanding of how web technologies work, and how to use them.  These exercises are focussed on an understanding of HTTP, basic networking and data distribution around the web.

---

Write a program that uses a web API from the command line.  Doing something like a search would be easy, since it typically doesn't require authentication.  Here are a few examples, feel free to use something else if you have a favourite...

  - Use the Github API to search for repositories...
    - http://develop.github.com/p/repo.html
    - e.g. `$ github_search.rb "net/http"`

  - Use the StackOverflow API to search for questions/answers...
    - http://api.stackoverflow.com/1.1/usage

---

Write a web application that implements a basic URL shortening service.  Fulfill the following requirements:

  - anyone can submit a URL, and get a 'short link' back.
  - anyone can follow a shortened link, and get redirected to the longer link.

*Note that you do not have to persist anything, if you don't want to. Writing a small Sinatra application, and storing everything in memory is perfectly acceptable.*


