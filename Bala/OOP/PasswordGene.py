import random
import string

class PasswordGene:

    def pwdgene(self, pwdlen):
        password = ''
        for x in range(pwdlen):
            password = password + \
                       random.choice(string.ascii_uppercase) + \
                       random.choice(string.ascii_lowercase) + \
                       random.choice(string.digits) + \
                       random.choice(string.punctuation)
        return password


if __name__ == '__main__':
    pwd_gene = PasswordGene()
    pwd_length = int(input("Enter the Length of your Password: "))
    pwd = pwd_gene.pwdgene(pwd_length)
    print(pwd)
