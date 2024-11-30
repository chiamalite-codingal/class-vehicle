#create a class
class students:
    platform = "codingal"
    course = "python"
    def __init__(self,country,name,favcolor):
        self.country = country
        self.name = name
        self.favcolor = favcolor
#objects
stu1 = students("Bangaladesh","tasheen","white")
stu2 = students("Portugal","vedanshi","green")
stu3 = students("Africa","Chiamalite","pink")
print("My student names are: 1.{} 2.{} 3.{}".format(stu1.name,stu2.name,stu3.name))