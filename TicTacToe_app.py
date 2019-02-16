from tkinter import *
import tkinter.messagebox
import sys


flag = 1 #initialize flag which show who's turn
btn_list = [] #list of the seques of gameplay in oder
game_list = ['nothing',' ',' ',' ',' ',' ',' ',' ',' ',' '] #to check for win and store the game progress


def btn_press(bno):
    #when any btn(tile) is pressed this function is invoked
    global game_list
    global flag
    global btn_list
    btn_list.append(bno)
    if(game_list[bno] == ' '): #check if all the 9 positions are ocupied or not
        if(flag == 1): #check which players turn, flag=1 is for players 'X' i.e. first player
            check_btn(bno,'X')
            check_winner('X',1)
        else:
            check_btn(bno,'O')
            check_winner('O',2)
        flag = -flag #check the turn to second player

    else:
        tkinter.messagebox.showinfo("Entry Error","Try clicking somewhere else") #error if same button(tile) is pressed twice

      
def check_btn(bno,bvalue):
    #set the mark on the button(tile) as per the click from the user also set the same on the game_list for further evatualtion
    global game_list
    if(bno == 1):
        btn1['text'] = bvalue
    elif(bno == 2):
        btn2['text'] = bvalue
    elif(bno == 3):
        btn3['text'] = bvalue
    elif(bno == 4):
        btn4['text'] = bvalue
    elif(bno == 5):
        btn5['text'] = bvalue
    elif(bno == 6):
        btn6['text'] = bvalue
    elif(bno == 7):
        btn7['text'] = bvalue
    elif(bno == 8):
        btn8['text'] = bvalue
    else:
        btn9['text'] = bvalue
    game_list[bno] = bvalue


def check_winner(btext,pno):
    #match all the possible win patterns with the current ingame status to ckeck the winner(as told by the functon name)
    global game_list
    c = 0
    for x in game_list:
        #check if all the places are not full
        if(x == ' '):
            c+=1
    if(c != 0):
        #if not then check for winner
        is_winner = show_winner(btext)
        if is_winner:
            check_player(pno)
            btn_reset()
    else:
        #if all tiles(buttons) are ocupied then also check for winner(just in case)
        is_winner = show_winner(btext)
        if is_winner:
            check_player(pno)
            btn_reset()
        else:
            #show no its a draw
            tkinter.messagebox.showinfo("Winner","no one haha, its a draw")
            btn_reset()


def show_winner(btext):
    #the part where we check for the winner
    #if won return true (winner winner chicken dinner)
    if(game_list[1] == btext and game_list[2] == btext and game_list[3] == btext):
        return True 
    elif(game_list[4] == btext and game_list[5] == btext and game_list[6] == btext):
        return True
    elif(game_list[7] == btext and game_list[8] == btext and game_list[9] == btext):
        return True
    elif(game_list[1] == btext and game_list[4] == btext and game_list[7] == btext):
        return True
    elif(game_list[2] == btext and game_list[5] == btext and game_list[8] == btext):
        return True
    elif(game_list[3] == btext and game_list[6] == btext and game_list[9] == btext):
        return True
    elif(game_list[1] == btext and game_list[5] == btext and game_list[9] == btext):
        return True
    elif(game_list[3] == btext and game_list[5] == btext and game_list[7] == btext):
        return True


def check_player(pno):
    #show the message box which the winner
    if (pno == 1):
        tkinter.messagebox.showinfo("Winner","Winner is player 1")
    else:
        tkinter.messagebox.showinfo("Winner","Winner is player 2")


def btn_clear():
    #its for the undo, rewind one step per click
    global btn_list
    global game_list
    global flag
    if(len(btn_list) == 0):
        pass
    else:
        btn_num = btn_list.pop()
        flag = -flag
        if(btn_num == 1):
            btn1['text'] = ' '
            game_list[btn_num] = ' '
        elif(btn_num == 2):
            btn2['text'] = ' '
            game_list[btn_num] = ' '
        elif(btn_num == 3):
            btn3['text'] = ' '
            game_list[btn_num] = ' '
        elif(btn_num == 4):
            btn4['text'] = ' '
            game_list[btn_num] = ' '
        elif(btn_num == 5):
            btn5['text'] = ' '
            game_list[btn_num] = ' '
        elif(btn_num == 6):
            btn6['text'] = ' '
            game_list[btn_num] = ' '
        elif(btn_num == 7):
            btn7['text'] = ' '
            game_list[btn_num] = ' '
        elif(btn_num == 8):
            btn8['text'] = ' '
            game_list[btn_num] = ' '
        elif(btn_num == 9):
            btn9['text'] = ' '
            game_list[btn_num] = ' '
        else:
            pass


def btn_reset():
    #reset the game to initial stage(as the function name suggest)
    global game_list
    global btn_list
    btn1['text'] = ' '
    btn2['text'] = ' '
    btn3['text'] = ' '
    btn3['text'] = ' '
    btn4['text'] = ' '
    btn5['text'] = ' '
    btn6['text'] = ' '
    btn7['text'] = ' '
    btn8['text'] = ' '
    btn9['text'] = ' '
    game_list = ['nothing',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    btn_list.clear()
    


def game_start():
    #on click open the game window aka root window
    root.deiconify()
    start_window.destroy()


def game_exit():
    #ask rhe user if yes then pack up
    exit_status = tkinter.messagebox.askyesno("Confirmation","Are you sure you want to exit?")
    if exit_status:
        root.destroy()
        sys.exit()
    else:
        pass


root = Tk() #create the main window and initialize it
root.title("Tic Tac Toe")
root.geometry("330x440+400+50")
root.resizable(width=FALSE,height=FALSE)
root.config(background='grey')


#this window appear at he start as a welcome screen
start_window = Toplevel(root)
start_window.title("Tic Tac Toe")
start_window.geometry("330x400+400+50")
root.resizable(width=FALSE,height=FALSE)
start_window.config(background='yellow')


btn_style = ('Times Roman New',50,'bold')
btn_style2 = ('Times New Roman',14,'bold')


#-----------------------widgets in the main window----------------------------------
head = Label(root,text="Tic Tac Toe", font=('Times Roman New',38,'bold'),fg="green")
head.place(x=10, y=10, width=310, height=50)
btn1 = Button(root,text=" ", font=btn_style,fg="brown", command=lambda: btn_press(1))
btn1.place(x=10, y=70, width=100, height=100)
btn2 = Button(root,text=" ", font=btn_style,fg="brown", command=lambda: btn_press(2))
btn2.place(x=115, y=70, width=100, height=100)
btn3 = Button(root,text=" ", font=btn_style,fg="brown", command=lambda: btn_press(3))
btn3.place(x=220, y=70, width=100, height=100)
btn4 = Button(root,text=" ", font=btn_style,fg="brown", command=lambda: btn_press(4))
btn4.place(x=10, y=175, width=100, height=100)
btn5 = Button(root,text=" ", font=btn_style,fg="brown", command=lambda: btn_press(5))
btn5.place(x=115, y=175, width=100, height=100)
btn6 = Button(root,text=" ", font=btn_style,fg="brown", command=lambda: btn_press(6))
btn6.place(x=220, y=175, width=100, height=100)
btn7 = Button(root,text=" ", font=btn_style,fg="brown", command=lambda: btn_press(7))
btn7.place(x=10, y=280, width=100, height=100)
btn8 = Button(root,text=" ", font=btn_style,fg="brown", command=lambda: btn_press(8))
btn8.place(x=115, y=280, width=100, height=100)
btn9 = Button(root,text=" ", font=btn_style,fg="brown", command=lambda: btn_press(9))
btn9.place(x=220, y=280, width=100, height=100)
btn_undo = Button(root,text="UNDO", font=btn_style2,fg="blue", command=btn_clear)
btn_undo.place(x=80, y=390)
btn_undo = Button(root,text="RESET", font=btn_style2,fg="blue", command=btn_reset)
btn_undo.place(x=180, y=390)
root.iconify() #keep the main game window hidden till start button is pressed

#----------------------widgets in start(welcome) window---------------------------------
photo = PhotoImage(file="start_pic.png")
start_label = Label(start_window, text="WELCOME", font=('Algerian',50,'bold'),fg="red")
start_label.place(x=10, y=10, width=310, height=60)
start_info = Label(start_window, image=photo)
start_info.place(x=10, y=80, width=310, height=200)

btn_start = Button(start_window,text="Start", font=('Times Roman New',22,'italic'),fg="purple", command=game_start)
btn_start.place(x=50, y=300, height=40)
btn_exit = Button(start_window,text="Exit", font=('Times Roman New',22,'italic'),fg="purple", command=game_exit)
btn_exit.place(x=200, y=300, height=40)


root.mainloop() #keep the app running until terminated by the user
