import requests
import sys
from twilio.rest import Client


# Twilio Account SID
ACCOUNT_SID = "XXXXX"

# Twilio Account Auth Token
AUTH_TOKEN = "XXXXX"

# Number on you Twilio Portal
SOURCE = "XXXXX"

# Number on which to receive the text
DEST = "XXXXX"

def url_ok(url):
    try:
        # Add a header with the User Agent to take care of sites which block
        # scraping, timeout after 10seconds
        r = requests.head(url, headers={'User-Agent': 'Custom'}, timeout=10)
        return (r.status_code == 200)
    except requests.exceptions.Timeout:
        print "Error!! Request Timed Out"
    except requests.ConnectionError:
        print "Error!! URL unreachable.  Possible network error."
    return False


def send_sms(url):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        to = DEST,
        from_ = SOURCE,
        body = "URL " + url + " is unreachable.")


def main(argv):
    if (len(argv) != 2):
        print("Incorrect Arguments.  Usage: python check_url.py <url>")
        return
    if (url_ok(argv[1])):
        print("URL is functional")
    else:
        send_sms(argv[1])

if __name__ == "__main__":
    main(sys.argv)
