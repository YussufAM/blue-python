import random
import string

randomLetter = random.choice('string.ascii_letters: ')

ec2_instance = input('how many ec2 instances do you want: ')
department = input('What department are you in: ')
for x in range (int(ec2_instance)):
    instance_Name = []
    char = string.ascii_letters + string.digits
    ec2_name = department + ''.join(random.choices(char, k=5))
    print(ec2_name)
