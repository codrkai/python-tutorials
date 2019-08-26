'''
    Tutorial 3 - Methods, Class, Lambdas, Import
    github.com/codrkai
'''

'''
    How to declare a method (ie. functions)
'''
def searchContacts(search):
    # this contacts variable is a dictionary
    # this dictionary also has another dictionary as it's values
    contacts = {
        "steve rogers": {
            "email":"captamerica@avengers.com",
            "phone":"555-555-5555"
        },
        "carol danvers": {
            "email":"captmarvel@avengers.com",
            "phone":"444-444-4444"
        }
    }

    # search for the contact
    # if it exists then print it out
    x = contacts.get(search)
    if x:
        print(x.get("email"))
    else:
        print('no records found')

# executing a method
searchContacts('carol danvers')


'''
    How to declare a class
'''
class SuperHeroes:
    def __init__(self):
        # Constructor
        self.email = ''
        self.phone = ''
        self.contacts = {}
        self.setContacts() # this method will be called when the class is initialized

    def setContacts(self):
        # this method is just to set up our contacts with a dictionary of values
        self.contacts = {
            "steve rogers": {
                "email":"captamerica@avengers.com",
                "phone":"555-555-5555"
            },
            "carol danvers": {
                "email":"captmarvel@avengers.com",
                "phone":"444-444-4444"
            }
        }

    def searchContacts(self, search):
        # this method will set our class variables if the contact is found
        x = self.contacts.get(search)
        if x:
            self.email = x.get('email')
            self.phone = x.get('phone')
        else:
            self.email = ''
            self.phone = ''
    
    def showContact(self):
        # this method will display our class variable values
        if self.email != '':
            print(f'Email is {self.email} and Phone is: {self.phone}')
        else:
            print('No record found.')

'''
    How to import a class
    this class file is located inside a folder called "inc"
    please do not put class files in your root folder
    put them in their own folder
'''
from inc.heroes import SuperHeroes

hero = SuperHeroes()
hero.searchContacts('steve rogers')
hero.showContact()


'''
    How to use Lambdas
'''
# this is a simple lambda
val = lambda a: a * 2
print(val(2))

def myLambdaMethod(y):
    return y * 4

# this lambda will call a custom method declared above
val = lambda a: myLambdaMethod(a)
print(val(2))


'''
github.com/codrkai
'''