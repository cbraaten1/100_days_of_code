# Don't change the code below 
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Don't change the code above


#Write your code below this row
acc_height = 0
div = 0

for height in student_heights:
    acc_height = acc_height + height
    div = div + 1
    
the_avg = round(acc_height / div)
print(the_avg)