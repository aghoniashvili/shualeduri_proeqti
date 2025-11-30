import json
import os



# Person კლასი სახელის მისანიჭებლად
class Person:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def show_info(self):
        return f"სახელი: {self.name}"



# Student კლასი მემკვიდრეობით Person-დან

class Student(Person):
    def __init__(self, name , student_number, grade):
        super().__init__(name)
        self.student_number = student_number
        self.grade = grade
    def get_student_number(self):
        return self.student_number
    
    def get_grade(self):
        return self.grade
    
    def set_grade(self, new_grade):
        if new_grade.upper() not in ['A' , 'B' , 'C' , 'D' , 'F']:
            print("შეფასება უნდა იყოს A, B, C, D ან F.")
            return False
        self.grade = new_grade.upper()
        return True
    
    def show_info(self):
        return f"სახელი: {self.name}, სტუდენტის ნომერი: {self.student_number}, შეფასება: {self.grade}  "
    


# მონაცემების სერიულიზაცია და დესერიულიზაცია JSON თვის
    def to_dict(self):
        return {
            "name": self.name,
            "student_number": self.student_number,
            "grade": self.grade
        }
    @staticmethod
    def from_dict(data):
        return Student(data["name"], data["student_number"], data["grade"])
    
# სტუდენტების მენეჯმენტის სისტემა , სტუდენტების მართვის და ფაილებთან ურთიერთობისთვის.
class StudentManagmentSystem:
    FILE_PATH = "studentebi.json"

    def __init__ (self):
        self.students = []
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.FILE_PATH):
            print("სტუდენტების მონაცემთა ფაილი ვერ მოიძებნა. ახალი ფაილი შეიქმნება.")
            return
        try:
            with open(self.FILE_PATH, "r") as f:
                data = json.load(f)
                self.students = [Student.from_dict(item) for item in data]
        except Exception as e:
            print(f"ფაილის წაკითხვისას დაფიქსირდა შეცდომა.{e}")
        
    def save_data(self):
        data = [s.to_dict() for s in self.students]
        try:
            with open(self.FILE_PATH, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"შეცდომა მონაცემების შენახვისას: {e}")

    def add_student(self):
        print("ახალი სტუდენტის დამატება:")
        name = input("შეიყვანეთ სახელი: ").strip()
        while True:
            try:

                num = int(input("შეიყვანეთ სტუდენტის ნომერი: ").strip())
                if any(s.get_student_number() == num for s in self.students):
                    print("სტუდენტის ნომერი უკვე არსებობს. სცადეთ სხვა ნომერი.")
                    continue
                break
            except ValueError:
                print("სტუდენტის ნომერი უნდა იყოს მთელი რიცხვი!")

        while True:
            grade = input("შეიყვანეთ შეფასება (A,B,C,D,F): ").strip().upper()
            if grade in ['A', 'B', 'C', 'D', 'F']:
                break
            else:
                print("შეფასება უნდა იყოს A, B, C, D ან F.")

        student = Student(name, num, grade)
        self.students.append(student)
        self.save_data()
        print("სტუდენტი წარმატებით დაემატა.")

    def show_all_students(self):
        if not self.students:
            print("სტუდენტები არ არის დამატებული.")
            return
        print("\n--- სტუდენტების სია ---")
        for s in self.students:
            print(s.show_info())
    
    def search_student(self):
        print("\n--- სტუდენტის ძებნა ნომრის მიხედვით ---")
        try:
            num = int(input("შეიყვანეთ სტუდენტის ნომერი: ").strip())
        except ValueError:
            print("სტუდენტის ნომერი უნდა იყოს მთელი რიცხვი!")
            return
        for student in self.students:
            if student.get_student_number() == num:
                print("სტუდენტი ნაპოვნია:")
                print(student.show_info())
                return
        print("სტუდენტი ვერ მოიძებნა აღნიშნული ნომრით.")
    
    def update_grade(self):
        print("\n--- სტუდენტის შეფასების განახლება ---")
        try:
            num = int(input("შეიყვანეთ სტუდენტის ნომერი: ").strip())
        except ValueError:
            print("სტუდენტის ნომერი უნდა იყოს მთელი რიცხვი!")
            return
        for student in self.students:
            if student.get_student_number() == num:
                print(f"მიმდინარე შეფასება: {student.get_grade()}")
                new_grade = input("შეიყვანეთ ახალი შეფასება (A,B,C,D,F): ").strip().upper()
                if student.set_grade(new_grade):
                    self.save_data()
                    print("შეფასება წარმატებით განახლდა.")
                return
        print("სტუდენტი ვერ მოიძებნა აღნიშნული ნომრით.")
    def delete_student(self):
        print("\n--- სტუდენტის წაშლა ---")
        try:
            num = int(input("შეიყვანეთ სტუდენტის ნომერი: ").strip())
        except ValueError:
            print("სტუდენტის ნომერი უნდა იყოს მთელი რიცხვი!")
            return
        for i, student in enumerate(self.students):
            if student.get_student_number() == num:
                del self.students[i]
                self.save_data()
                print("სტუდენტი წარმატებით წაიშალა.")
                return
            
        print("სტუდენტი ვერ მოიძებნა აღნიშნული ნომრით.")
    
    def menu(self):
        while True:
            print("\n--- სტუდენტების მართვის სისტემა ---")
            print("1. სტუდენტის დამატება")
            print("2. ყველა სტუდენტის ჩვენება")
            print("3. სტუდენტის ძებნა ნომრის მიხედვით")
            print("4. სტუდენტის შეფასების განახლება")
            print("5. სტუდენტის წაშლა")
            print("6. გამოსვლა")
            choice = input("შეიყვანეთ თქვენი არჩევანი (1-6): ").strip()
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.show_all_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.update_grade()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                print("პროგრამიდან გამოხვედით.")
                break
            else:
                print("ფუნქცია არ არსებობს სცადეთ თავიდან.")

# პროგრამის გაშვება
if __name__ == "__main__":
    sms = StudentManagmentSystem()
    sms.menu()


        
    



        
        