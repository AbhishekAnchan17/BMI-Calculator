from mysql.connector import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from datetime import *


f=("courier", 20, "bold")

#splash screen

splash_window=Tk()
splash_window.geometry("400x400")
splash_window.title("Welcome")
splash_label = Label(splash_window, text= "BMI Calci" + "\n" +"by Kamal Sir", font=('Calibri', 50, 'italic'),fg="red")
splash_label.pack()

d=datetime.now()	
hour=d.hour

if hour<12:
	res=str(d)+str("Good Morning")
elif hour<17:
	res=str(d)+str("Good Afternoon")
else:
	res=str(d)+str("Good Evening")


def main():
	

	def f1():
	
		cal_window.deiconify()
		main_window.withdraw()

	
	def f2():
	
		main_window.deiconify()
		cal_window.withdraw()

	def f3():
	
		conv_window.deiconify()
		cal_window.withdraw()


	def f4():
	
		cal_window.deiconify()
		conv_window.withdraw()
		
		
		

	def f5():

		#name

		name=cw_ent_name.get()
		if (name==""):
			showerror("Name issue", "name should not be empty")
			cw_ent_name.delete(0, END)
			cw_ent_name.focus()
			return
		if (len(name)<2):
			showerror("Name issue", "name cannot be only 1 letter")
			cw_ent_name.delete(0, END)
			cw_ent_name.focus()
			return

		if  not name.isalpha():
			showerror('Error', 'Name cannot be numeric')
			cw_ent_name.delete(0,END)
			cw_ent_name.focus()
			return
		

		#age
		age=cw_ent_age.get()
		if (age==""):
			showerror("Error", "age cannot be empty")
			cw_ent_age.delete(0, END)
			cw_ent_age.focus()
			return
		if (not age.isdigit()) or (int(age)<=1):
			showerror("Error", "Age should contain only positive numbers")
			cw_ent_age.delete(0, END)
			cw_ent_age.focus()
			return
		if (len(age)>3):
			showerror("Error", "Age is more than 100")
			cw_ent_age.delete(0, END)
			cw_ent_age.focus()
			return

		#phone
		phone=cw_ent_ph.get()
		if (phone==""):
			showerror("Error", "phone number cannot be empty")
			cw_ent_ph.delete(0, END)
			cw_ent_ph.focus()
			return
		if (not phone.isdigit()) or (int(phone)<=1):
			showerror("Error", "phone number contain positive numbers")
			cw_ent_ph.delete(0, END)
			cw_ent_ph.focus()
			return
		if (not len(phone)==10):
			showerror("Error", "Phone number should contain 10 numbers")
			cw_ent_ph.delete(0, END)
			cw_ent_ph.focus()
			return

		#height
		height=cw_ent_he.get()
		if (height==""):
			showerror("Error", "Height cannot be empty")
			cw_ent_he.delete(0, END)
			cw_ent_he.focus()
			return
		if (not height.isdigit()):
			showerror("Error", "Height should contain only positive numbers")
			cw_ent_he.delete(0, END)
			cw_ent_he.focus()
			return
		if (float(height)<60):
			showerror("Error", "Height cannot be less than 60 cm")
			cw_ent_he.delete(0, END)
			cw_ent_he.focus()
			return
		if (float(height)==0):
			showerror("Error", "Height cannot be 0")
			cw_ent_he.delete(0, END)
			cw_ent_he.focus()
			return
		if (float(height)>250):
			showerror("Error", "Invalid Height")
			cw_ent_he.delete(0, END)
			cw_ent_he.focus()
			return

		#weight
		weight=cw_ent_we.get()
		if (weight==""):
			showerror("Error", "weight cannot be empty")
			cw_ent_we.delete(0, END)
			cw_ent_we.focus()
			return
		if (not weight.isdigit()):
			showerror("weight issue", "Weight should contain only positive numbers")
			cw_ent_we.delete(0, END)
			cw_ent_we.focus()
			return
		if (float(weight)==0):
			showerror("Error", "Weight cannot be 0")
			cw_ent_we.delete(0, END)
			cw_ent_we.focus()
			return
		if (float(weight)>250):
			showerror("Error", "Invalid weight")
			cw_ent_we.delete(0, END)
			cw_ent_we.focus()
			return

		heightm= float(height )/ 100.0
		bmi=float(weight)/float(heightm**2)
		bmif=round(bmi,2)
		if bmi<18.5:
			resc="underweight"
			res="ur bmi is "+str(bmif)+" "+"your category is underweight"
		elif bmi>18.5 and bmi<24.9:
			resc="normal"
			res="ur bmi is "+str(bmif)+" "+"your category is normal catgeory"
		else:
			resc="obesity"
			res="ur bmi is "+str(bmif)+" "+"your category is under obesity category"
		showinfo("BMI", res)
		con=None
		try:
			con=connect(host="localhost",user="root",password="abc456",database="kita", allow_local_infile=True)
			cursor=con.cursor()
			sql="insert into users values('%s', '%d', '%d','%s','%f','%d','%f','%s')"
			name=cw_ent_name.get()
			age=int(cw_ent_age.get())
			phone=int(cw_ent_ph.get())
			if ge.get()==1:
				gender="Male"
			else:
				gender="Female"
			height=int(cw_ent_he.get())
			weight=int(cw_ent_we.get())
			cursor.execute(sql%(name,age,phone,gender,height,weight,bmif,resc))
			con.commit()
			cw_ent_name.delete(0,END)
			cw_ent_age.delete(0,END)
			cw_ent_ph.delete(0,END)
			cw_ent_he.delete(0,END)
			cw_ent_we.delete(0,END)
			cw_ent_name.focus()
		except Exception as e:
			showerror("failure",str(e))
			con.rollback()


	con=None
	con=connect(host="localhost",user="root",password="abc456",database="kita", allow_local_infile=True)
	cursor=con.cursor()
	query="select count(*) from users"
	cursor.execute(query)
	resf=cursor.fetchone()
	total_rows=resf[0]
	countf="count= "+str(total_rows)





	def f6():
	
		feet=conv_ent_feet.get()
		if (feet==""):
			showerror("Error", "feets cannot be empty")
			conv_ent_feet.delete(0, END)
			conv_ent_feet.focus()
			return
		if (not feet.isdigit()) or (int(feet)<2) or (int(feet)>7) :
			showerror("Error", "feets should be only number and between 2 to 7")
			conv_ent_feet.delete(0, END)
			conv_ent_feet.focus()
			return

		inches=conv_ent_inc.get()
		if (inches==""):
			showerror("Inches value issue", "inches cannot be empty")	
			conv_ent_inc.delete(0, END)
			conv_ent_inc.focus()
			return
		if (not inches.isdigit()) or (int(inches)<0):
			showerror("Error", "Invalid inches should only contain numbers")
			conv_ent_inc.delete(0, END)
			conv_ent_inc.focus()
			return
		if (int(inches)>11):
			showerror("Error", "Inches cannot be more than 11")
			conv_ent_inc.delete(0, END)
			conv_ent_inc.focus()
			return

		cm=int(feet)*30.48+int(inches)*2.54
		me=round(cm,0)
		res="Your height in centimetres is "+str(me)
		showinfo("Height in centimetres",res)
		conv_ent_feet.delete(0,END)
		conv_ent_inc.delete(0,END)
		conv_ent_feet.focus()
	
	def f7():
	
		view_window.deiconify()
		main_window.withdraw()
		vw_st_data.delete(1.0, END)
		info=""
		con=None
		try:
			con=connect(host="localhost",user="root",password="abc456",database="kita", allow_local_infile=True)
			cursor=con.cursor()
			sql="select name,age,phone,gender,bmi from users"
			cursor.execute(sql)
			data=cursor.fetchall()
			for d in data:
				info=info+"name= "+str(d[0])+"\n"+"age= "+str(d[1])+"\n"+"phone= "+str(d[2])+"\n"+"gender= "+str(d[3])+"\n"+"bmi= "+str(d[4])+"\n"+"******************************"+"\n"
			vw_st_data.insert(INSERT, info)
		except Exception as e:
			showerror("Issue", str(e))
		finally:
			if con is not None:
				con.close()




	def f8():
		view_window.withdraw()
		main_window.deiconify()

	def f9():
		con=None
		try:	
			con=connect(host="localhost",user="root",password="abc456",database="kita", allow_local_infile=True)
			with open('p.sql', 'r') as f:
    				with con.cursor() as cursor:
        					cursor.execute(f.read(), multi=True)
			showinfo("success","Data is exported to D:\ENT\My_Files\Projects\BMI_Calculator\bmidata1")	
		except Exception as e:
			showerror("Failure", str(e))
			con.rollback()
		if con is not None:
			con.close()

	splash_window.destroy()



	
	
#main window:

	main_window = Tk()
	main_window.title("BMI Calculator")
	main_window.geometry("500x500")
	main_window.configure(bg='gold')	

	mw_btn_cal=Button(main_window, text="Calculate BMI", font=f, width=20,command=f1)
	mw_btn_view=Button(main_window, text="View History", font=f, width=20,command=f7)
	mw_btn_export=Button(main_window, text="Export data", font=f, width=20,command=f9)

	mw_btn_cal.pack(pady=10)
	mw_btn_view.pack(pady=10)
	mw_btn_export.pack(pady=10)


	text1=Text(main_window,font=f)
	text1.place(x=70, y=250, height=70, width=370)
	text1.insert(END,res)
	text1.configure(state="disabled")
	text1.get(1.0,END)

	text2=Text(main_window,font=f)
	text2.place(x=70, y=350, height=70, width=370)
	text2.insert(END,countf)
	text2.configure(state="disabled")
	text2.get(1.0,END)


	#calculate
	cal_window=Toplevel(main_window)
	cal_window.title("BMI Calculator")
	cal_window.geometry("900x500")
	cal_window.configure(bg='light blue')

	cw_lbl_name=Label(cal_window, text="Enter name ", font=f)
	cw_lbl_name.place(x=15,y=15)

	cw_ent_name=Entry(cal_window,bd=5,font=f)
	cw_ent_name.place(x=180,y=15)

	cw_lbl_age=Label(cal_window, text="Enter age  ", font=f)
	cw_lbl_age.place(x=15,y=80)

	cw_ent_age=Entry(cal_window,bd=5,font=f)
	cw_ent_age.place(x=170,y=80)

	cw_lbl_ph=Label(cal_window, text="Enter phone ", font=f)
	cw_lbl_ph.place(x=15,y=145)

	cw_ent_ph=Entry(cal_window,bd=5,font=f)
	cw_ent_ph.place(x=190,y=145)

	cw_lbl_ge=Label(cal_window, text="Gender", font=f)
	cw_lbl_ge.place(x=15,y=210)

	ge=IntVar()
	ge.set(1)
	cw_rb_male=Radiobutton(cal_window, text="Male",font=f,value=1,variable=ge)
	cw_rb_female=Radiobutton(cal_window, text="Female",font=f,value=2,variable=ge)

	cw_rb_male.place(x=150,y=210)
	cw_rb_female.place(x=250,y=210)

	cw_lbl_he=Label(cal_window, text="Enter Height in cms", font=f)
	cw_lbl_he.place(x=15,y=275)

	cw_ent_he=Entry(cal_window,bd=5,font=f)
	cw_ent_he.place(x=320,y=275)

	cw_btn_convert=Button(cal_window, text="Convert", font=f, width=10,command=f3)
	cw_btn_convert.place(x=700,y=275)

	cw_lbl_we=Label(cal_window, text="Enter Weight in kg", font=f)
	cw_lbl_we.place(x=15,y=340)

	cw_ent_we=Entry(cal_window,bd=5,font=f)
	cw_ent_we.place(x=320,y=340)

	cw_btn_cal=Button(cal_window, text="Calculate", font=f, width=10,command=f5)
	cw_btn_cal.place(x=15,y=405)

	cw_btn_back=Button(cal_window, text="Back", font=f, width=10, command=f2)
	cw_btn_back.place(x=220,y=405)

	cal_window.withdraw()

	#convert

	conv_window=Toplevel(main_window)
	conv_window.title("Height Convertor")
	conv_window.geometry("900x500")
	conv_window.configure(bg='light green')

	conv_lbl_info=Label(conv_window, text="Enter your height", font=f)
	conv_lbl_info.place(x=300,y=10)

	conv_lbl_feet=Label(conv_window, text="Feet", font=f)
	conv_lbl_feet.place(x=100,y=75)

	conv_ent_feet=Entry(conv_window,bd=5,font=f)
	conv_ent_feet.place(x=100,y=140)

	conv_lbl_inc=Label(conv_window, text="Inches", font=f)
	conv_lbl_inc.place(x=100,y=205)

	conv_ent_inc=Entry(conv_window,bd=5,font=f)
	conv_ent_inc.place(x=100,y=270)

	conv_btn_cal=Button(conv_window, text="Convert", font=f, width=10,command=f6)
	conv_btn_cal.place(x=250,y=335)

	conv_btn_back=Button(conv_window, text="Back", font=f, width=10,command=f4)
	conv_btn_back.place(x=600,y=335)

	conv_window.withdraw()

	view_window=Toplevel(main_window)
	view_window.title("View")
	view_window.geometry("900x500")

	vw_st_data=ScrolledText(view_window, width=50, height=10, font=f)
	vw_btn_back=Button(view_window, text="Back", font=f,command=f8)

	vw_st_data.pack(pady=10)
	vw_btn_back.pack(pady=10)
	view_window.withdraw()

splash_window.after(3000,main)





mainloop()