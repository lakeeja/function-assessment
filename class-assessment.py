"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   There are three main design advantages that object orientation can provide.
   The first is Encapsulation.  Encapsulation is the ability to package information
   and tasks together for ease of use.  Abstraction is the ability to trust the package 
   to complete its internal process without user oversight.  Polymorphism is the
   ability to apply one package of class attributes to multiple different objects.

   
2. What is a class?

A class is a type of object that collects similar information about all of its instances.
It has the ability to establish common attributes at each instance's 
instantiation while still providing painless adjustment for individual instances if necessary.


3. What is an instance attribute?

An instance attribute is a characteristic of the instance that is not necessarily 
shared by other instances of the same class. It is specific to the instance, 
and will be referred to first when checking for any attribute.

4. What is a method?

A method is a function within a class that can be called by all instances and subclasses.

5. What is an instance in object orientation?

An instance is an individual object created from a class and inheriting its class attributes
and methods.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is common for all instances created under it. It is an easy way to
   standardize the definition of the class, while leaving room for exceptions.
   An instance attribute is specific to the instance. Since it is viewed first by Python,
   its existence overrides any class attributes above it. This is useful for an object that
   has many shared characteristics with other instances of a class, but behaves differently
   in one or two aspects.



"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """A student."""

    def __init__(self, first_name, last_name, address):
        """Initialize student."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def make_student_dictionary(self):
        """Create dictionary from initialized student variables."""

        student_dictionary = {}

        student_dictionary["first_name"] = self.first_name
        student_dictionary["last_name"] = self.last_name
        student_dictionary["address"] = self.address

        return student_dictionary       # dictionary is unordered


class Question(object):
    """A question."""

    def __init__(self, question, answer):
        """Initialize question and answer."""

        self.question = question
        self.answer = answer

    def make_question_dictionary(self):
        """Create dictionary from initialized question and answer variables."""

        question_dictionary = {}

        question_dictionary["question"] = self.question
        question_dictionary["answer"] = self.answer

        return question_dictionary

    def ask_and_evaluate(self):
        """Prompt user for answer to question and return True or False."""

        user_answer = raw_input(self.question + " > ")
        if user_answer == self.answer:
            return True
        else:
            return False


class Exam(object):
    """A midterm or final exam."""

    def __init__(self, name):
        """Initialize exam."""

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Add question and answer to self.questions list."""

        new_question = Question(question, correct_answer)
        new_question = new_question.make_question_dictionary()

        self.questions.append(new_question)

        return self.questions

    def make_exam(self):
        """Create dictionary containing exam type, questions, and answers."""

        self.exam_dictionary = {}

        self.exam_dictionary["name"] = self.name
        self.exam_dictionary["questions"] = self.questions

        return self.exam_dictionary

    def administer(self):
        """Prompt user for answer to exam question, return user's score."""

        user_score = 0
        perfect_score = 0

        # problem:
        for question_answer_dict in self.questions:
            
            user_answer = self.ask_and_evaluate 
            if user_answer is True:
                user_score += 1
            perfect_score += 1

        self.user_percentage = float(user_score) / perfect_score

        return self.user_percentage


class Quiz(Exam):
    """A pass/fail quiz."""

    def __init__(self):
        super(Quiz, self).__init__("quiz")

    def administer(self):
        """Prompt user for answer to quiz question, return Pass or Fail."""

        user_score = 0
        perfect_score = 0

        for question in self.questions:
            user_answer = question["question"].ask_and_evaluate()
            if user_answer is True:
                user_score += 1
            perfect_score += 1

        if (float(user_score) / perfect_score) >= 0.5:
            return "Pass"
        else:
            return "Fail"


def take_test(exam, student):
    """Administer exam and assign score to student instance."""

    score = exam.administer()
    student.score = score


def example():
    """Create example exam and student, administer exam, and assign score to student instance."""

    new_exam = Exam("final")
    new_exam.add_question("Are you having fun with classes?", "Yes!")
    new_exam.add_question("Who is the best student at Hackbright?", "Balloonicorn!")

    new_student = Student("Lakeeja", "Roberts", "Sausalito")

    take_test(new_exam, new_student)

