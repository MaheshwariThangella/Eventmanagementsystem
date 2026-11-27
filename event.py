import csv
class EMS:
    def __init__(self):
        self.event={}
        self.admin={}
        self.customer={}

    def create_csv(self):
        with open("admin.csv","w")as file:
            writer=csv.writer(file)
            writer.writerow(["name","email","password"])
        print("Admin CSV file created successfully")    

class Event:  
    def even(self):
        with open("event.csv","w")as file:
            writer=csv.writer(file)
            writer.writerow(["event_id","event_name","location","amount"])
        print("Event CSV file created successfully")
    def add_event(self):
        event_name=input("Enter Event Name:")
        location=input("Enter Event Location:")
        amount=input("Enter Event Amount:")
        event_id=100
        with open("event.csv","r") as file:
            reader=csv.reader(file)
            for i in reader:
                if i and i[0]!= "event_id":
                    event_id=int(i[0])
        event_id=event_id+1            
        with open("event.csv","a")as file:
            writer=csv.writer(file)
            
            writer.writerow([event_id,event_name,location,amount])
            print("Event Added Successfully with event_id :",event_id)
    def view_event(self):
        with open("event.csv","r") as file:
            reader=csv.reader(file)
            for i in reader:
                if len(i)==4:
                    print(i[0],i[1],i[2],i[3])            
    
    def update_event(self):
        event_id = input("Enter event_id to update: ").strip()

        events = []

        with open("event.csv", "r") as file:
            reader = csv.reader(file)

            for i in reader:
                events.append(i)

        for i in events:
            if len(i) == 4 and i[0].split() == event_id.split():

                print("1. Update Event Name")
                print("2. Update Location")
                print("3. Update Amount")
                print("4. Update All Details")

                choose = input("Enter your choice: ")

                if choose == "1":
                    i[1] = input("Enter new Event Name: ")

                elif choose == "2":
                    i[2] = input("Enter new Location: ")

                elif choose == "3":
                    i[3] = input("Enter new Amount: ")

                elif choose == "4":
                    i[1] = input("Enter new Event Name: ")
                    i[2] = input("Enter new Location: ")
                    i[3] = input("Enter new Amount: ")

                else:
                    print("Please choose the correct number")
                    return

                with open("event.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(events)

                print("Event updated successfully!")
                break

        else:
            print("Event ID not found!")
   
    def delete_event(self):
        event_id = input("Enter event_id to delete: ").strip()
        eventss = []     
        with open("event.csv", "r") as file:
            reader = csv.reader(file)
            for i in reader:
                eventss.append(i)
        for i in eventss:    
            if len(i) == 4 and i[0].split() == event_id.split():
                eventss.remove(i)
                with open("event.csv", "w",newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(eventss)               
                print("Event deleted successfully!")
                return
        else:
            print("Event ID not found!")
    def view_customers(self):
        with open("customer.csv", "r") as file:
            reader = csv.reader(file)

            for i in reader:
                if len(i) == 3:
                    if i[1] != "email":
                        print("Customer Name:", i[0])
                        print("Email:", i[1])    
    def view_bookings(self):
        with open("bookings.csv", "r") as file:
            reader = csv.reader(file)
            for i in reader:
                if len(i) == 6:
                    if i[1] != "customer_email":
                        print("Customer Name:", i[0])
                        print("Customer Email:", i[1])
                        print("Event ID:", i[2])
                        print("Event Name:", i[3])
                        print("Event Date:", i[4])
                        print("Amount:", i[5])                    
class Admin:
    def registration(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
        with open ("admin.csv","a")as file:
            writer=csv.writer(file)
            writer.writerow([self.name,self.email,self.password])
        print("Admin Registred successfully")

    
    def Login(self):
        email = input("Enter your Existing email id: ")
        password = input("Enter your password: ")

        with open("admin.csv", "r") as file:
            reader = csv.reader(file)

            for i in reader:
                if len(i) == 3:
                    if email == i[1] and password == i[2]:
                        print("Login successful")
                        return True

        print("Invalid email and password")
        return False

class Customer(Event):
    def registration(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
        with open ("customer.csv","a")as file:
            writer=csv.writer(file)
            writer.writerow([self.name,self.email,self.password])
        print("Customer Registred successfully")
       
    
    def Login(self):
        email = input("Enter your Existing email id: ")
        password = input("Enter your password: ")
    
        with open("customer.csv", "r") as file:
            reader = csv.reader(file)
    
            for i in reader:
                if len(i) == 3:
                    if email == i[1] and password == i[2]:
                        self.name = i[0]
                        self.email = i[1]
                        print("Login successful")
                        return True
    
        print("Invalid email and password")
        return False
    def search_event(self):
        search=input("Search event here:")
        ev=[]
        with open("event.csv","r")as file:
            reader=csv.reader(file)
            for i in reader:
                if len(i) == 4:
                    if i[1].lower() == search.lower():
                        print(i[0], i[1], i[2], i[3])
                        break
            else:
                print("Search event not found")   
    def book_event(self):
        event_id = input("Enter Event ID: ")

        with open("event.csv", "r") as file:
            reader = csv.reader(file)

            for i in reader:
                if len(i) == 4:
                    if i[0] == event_id:

                        event_name = i[1]
                        amount = i[3]

                        event_date = input("Enter Event Date: ")

                        with open("bookings.csv", "a", newline="") as file:
                            writer = csv.writer(file)

                            writer.writerow([
                                self.name,
                                self.email,
                                event_id,
                                event_name,
                                event_date,
                                amount
                            ])

                        print("Event Booked Successfully!")
                        return

        print("Event ID Not Found!")                 
    def view_my_bookings(self):
        with open("bookings.csv", "r") as file:
            reader = csv.reader(file)

            for i in reader:
                if len(i) == 6:
                    if i[1] == self.email:

                        print("Event ID:", i[2])
                        print("Event Name:", i[3])
                        print("Event Date:", i[4])
                        print("Amount:", i[5])
    def cancel_booking(self):
        event_id = input("Enter Event ID to cancel: ")

        bookings = []

        with open("bookings.csv", "r") as file:
            reader = csv.reader(file)

            for i in reader:
                bookings.append(i)

        for i in bookings:
            if len(i) == 6:
                if i[1] == self.email and i[2] == event_id:

                    bookings.remove(i)

                    with open("bookings.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(bookings)

                    print("Booking Cancelled Successfully!")
                    return

        print("Booking Not Found!")
while True:
    print("1.Admin")
    print("2.Customer")
    print("3.Exit")
    choice=input("enter your choice:")
    if choice =="1":
        print("Welcome to event planner")
        while True:
            print("1.Admin Registration")
            print("2.Admin Login")
            print("3.Exit")
            select=input("Enter your choice:")
            if select=="1":
                name=input("Enter Admin Name:")
                email=input("Enter Admin Email Address:")
                password=input("Enter Admin Password:")
                a=Admin()
                a.registration(name,email,password)
            
            elif select == "2":
                a = Admin()

                result = a.Login()

                if result == True:
                    while True:
                        print("1.Add Event")
                        print("2.View Events")
                        print("3.Update Event")
                        print("4.Delete Event")
                        print("5.View Customers")
                        print("6.View Bookings")
                        print("7.Logout")

                        pick = input("Enter your choice: ")

                        if pick == "1":
                            e = Event()
                            e.add_event()

                        elif pick == "2":
                            e = Event()
                            e.view_event()

                        elif pick == "3":
                            e = Event()
                            e.update_event()

                        elif pick == "4":
                            e = Event()
                            e.delete_event()

                        elif pick == "5":
                            print("Lets view customers:")
                            e=Event()
                            e.view_customers()
                        
                        elif pick == "6":
                            print("The Events Bookings:")
                            e=Event()
                            e.view_bookings()
                        
                        elif pick == "7":
                            print("Returning to Admin Menu")
                            break
                        
                        else:
                            print("Invalid choice")

                else:
                    print("Please login again") 
            elif select=="3":
                print("Retuning to main menu")
                break
            else:
                print("invalid choice")            
    elif choice=="2":
        print("Welcome to event planner")
        while True:
            print("1.Customer Registration")
            print("2.Customer Login")
            print("3.Exit")
            select=input("Enter your choice:")
            if select=="1":
                name=input("Enter Customer Name:")
                email=input("Enter Customer Email Address:")
                password=input("Enter Customer Password:")
                a=Customer()
                a.registration(name,email,password)
            elif select=="2":
                a=Customer()
                result = a.Login()
                if result== True:
                    while True:
                        print("1.View Events")
                        print("2.Search Events")
                        print("3.Book Events")
                        print("4.View my Bookings")
                        print("5.Cancel My Booking")
                        print("6.Logout")
                        chooose =input("Enter your choice:")
                        if chooose=="1":
                            print("The Events are:")
                            e=Event()
                            e.view_event()
                        elif chooose  =="2":
                            print("Your searched event:")
                            a.search_event()
                        elif chooose =="3":
                            print("Your Booked events are:")
                            a.book_event()
                        elif chooose =="4":
                            print("Your booked events are:")
                            a.view_my_bookings()
                        elif chooose=="5":
                            print("Your event canceled")   
                            a.cancel_booking()
                        elif chooose=="6":
                            print("Logout Sucessfully")
                            break
                        else:
                            print("Invalid choice")

                else:
                    print("Please login again") 
            elif select=="3":
                print("Retuning to main menu")
                break
            else:
                print("invalid choice") 
    elif choice=="3":
        print("Thank you")
        break
    else:
        print("Invalid Choice")
