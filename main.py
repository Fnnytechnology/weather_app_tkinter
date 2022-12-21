from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar

# for weather

import requests
from PIL import ImageTk,Image
from tkinter import messagebox
from time import strftime
from datetime import datetime

w = Tk()

widht_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()

x_cordianete = (screen_width/2) - (widht_of_window/2)
y_cordianete = (screen_height/2) - (height_of_window/2)

w.geometry("%dx%d+%d+%d"%(widht_of_window ,height_of_window,x_cordianete , y_cordianete))
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)
w.overrideredirect(1)


def weather_screen():
     w=Tk()
     w.geometry('800x400')
     w.iconbitmap('./resource/icon.ico')
     w.title("Weather")
     w.resizable(0,0)

     try:
          

     ######################################
     #Mechenism
          
          def weather_data(query):
                         res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&appid=06c921750b9a82d8f5d1294e1586276f');
                         return res.json();
     


          #Body UI
          Frame(w,width=800,height=50,bg='#353535').place(x=0,y=0)

          #serach bar
          img1 = ImageTk.PhotoImage(Image.open("./resource/search.png"))
          def on_enter(e):
               e1.delete(0,'end')    
          def on_leave(e):
               if e1.get()=='':   
                    e1.insert(0,'Search City')

          
          e1 =Entry(w,width=21,fg='white',bg="#353535",border=0)
          e1.config(font=('Calibri (Body)',12))
          e1.bind("<FocusIn>", on_enter)
          e1.bind("<FocusOut>", on_leave)
          e1.insert(0,'Search City')
          e1.place(x=620,y=15)

          #date

          a=datetime.today().strftime('%B')
          b=(a.upper())
          q = datetime.now().month

     
          now = datetime.now()


          c=now.strftime('%B')
          month=c[0:3]
     

          today = datetime.today()

          date = today.strftime("%d")





          def label(a):
               
               Frame(width=500,height=50,bg="#353535").place(x=0,y=0)
               
               
               l2=Label(w, text=str(a),bg="#353535",fg="white")# upper border
               l2.config(font=("Microsoft JhengHei UI Light", 18))
               l2.place(x=20,y=8)

               #def weather_cast():
               city=a
               query='q='+city
               w_data=weather_data(query)
               result=w_data
               try:
                    check="{}".format(result['main']['temp'])
                    celsius="{}".format(result['main']['temp'])
               #print(check)
               except:
                    messagebox.showinfo("", "    City name not found    ")

               c=(int(float(check)))-273
               descp=("{}".format(result['weather'][0]['description']))
               weather=("{}".format(result['weather'][0]['main']))
          # print(weather)


               global img

               if c>10 and weather=="Haze" or weather=="Clear":
                    Frame(w,width=800,height=350,bg="#f78954").place(x=0,y=50)          
                    img = ImageTk.PhotoImage(Image.open("./resource/sunny1.png"))
                    Label(w,image=img,border=0).place(x=170,y=130)
                    bcolor="#f78954"
                    fcolor="white"

               elif c>10 and weather=="Clouds":
                    Frame(w,width=800,height=350,bg="#7492b3").place(x=0,y=50)
                    img = ImageTk.PhotoImage(Image.open("./resource/cloudy1.png"))
                    Label(w,image=img,border=0).place(x=170,y=130)
                    bcolor="#7492b3"
                    fcolor="white"

               elif c<=10 and weather=="Clouds":
                    Frame(w,width=800,height=350,bg="#7492b3").place(x=0,y=50)
                    img = ImageTk.PhotoImage(Image.open("./resource/cloudcold.png"))
                    Label(w,image=img,border=0).place(x=170,y=130)
                    bcolor="#7492b3"
                    fcolor="white"

               elif c>10 and weather=="Rain":
                    Frame(w,width=800,height=350,bg="#60789e").place(x=0,y=50)
                    img = ImageTk.PhotoImage(Image.open("./resouce/rain1.png"))
                    Label(w,image=img,border=0).place(x=170,y=130)
                    bcolor="#60789e"
                    fcolor="white"

               elif c<=10 and weather=="Fog" or weather=="Clear":
                    Frame(w,width=800,height=350,bg="white").place(x=0,y=50)          
                    img = ImageTk.PhotoImage(Image.open("./resouce/cold.png"))
                    Label(w,image=img,border=0).place(x=170,y=130)
                    bcolor="white"
                    fcolor="black"
                         
               else:
                    Frame(w,width=800,height=350,bg="white").place(x=0,y=50)
               # img = ImageTk.PhotoImage(Image.open("error.png"))
                    label=Label(w,text=weather,border=0,bg='white')
                    label.configure(font=(("Microsoft JhengHei UI Light", 18)))
                    label.place(x=160,y=130)
                    bcolor="white"
                    fcolor="black"

               w_data=weather_data(query)
               result=w_data



               e=("Humidity: {}".format(result['main']['humidity']))
               f=("Pressure: {}".format(result['main']['pressure']))
               g=("MAX temp: {}".format(result['main']['temp_max']))
               h=("MIN temp: {}".format(result['main']['temp_min']))
               b1=b=("Wind speed: {} m/s".format(result['wind']['speed']))
               
          
               
               l5=Label(w, text=str(month+"  "+ date),bg=bcolor,fg=fcolor)# upper border
               l5.config(font=("Microsoft JhengHei UI Light", 25))
               l5.place(x=330,y=335)          


               l4=Label(w, text=str(str(e+"%")),bg=bcolor,fg=fcolor)# upper border
               l4.config(font=("Microsoft JhengHei UI Light", 11))
               l4.place(x=510,y=135)

               

               l4=Label(w, text=str(str(f+" hPa")),bg=bcolor,fg=fcolor)# upper border
               l4.config(font=("Microsoft JhengHei UI Light", 11))
               l4.place(x=510,y=175)

               l4=Label(w, text=str(str(b1)),bg=bcolor,fg=fcolor)# upper border
               l4.config(font=("Microsoft JhengHei UI Light", 11))
               l4.place(x=510,y=215)
               

               
          

               l3=Label(w, text=str(str(c) +"°C"),bg=bcolor,fg=fcolor)# upper border
               l3.config(font=("Microsoft JhengHei UI Light", 40))
               l3.place(x=330,y=150)
                    
          label(a="Dhaka")

          def cmd1():
               b=str(e1.get())
               label(str(b))
               
                    
                    
          Button(w,image=img1,command=cmd1,border=0).place(x=750,y=10)


     except:
          
          Frame(w,width=800,height=400,bg='white').place(x=0,y=0)
          global imgx
          imgx = ImageTk.PhotoImage(Image.open("nointernet.png"))

          Label(w,image=imgx,border=0).pack(expand=True)#place(x=100,y=100)
          


     w.mainloop()


def bar():
    l4 = Label(w,text='loading...' , fg="white" , bg='#249794')
    lst4 = ('Calirbi(Body)',10)
    l4.configure(font=lst4)
    l4.place(x=18, y = 210)

    import time 
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks ()
        time.sleep(0.03)
        r = r + 1
    w.destroy()
    weather_screen() 

progress.place(x=-10,y=235)


#adding frae
#249794
Frame(w, width=427 , height=241 , bg='#249794').place(x=0 ,y=0)
b1=Button(w,width=10 , height=1 , text="Get Started",command = bar , border=0, fg='#249794')
b1.place(x=170 , y=200)

# labels
l1 = Label(w, text='Weather', fg="white", bg='#249794')
list1=('Calirbi(Body)',18,'bold')
l1.configure(font=list1)
l1.place(x=50 , y=80)


l2 = Label(w, text='App', fg="white", bg='#249794')
list2=('Calirbi(Body)',13)
l2.configure(font=list2)
l2.place(x=155 , y=82)


l3 = Label(w, text='Programmed by PiPy Fun', fg="white", bg='#249794')
list3=('Calirbi(Body)',13)
l3.configure(font=list3)
l3.place(x=50 , y=110)
w.mainloop()