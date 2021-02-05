import random, string

class PasswordGene:

    def pwdgene(self, pwdlen):
        password = ''

        for x in range(0, 4):
            password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
        for y in range(pwdlen - 4):
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

        return password
