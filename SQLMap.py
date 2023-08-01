################################# SQL MAP #################################

# What is SQL injection ?

# -> sql map automate the sql injection 




'''
# Techniques types :

    ● B: Boolean-based blind

    ● E: Error-based

    ● U: Union query-based

    ● S: Stacked queries

    ● T: Time-based queries

    ● Q: Inline queries


# --Crawl - scan web application entire parameter and return which para is vulnerable.


# --batch - select bydefault answer


# --technique - select specific like "U"


# --threads 5 - bydefault 1 maximum 10 (time save)


# --risk 1 - 
# >>> sqlmap -u http://testphp.vulnweb.com/ --crawl 2 --batch --risk 3


# Level - if vulnerability not show then we use level up
# >>> sqlmap -u http://testphp.vulnweb.com/ --crawl 2 --batch --level 1


# Verbosity - 0 : Show only Python tracebacks, error and critical messages.

'''


