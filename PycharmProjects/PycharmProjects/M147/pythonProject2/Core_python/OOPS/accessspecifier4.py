# -------------------------------------------------------------------------------------
# access specifiers:are the members of the class which will tell the user whether they
# can access it outside the class or not.

# Access specifiers are got classified into 3 types.
# 1. public
# 2. protected
# 3. private

# Public access specifiers:-
# These are the members of the class ,it is possible to access all these members outside the class.
# The members which are creating inside the class generally will be considered as public access specifiers.

# Protected access specifiers(_) :-
# These are members ,which should give the protection to the data store inside the class
# but in python protected members will not give any security (it will act like public members)

# Private access specifiers (__):-
# these are the members of the class ,which will not allow the to access them outside
# the class.
class spam:
    a = 89
    __b = 55

    print(__b)
s1 = spam()
print(s1.a)
print(s1.__b)