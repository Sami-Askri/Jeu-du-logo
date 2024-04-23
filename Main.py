from tkinter import *
import random
from random import shuffle
from PIL import ImageTk, Image
import pygame


pygame.init()

score = 0
root = Tk()  # interface principale

soundstatus=1
frame = Frame(root, width=520, height=350 )

var1=IntVar()
var2=IntVar()
var3=IntVar()

root.title("Le jeu du LOGO ")
i0 = "realmadrid.png"
i1 = "adidas.png"
i2 = "mercedes.png"
i3 = "whatsapp.png"
i4 = "instagram.png"
i5 = "android.png"
i6 = "dominos.png"
i7="apple.png"
i8="asus.png"
i9="Blackberry.png"
i10="Fastrack.png"
i11="Microsoft.png"
i12="Pepsi.png"
i13="porsche.png"
i14="Skullcandy.png"
i15="spotify.png"
i16="Starbucks.png"
i17="Tesla.png"
i18="Unity.png"
i19="Unreal.png"
i20="vodafone.png"

musicflag=1

list1 = []
list = [[i0, "Real Madrid"], [i1, "Adidas"], [i2, "Mercedes"], [i3, "Whatsapp"], [i4, "Instagram"], [i5, 'Android'],
		[i6, 'Dominos'],[i7,"Apple"],[i8,"Asus"],[i9,"BlackBerry"],[i10,"Fastrack"],[i11,"Microsoft"],[i12,"Pepsi"],[i13,"Porsche"],[i14,"Skullcandy"],
		[i15,"Spotify"],[i16,"Starbucks"],[i17,"Tesla"],[i18,"Unity"],[i19,"Unreal"],[i20,"Vodafone"]]
list2 = [['Real Madrid', 'Barcelona', 'AC Milan', 'Arsenal'], ['Nike', 'Puma', 'Reebok', 'Adidas'],
         ['Mercedes', 'Ferrari', 'Audi', 'Ford'], ['Hike', 'Whatsapp', 'Telegram', 'Line'],
         ['Snapchat', 'Instagram', 'Whatsapp', 'Facebook'],['Android', 'Windows', 'Microsoft', 'Symbian'], ['Dominos', 'Pizza Hut', 'Burger King', 'McDonalds'],
         ['Apple','Samsung','One Plus','Google'],['Asus','Hp','Lenovo','Acer'],['BlackBerry','Nokia','Samsung','Apple'],['Fastrack','Fossil','Titan','Casio']
         ,['Apple','Google','Amazon','Microsoft'],['Pepsi','Coke','Coca Cola','Fanta'],['Porsche','Mustang','BMW','Jaguar'],['Skullcandy','JBL','Boat','Sony'],
         ['Spotify','Pandora','Gaana','Saavn'],['Starbucks','CCD','Costa Coffee','Dunkin Donuts'],['Tesla','Audi','Toyota','Bentley'],
         ['Unity','Unreal','Gnome','Cryengine'],['Unreal','Game Maker','Corona','Unity'],['Vodafone','Jio','Airtel','Idea']]




def showimage():

	def button_event(text, x):
		if text == list[x][1]:
			global score
			score = score + 1;print("SCORE: ", score)
			
			print("Correct")
			 
			answer=1

			frame1.destroy()
			showimage()
		else:
			print("Faux")
			frame1.destroy()
			
			answer=0

			frame3=Frame(root,width=500,height=330)
			canvas3=Canvas(frame3,width=500,height=330,bg="lightblue")
			
			canvas3.create_text(250,80,text="Perdu !!!!",fill="red",font=("Times",30))
			canvas3.create_text(245,150,text="Essaye encore une fois !",fill="red",font=("Times",30))
			canvas3.create_text(240,195,text="Votre Score: "+str(score),fill="darkblue",font=("Times",30))
				
			restart_but1 = Button(frame3, text="Re essaye", width=15, height=2, command=lambda: restart(frame3))
			restart_but1.place(x=135, y=250)
			exit_but1=Button(frame3, text="Quitter", width=15, height=2, command=exit)
			exit_but1.place(x=255, y=250)
			canvas3.pack()
			frame3.pack()

	def showbuttons(n):
		if musicflag == 0:
			val=1
		else:
			val=0
		cbut_music1 = Checkbutton(frame1, text="Musique",variable=var1,onvalue=val,offvalue=not val,command=music)
		cbut_music1.place(x=450,y=3)
		
		
		shuffle(list2[n])
		x1=10
		y1=260
		option1 = Button(frame1, text=list2[n][0], width=34, height=2, command=lambda: button_event(list2[n][0], n))
		option1.place(x=x1, y=y1)

		x2=265
		y2=260
		option2 = Button(frame1, text=list2[n][1], width=34, height=2, command=lambda: button_event(list2[n][1], n))
		option2.place(x=x2, y=y2)
		
		x3=10
		y3=305
		option3 = Button(frame1, text=list2[n][2], width=34, height=2, command=lambda: button_event(list2[n][2], n))
		option3.place(x=x3, y=y3)
		
		x4=265
		y4=305
		option4 = Button(frame1, text=list2[n][3], width=34, height=2, command=lambda: button_event(list2[n][3], n))
		option4.place(x=x4, y=y4)
        
	frame.destroy()
	global frame1
	frame1 = Frame(root, width=520, height=350)
	canvas1 = Canvas(frame1, width=520, height=350,bg="lightblue")
	canvas1.place(x=0, y=0)
	
	
	canvas1.create_rectangle(380,32,500,47,fill="white")   
	
	canvas1.create_text(435, 40, fill="darkblue", text="SCORE ACTUEL : ",font=("Times",9))
	canvas1.create_text(490, 40, fill="darkblue", text=str(score),font=("Times",9))
	
	
	
	n = random.randrange(0, 20, 1)
    
	def restart(frame2):
		global score
		score=0
		frame2.destroy()
		showimage()
		
	if len(list1) == 20:
		list1.clear()
		frame1.destroy()
		frame2 = Frame(root)
		canvas2 = Canvas(frame2, height=330, width=500,bg="lightblue")

		canvas2.create_text(250,80, fill="green", text="T'as gagné!!!!", font=("Times", 30))
		canvas2.create_text(250,130, fill="darkblue", text="*Bravo*", font=("Times", 30))
		
		restart_but = Button(frame2, text="Rejouer", width=15, height=2, command=lambda: restart(frame2))
		restart_but.place(x=135, y=170)
		exit_but=Button(frame2, text="Quitter", width=15, height=2, command=exit)
		exit_but.place(x=255, y=170)
		canvas2.pack()
		frame2.pack()

	elif n in list1:
		showimage()

	else:
		
		canvas1.create_rectangle(12,12,253,253)
		canvas1.create_rectangle(10,10,255,255,fill="gray")
		canvas1.create_rectangle(15,15,250,250,fill="red")
		img = ImageTk.PhotoImage(Image.open("Images/"+list[n][0]))
		canvas1.create_image(20, 20, anchor=NW, image=img)
		canvas1.image = img
		canvas1.place(x=0, y=0)
		
		list1.append(n)
		showbuttons(n)

	frame1.pack()
	print("list1 : ",list1)
	

		



def exit():

	quit()
def music():
	
	global musicflag
	if musicflag == 0:
		musicflag=1
		pygame.mixer.music.load('music.mp3')
		pygame.mixer.music.play(-1)
		print("music on")
	else:
		musicflag=0
		pygame.mixer.music.stop()
		print("music off")	



		


canvas4 = Canvas(frame, height=350, width=500)
back_img=ImageTk.PhotoImage(Image.open("Images/bg.png"))
canvas4.create_image(0, 0, anchor=NW, image=back_img)
canvas4.image = back_img
canvas4.pack()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)


but = Button(frame, text="Commencer",width=25, height=1, command=showimage)
but1 = Button(frame, text="Quitter", width=25, height=1,command=exit)
cbut_music = Checkbutton(frame, text="Musique",variable=var3,onvalue=0,offvalue=1,command=music)


but.place(x=60,y=40)
but1.place(x=280,y=40)
cbut_music.place(x=430,y=3)

frame.pack()
root.resizable(0,0)
root.mainloop()
