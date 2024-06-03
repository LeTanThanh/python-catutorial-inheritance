from person import Person

class Employee(Person):
  def __init__(self, name, job_title) -> None:
    self.name = name
    self.job_title = job_title

  def greet(self):
    return f"Hi, it's {self.name}"
