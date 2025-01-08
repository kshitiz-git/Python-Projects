import os
import pickle

class StudentRecords:
    def __init__(self, rollno=None, name=None, maths=None, eng=None, comp=None):
        self.rollno = rollno
        self.name = name
        self.sub = {'maths': maths, 'eng': eng, 'comp': comp}

def add_student():
    name = input("ENTER NAME OF THE STUDENT: ")
    rollno = int(input("ENTER ROLL NO OF THE STUDENT: "))
    maths = int(input("ENTER NO OF MATHS OF THE STUDENT: "))
    eng = int(input("ENTER NO OF ENGLISH OF THE STUDENT: "))
    comp = int(input("ENTER NO OF COMPUTER OF THE STUDENT: "))

    student = StudentRecords(rollno, name, maths, eng, comp)

    with open("class.dat", "ab") as fp:
        pickle.dump(student, fp)

def print_all_records():
    try:
        with open("class.dat", "rb") as fp:
            i = 1
            while True:
                student = pickle.load(fp)
                print(f"RECORD {i}:")
                print(f"NAME: {student.name}")
                print(f"ROLL NO: {student.rollno}")
                print(f"MATHS: {student.sub['maths']}")
                print(f"ENGLISH: {student.sub['eng']}")
                print(f"COMPUTER: {student.sub['comp']}\n")
                i += 1
    except EOFError:
        pass

def search_record():
    choice = int(input("\t\t:: ENTER CHOICE ::\n\t\t:: 1. BY NAME ::\n\t\t:: 2. BY ROLL NO ::\n"))
    if choice == 1:
        name = input("ENTER NAME: ").strip()
        found = False
        with open("class.dat", "rb") as fp:
            try:
                while True:
                    student = pickle.load(fp)
                    if student.name.strip() == name:
                        print(f"NAME: {student.name}")
                        print(f"ROLL NO: {student.rollno}")
                        print(f"MATHS: {student.sub['maths']}")
                        print(f"ENGLISH: {student.sub['eng']}")
                        print(f"COMPUTER: {student.sub['comp']}\n")
                        found = True
            except EOFError:
                pass
        if not found:
            print("Record not found.")
    elif choice == 2:
        roll_no = int(input("ENTER ROLL NO: "))
        found = False
        with open("class.dat", "rb") as fp:
            try:
                while True:
                    student = pickle.load(fp)
                    if student.rollno == roll_no:
                        print(f"NAME: {student.name}")
                        print(f"ROLL NO: {student.rollno}")
                        print(f"MATHS: {student.sub['maths']}")
                        print(f"ENGLISH: {student.sub['eng']}")
                        print(f"COMPUTER: {student.sub['comp']}\n")
                        found = True
            except EOFError:
                pass
        if not found:
            print("Record not found.")

def delete_record():
    choice = int(input("\t\t:: ENTER CHOICE ::\n\t\t:: 1. BY NAME ::\n\t\t:: 2. BY ROLL NO ::\n"))
    if choice == 1:
        name = input("ENTER NAME: ").strip()
        found = False
        students = []
        with open("class.dat", "rb") as fp:
            try:
                while True:
                    student = pickle.load(fp)
                    if student.name.strip() != name:
                        students.append(student)
                    else:
                        found = True
            except EOFError:
                pass
        if found:
            with open("class.dat", "wb") as fp:
                for student in students:
                    pickle.dump(student, fp)
            print("RECORD DELETED")
        else:
            print("Record not found.")
    elif choice == 2:
        roll_no = int(input("ENTER ROLL NO: "))
        found = False
        students = []
        with open("class.dat", "rb") as fp:
            try:
                while True:
                    student = pickle.load(fp)
                    if student.rollno != roll_no:
                        students.append(student)
                    else:
                        found = True
            except EOFError:
                pass
        if found:
            with open("class.dat", "wb") as fp:
                for student in students:
                    pickle.dump(student, fp)
            print("RECORD DELETED")
        else:
            print("Record not found.")

def delete_all_records():
    open("class.dat", "wb").close()
    print("SUCCESSFULLY DELETED ALL RECORDS")

def main():
    print("\t\t:: WELCOME ::")
    while True:
        print("\t\t:: ENTER CHOICE ::")
        print("\t\t:: 1. ENTER RECORD ::")
        print("\t\t:: 2. PRINT ALL RECORDS::")
        print("\t\t:: 3. SEARCH RECORD ::")
        print("\t\t:: 4. DELETE RECORD ::")
        print("\t\t:: 5. DELETE ALL RECORD ::")
        print("\t\t:: 6. EXIT ::\n")

        choice = int(input())

        if choice == 1:
            add_student()
        elif choice == 2:
            print_all_records()
        elif choice == 3:
            search_record()
        elif choice == 4:
            delete_record()
        elif choice == 5:
            delete_all_records()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("WRONG CHOICE")

if __name__ == "__main__":
    main()