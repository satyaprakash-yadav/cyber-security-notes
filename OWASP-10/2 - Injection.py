#   Injection :-


# Two types of Injection :-

# 1). SQL Injection :- This occurs when user controlled input is passed to SQL quries. As a results, an acttacker can pass in SQL queries to manipulate the outcome
#                      of such quries.


# 2). Command Injection :- This occurs when user input is passed to system commands.As a result, an acttacker is able to execute arbitary system commands on
#                          application servers.


# Preventing injection attacks :-

# allow list: when input is sent to the server, this input is compared to a list of safe input or characters. If the input is marked as safe,
#             then it is processed. Otherwise, it is rejected and the application throws an error.


# Stripping input: If the input contains dangerous characters, these characters are removed before they are processed.

