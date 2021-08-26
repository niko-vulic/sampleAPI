# sampleAPI

This project will be used mainly for leetcode testing and learning how to implement APIs in Python. 
My goals will be as follows:
1. Perform some leetcode questions to familiarize myself with Python
2. From the existing frameworks I have in place, abstract it even further to be able to call questions and pass tests cases dynamically. 
3. Expose the above functionality from Q2 with an API with some basic verbs such as 
  - GET /question/{id} which will return the STDOUT from Q3 with the default test cases
  - POST /question/{id} with a request body which should be able to accept custom test cases and return a result
