names=[]

DicCount={}

file_name='201811113001.log'

studentID=file_name.split('.')[0]

with open("text-file-process/log_files/"+file_name,encoding='utf-8') as f:
    for line in f:
        student_id = line.split(',')[1]
        student_id = student_id.strip()
        names.append(student_id)

names.sort()


for name in names:
     DicCount[name]=names.count(name)

print("The whole attendence records:")
print(DicCount)

print("Your attendence:")
print(DicCount["学号："+studentID])

