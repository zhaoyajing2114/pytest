str="-----BEGIN RSA PRIVATE KEY----0H8kuq9eG+BRMHIJSWBNnAm2BLXoeSxcwCYTZ9AKH2m9X7suvuVa5Xg=-----END RSA PRIVATE KEY-----"
a = str.split("=")[0]
print(a)
print(a[-10:])