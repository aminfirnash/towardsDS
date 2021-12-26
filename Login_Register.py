# stage01- Registration
import re


store = open('store_cred.txt', 'r')
e = []
p = []
for line in store:
    a, b = line.split(', ')
    a = a.strip()
    b = b.strip()
    e.append(a)
    p.append(b)
data = dict(zip(e, p))
print(data)


def begin():
    global pswd
    global email
    start_ = input('Type L to Login or R to Register: ')
    final = start_.upper()
    if final == 'L':
        def login():
            email = input('Enter your email: ')
            if email in e:
                def ps_reenter():
                    pswd = input('Enter your password: ')
                    if pswd in p:
                        print('Credential match, Login Successful!')
                    elif pswd not in p:
                        print('Your password in incorrect.')
                        pswd_redo = input('T for Try again/ F for Forgot password: ')
                        pswd_redo = pswd_redo.upper()
                        if pswd_redo == 'T':
                            ps_reenter()
                        elif pswd_redo == 'F':
                            def forgot():
                                def psd1():
                                    while True:
                                        # pswd len 5-16. pswd - 1 spl char, 1 num, 1 lower, 1 upper.
                                        pattern = "(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?^[a-zA-Z0-9])[a-zA-Z0-9!@#$&%*-_\s]{5,16}"
                                        global pswd2
                                        pswd2 = input('Create new password: ')
                                        pattern = re.compile(r'')
                                        if len(pswd2) < 5 or len(pswd2) > 16:
                                            print('Password must be of length 5-16.')
                                        elif re.search(r'\d', pswd2) is None:
                                            print('Password must contain a number')
                                        elif re.search(r'[a-z]', pswd2) is None:
                                            print('Password must contain a lower case letter')
                                        elif re.search(r'[A-Z]', pswd2) is None:
                                            print('Password must contain a upper case letter')
                                        elif re.search(r'[!@#$&-*+.,]', pswd2) is None:
                                            print('Password must contain a special character')
                                        elif re.match(pattern, pswd2):
                                            print('Password is Valid')
                                            break
                                        else:
                                            print('Password is Invalid')
                                            psd1()

                                psd1()

                                def confirm_pswd():
                                    global pswd1
                                    pswd1 = input('Enter password again to confirm: ')
                                    if pswd2 != pswd1:
                                        print('Enter the correct password to match.')
                                        confirm_pswd()

                                    else:
                                        print('Password Match!')
                                        with open('store_cred.txt', 'rt') as rep:
                                            data = rep.read()
                                            for email in e:
                                                data = data.replace(pswd, pswd1)
                                        #db.write(email + ', ' + pswd1 + '\n')
                                        print('Great, Email Registered!')

                                confirm_pswd()

                            forgot()

                ps_reenter()
            else:
                print('Email not found. Try again or Register if new user.')
                begin()

        login()
    elif final == 'R':
        def register():
            pattern = '(^[a-zA-Z])+(\w)+([-_.])*(\w)*@(\w)+([-_.])*(\w)*\.([a-z])+$'
            # email starts with alpha, can contain spl char [-_.], should have @ and not immediate period, endswith alpha
            global email
            email = input('Enter your email: ')
            if email in e:
                print('Email already registered')
                begin()
            elif re.match(pattern, email):
                print('Proceeding to password!')

                def psd():
                    while True:
                        # pswd len 5-16. pswd - 1 spl char, 1 num, 1 lower, 1 upper.
                        pattern = "(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?^[a-zA-Z0-9])[a-zA-Z0-9!@#$&%*-_\s]{5,16}"
                        global pswd
                        pswd = input('Enter password: ')
                        pattern = re.compile(r'')
                        if len(pswd) < 5 or len(pswd) > 16:
                            print('Password must be of length 5-16.')
                        elif re.search(r'\d', pswd) is None:
                            print('Password must contain a number')
                        elif re.search(r'[a-z]', pswd) is None:
                            print('Password must contain a lower case letter')
                        elif re.search(r'[A-Z]', pswd) is None:
                            print('Password must contain a upper case letter')
                        elif re.search(r'[!@#$&-*+.,]', pswd) is None:
                            print('Password must contain a special character')
                        elif re.match(pattern, pswd):
                            print('Password is Valid')
                            break
                        else:
                            print('Password is Invalid')
                            psd()

                psd()
            else:
                print('Please, Enter a valid email address!')
                register()

        register()

        def confirm_pswd():
            global pswd1
            pswd1 = input('Enter password again to confirm: ')
            if pswd != pswd1:
                print('Enter the correct password to match.')
                confirm_pswd()
            else:
                print('Password Match!')
                db = open('store_cred.txt', 'a')
                db.write(email + ', ' + pswd1 + '\n')
                print('Great, Email Registered!')

        confirm_pswd()
    else:
        begin()

begin()
# email passed pswd passed with all needed entries
