import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import *
from ttkbootstrap import *
import pprint as pprint

root = tb.Window(themename="superhero")
root.title("Data entry")

frame = tb.Frame(root)
frame.pack()

def SubmitData():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    title = title_comboBox.get()
    age = my_spinbox.get()
    nationality = nationality_comboBox.get()
    course = Course_Completed.get()
    semester = Semester_Completed.get()
    registered = var1.get()
    terms = var2.get()
    if var1.get() == 1:
        registered = True
    if var2.get() == 1:
        terms = True
    else:
         registered = False
         terms = False
    first_name_entry.delete(0,END)
    last_name_entry.delete(0,END)
    title_comboBox.delete(0,END)
    age = my_spinbox.delete(0,END)
    nationality_comboBox.delete(0,END)
    Course_Completed.delete(0,END)
    Semester_Completed.delete(0,END)

    print(f'''
            Name: {title} {first_name} {last_name}
            Nationality: {nationality}
            Age: {age}
            Course Completed{course}
            Semester Completed{semester}
            Registered  {registered}
            Accepted Terms and Conditions: {terms}''')


#Saving User info
user_info_frame = tb.Labelframe(frame,text="User Information")
user_info_frame.grid(row=0,column=0)

first_name_label = tb.Label(user_info_frame,text="First Name")
first_name_label.grid(row=0,column=0)

last_name_label = tb.Label(user_info_frame,text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry = tb.Entry(user_info_frame,bootstyle="info")
first_name_entry.grid(row=1,column=0)

last_name_entry = tb.Entry(user_info_frame,bootstyle="info")
last_name_entry.grid(row=1,column=1)

title_label = tb.Label(user_info_frame,text="Title")
title_label.grid(row=0,column=2)
titles = ["","Mr.","Ms.","Dr."]
title_comboBox = tb.Combobox(user_info_frame,values=titles,bootstyle="info",state="readonly")
title_comboBox.grid(row=1,column=2)

age_label = tb.Label(user_info_frame,text="Age")
age_label.grid(row=2,column=0)

my_spinbox = tb.Spinbox(user_info_frame,bootstyle="info",from_=0, to=10,)
my_spinbox.grid(row=3,column=0)

NATIONALITIES_list = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean']

nationality_Label = tb.Label(user_info_frame,text="Nationality")
nationality_Label.grid(row=2,column=1)
nationality_comboBox = tb.Combobox(user_info_frame,values=NATIONALITIES_list,bootstyle="info",state="readonly")
nationality_comboBox.grid(row=3,column=1)
nationality_comboBox.set('Afghan')

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

courses_frame = tb.Labelframe(frame)
courses_frame.grid(row=1,column=0,sticky="news")

registered_label = tb.Label(courses_frame,text="Registration Status")
registered_label.grid(row=0,column=0)

var1 = IntVar()
registered_check = tb.Checkbutton(courses_frame,bootstyle = "info",text="Currently Registered",
            variable=var1,
            onvalue=1,
            offvalue=0,
            )
registered_check.grid(row=1,column=0,padx=10,pady=10)

Course_Completed = tb.Label(courses_frame,text="#Course Completed")
Course_Completed.grid(row=0,column=1)

Course_Completed = tb.Spinbox(courses_frame,bootstyle="info",from_=0, to=100,state="readonly")
Course_Completed.grid(row=1,column=1)

Semester_Completed = tb.Label(courses_frame,text="#Semester Completed")
Semester_Completed.grid(row=0,column=2)

Semester_Completed = tb.Spinbox(courses_frame,bootstyle="info",from_=0, to=100,state="readonly")
Semester_Completed.grid(row=1,column=2) 

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)


terms_frame = tb.Labelframe(frame,text="Terms and conditions")
terms_frame.grid(row=2,column=0,sticky="news",padx=10,pady=10)


var2 = IntVar()
registered_term_check = tb.Checkbutton(terms_frame,bootstyle = "info",text="I accept terms and conditions",
            variable=var2,
            onvalue=1,
            offvalue=0,
            )
registered_term_check.grid(row=1,column=0,padx=10,pady=10)

button_submit = tb.Button(frame,text="Submit Data",bootstyle="info",command=SubmitData)
button_submit.grid(row=3,column=0,padx=10,pady=10,sticky="news")

root.mainloop()