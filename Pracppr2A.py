#Task 1
total_hgt=0
total_mhgt=0
total_fhgt=0
count_female=0
count_male=0
fem_hgtchg=0
m_hgtchg=0
height_change=0
large_studhchg=0
large_malehchg=0
large_femhchg=0
smal_studhchg=0
smal_malehchg=0
smal_femhchg=0
name_ary=[]
stud_height=[]
stud_gender=[]
male_height=[]
female_height=[]
hgt_a3mths=[]
stud_hgtchg=[]
male_hgtchg=[]
female_hgtchg=[]

for i in range(0,4):
    name_input=str(input('Enter name of student: '))
    name_ary.append(name_input)
    
    gender_input= str(input('Enter gender of student[F/M]: '))
    gender_input = gender_input[0]
    while (gender_input != 'F') and (gender_input!= 'M'):
        print('Invalid input. Try again.')
        gender_input=str(input('Enter gender of student[F/M]: '))
        gender_input = gender_input[0]
    stud_gender.append(gender_input)
    height_input=int(input('Enter height of student[in cm]: '))
    while height_input>1000 or height_input<99:
        print('Height is out of range. Please input again')
        height_input=int(input('Enter height of student[in cm]: '))
    stud_height.append(height_input)
    total_hgt=total_hgt+height_input
    if gender_input == 'F':
        count_female=count_female+1
        female_height.append(height_input)
        total_fhgt=total_fhgt+height_input
    else:
        count_male=count_male+1
        male_height.append(height_input)
        total_mhgt=total_mhgt+height_input
    print("")
avrh_stud=total_hgt/4
avrh_male=total_mhgt/count_male
avrh_female=total_fhgt/count_female
print('Average height of all students:',avrh_stud)
print('Average height of female students:',avrh_female)
print('Average height of male students:',avrh_male)
print('')
#Task 2
ask_3mths=input('Has 3 months passed[Y/N]: ' )
while ask_3mths !='Y':
    print('3 months have not passed yet.')
    ask_3mths=input('Has 3 months passed[Y/N]: ' )  
else:
    name=''
    for w in range(0,4):
        name_2=str(input('Enter name of student: '))
        while (name_2 not in name_ary):
            print('Name does not exist. Try again')
            name_2=str(input('Enter name of student: '))
        else:
            height_2=int(input('Enter new height of student: '))
            while height_2>1000 or height_2<99:
                print('Height is out of range. Please input again')
                height_2=int(input('Enter new height of student[in cm]: '))
            midx= name_ary.index(name_2)
            hgt_read=stud_height[midx]
            hgt_chg=height_2-hgt_read
            height_change=height_change+hgt_chg
            stud_hgtchg.insert(midx,hgt_chg)
            hgt_a3mths.insert(midx, height_2)
            if hgt_chg>large_studhchg:
                large_studhchg=hgt_chg
                name_slarge=name_ary[midx]
            gender_2=stud_gender[midx]
            if gender_2=='F':
                fem_hgtchg=fem_hgtchg+hgt_chg
                female_hgtchg.insert(midx,hgt_chg)
                if hgt_chg>large_femhchg:
                    large_femhchg=hgt_chg
                    name_flarge=name_ary[midx]
            else:
                m_hgtchg=m_hgtchg+hgt_chg
                male_hgtchg.insert(midx,hgt_chg)
                if hgt_chg>large_malehchg:
                    large_malehchg=hgt_chg
                    name_mlarge=name_ary[midx]
            print("")
smal_studhchg=min(stud_hgtchg)
midx_2=stud_hgtchg.index(smal_studhchg)
name_ssmal=name_ary[midx_2]
smal_malehchg=min(male_hgtchg)
midx_3=male_hgtchg.index(smal_malehchg)
name_msmal=name_ary[midx_3]
smal_femhchg=min(female_hgtchg)
midx_4=female_hgtchg.index(smal_femhchg)
name_fsmal=name_ary[midx_4]

newavr_hgt=height_change/4
newavr_fhgt=fem_hgtchg/count_female
newavr_mhgt=m_hgtchg/count_male

#Task 3
print('Name','\t','Gender','\t','Initial height','\t','Height Change')
for p in range(0,len(name_ary)):
    print(name_ary[p],'\t',stud_gender[p],'\t','\t','\t',stud_height[p],'\t','\t','\t',stud_hgtchg[p])
    print('')

print('*Average height changes*')    
print ('Average height change for all students: ', newavr_hgt)
print('Average height change for males: ', newavr_mhgt )
print('Average height change for females: ', newavr_fhgt )
print('')
print('*Largest height changes*')
print('Largest height change in class is, ',large_studhchg,',',name_slarge )
print('Largest height change in males is, ', large_malehchg,',',name_mlarge)
print('Largest height change in females is, ', large_femhchg,',',name_flarge)
print('')
print('*Smallest height changes*')
print('Smallest height change in class is,',smal_studhchg,',',name_ssmal)
print('Smallest height change in males is,',smal_malehchg,',',name_msmal)
print('Smallest height change in females is,',smal_femhchg,',',name_fsmal)
