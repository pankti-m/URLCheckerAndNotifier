This is a Python script which checks if a URL is up and sends a text message if
not.  Redirect(30x) is not treated as a success response.

Prerequisite: A twilio account where you can receive messages is required to use
this script.

Usage: "python check_url_status <url>"

Exceptions:
TimeoutException: The script throws a timeout exception if the server hosting
the webpage has not reponded in 10 seconds.

ConnectionError: ConnectionError is thrown in case of any network errors, such
as DNS failure, refused or broken connection etc.



References:
1. Python Requests Library
https://requests.readthedocs.io/en/master/user/quickstart/

2. Stack Overflow and other Q&A forums
