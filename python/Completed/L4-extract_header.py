email = input("What is your email address?\n>")
email_split = email.split("@")
domain_slipt = email_split[1].split('.')
domain = domain_slipt[0]

print("Your domain name is {}".format(domain))
