# poneto

## archive-rip.py
This script takes the directory containing the website as a parameter and cleans out wayback machine references and replaces links with relative links.

Important: python archive-rip.py my/awesome/directory/ <-- Don't forget to add the "/" to the end.

optional parameter can be added to define a custom email address to use. By default, all emails will be changed to <...>@us.gmail.com

example: python archive-rip.py my/awesome/directory/ @custom.email.com
