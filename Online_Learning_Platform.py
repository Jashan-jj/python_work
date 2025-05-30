class user:
    def __init__(self, name, email):
        self.name= name
        self.email= email

    def display_info(self):
        print("User Name: ", self.name)
        print("User email: ", self.email)

class instructor(user):
    def __init__(self, name, email, subject_expt):
        super().__init__(name, email)
        self.subject_expt= subject_expt
        self.contents = []
    
    def upload_content(self, content):
        self.contents.append(content)

    def display_info(self):
        super().display_info()
        print("Content: ", self.contents)

class coursecreator(instructor):
    def __init__(self, name, email, subject_expt):
        super().__init__(name, email, subject_expt)
        self.courses= {}
    
    def create_course(self, course_name, module):
        self.courses[course_name]= module

    def display_info(self):
        super().display_info()
        print("Courses with Modules: ", self.courses)

c = coursecreator("Jashan", "jas123@gmail.com", "data science")
c.upload_content("Sibject 1")
c.upload_content("Sibject 2")
c.create_course("Subject 1", ["chapter1", "chapter2"])
c.display_info()