# This is an example and test file
# In this file we illustrate how to use google functions file.

import Google_Function as google

response = google.search("test", type = None);

for r in response:
    print(r)
