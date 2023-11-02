import pickle
import sys


print("--------SCHOOL SOFTWARE--------")
ph = '_________________________________________'
choice = 0


def main():
    print()
    print("1.Student")             
    print("2.Teacher")
    print("3.Help")
    print("4.About")
    print("5.Exit")
    choice = int(input('Enter choice:'))

    if choice== 1:
        student()

    elif choice == 2:
        passwd = 'sapsteacher'
        while True:
            if input('Enter password: ') == passwd:
                break
            else:
                print('Wrong password')
        teacher()

    elif choice==3:
        help1()

    elif choice==4:
        with open('about.txt','r') as f:
            print(f.read())
        print(ph)
        print(main())
        
    elif choice==5:
        sys.exit()
        
    else:
        print('Wrong choice')

def enterdetails():
    with open('STUDNTDATA.bin','ab') as f:
        Admno = int(input("Enter Admission no: "))
        Name = input('Enter Name: ')
        Class = input('Enter Class: ')
        Total_Marks = input('Enter Total marks:')
        Percentage = input('Enter Percentage: ')
        Grade = input('Enter Grade: ')
        d = {'Admno':Admno,'Name':Name,'class':Class,'Total marks':Total_Marks,'Percentage':Percentage,'Grade':Grade}
        pickle.dump(d,f)

def viewdetails(Admno):
    with open('STUDNTDATA.bin','rb') as fin:
        try:
            while True:
                dat = pickle.load(fin)
                #print(dat)
                if dat['Admno'] == Admno:
                    print("Name:",dat['Name'])
                    print("Class:",dat['class'])
                    print('Total Marks:',dat['Total marks'])
                    print('Percentage:',dat['Percentage'])
                    print('Grade:',dat['Grade'])
                    break
                    
        except:
            return('Wrong Admission Number')

def student():
    passwd='sapsstudent'
    while True:
      if input('Enter password: ') == passwd:
          break
      else:
        print('Wrong password')
        
    Admno = int(input("Enter admission number:"))
    print(ph)
    viewdetails(Admno)
    print(ph)
    main()


def teacher():
    print(ph)
    print('1.View student')
        print('2.View class')
    print('3.Add student')
    print('4.Return\n\n')
    choice = int(input('Enter choice: '))


    if choice == 1:
        Admno = int(input('Enter admission number:'))
        print("\n")
        viewdetails(Admno)
        teacher()

    if choice == 2:
        Class = input("Enter Class: ")
        print('\n\n')
        print("{:<17}{:>21}{:^10}{:^10}".format("Admno","Total Marks","Percentage","Grade"))
        #print("Admno",'%17s'%("Name"),'%21s'%("Total Marks"),'%10s'%("Percentage"),'%10s'%("Grade"))
        with open('STUDNTDATA.bin','rb') as f:
            try:
                while True:
                    dat = pickle.load(f)
                    if dat['class'] == Class:
                        print(dat['Admno'],'%21s'%(dat["Name"]),'%17s'%(dat["Total marks"]),'%10s'%(dat["Percentage"]),'%10s'%(dat["Grade"]))
            except:
                pass
        teacher()

            
            
    if choice == 3:
        continuechoice='Y'  
        while continuechoice in ["y","Y"]:
            enterdetails()
            continuechoice = input("Do you want to continue(Y/N): ")
        teacher()

    if choice == 4:
        main()
        


def display_help():
    print("\n")
    print("School Software Help Menu")
    print("1. View Contact Information")
    print("2. Frequently Asked Questions (FAQs)")
    print("3. Exit")

def view_contact_information():
    print("Contact Information:")
    print("School Name: XYZ School")
    print("Address: 123 Main Street, City")
    print("Phone: (123) 456-7890")
    print("Email: info@xyzschool.edu")

def answer_faq(faq_number):
    faqs = {
        1: {"question": "How do I reset my password?", "answer": "You can reset your password by visiting our website and clicking on the 'Forgot Password' link."},
        2: {"question": "How can I access my child's grades?", "answer": "You can access your child's grades by logging into the parent portal with your credentials."},
        3: {"question": "What are the school's office hours?", "answer": "The school's office hours are from 8:00 AM to 4:00 PM, Monday to Friday."},
        4: {"question": "How do I report an issue with the software?", "answer": "To report an issue, please contact our support team at support@xyzschool.edu."},
    }
    
    if faq_number in faqs:
        faq = faqs[faq_number]
        print(f"FAQ #{faq_number}: {faq['question']}")
        print(f"Answer: {faq['answer']}")
    else:
        print("FAQ not found. Please enter a valid FAQ number.")

def help1():
    while True:
        display_help()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_contact_information()
        elif choice == '2':
            while True:
                print("Frequently Asked Questions (FAQs)")
                print("1. How do I reset my password?")
                print("2. How can I access my child's grades?")
                print("3. What are the school's office hours?")
                print("4. How do I report an issue with the software?")
                print("5. Back to main menu")
                faq_choice = input("Enter the FAQ number or '5' to go back: ")
                
                if faq_choice == '5':
                    break
                elif faq_choice.isdigit():
                    answer_faq(int(faq_choice))
                else:
                    print("Invalid choice. Please enter a valid FAQ number.")
        elif choice == '3':
            print("Exiting the School Software Help Menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")





###########
main()
##########
