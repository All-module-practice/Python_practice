# Complete the function/method so that it returns the url with anything after the anchor (#) removed.

# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"

def remove_url_anchor(url):
    # TODO: complete
    newstr=""
    for c in url:
        if c=='#':
            break
        else:
            newstr+=c
    return newstr
