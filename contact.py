class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send {}  order to {}".format(order, self.name))


c = Contact("Justin", "justin@conrads.com")
s = Supplier("RY", "ryenug@com")

print(c.name, c.email, s.name, s.email)

print(c.all_contacts)
print(s.all_contacts)
print(s.order("I need pu"))

for x in c.all_contacts:
    print()
