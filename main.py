import tkinter, math

window = tkinter.Tk()
window.geometry("400x500")

z = 0

def func():
    list = [entry1.get(), entry2.get(), entry3.get(), entry4.get()]
    
    if list.count('') > 2:
        label6.config(text='* 최소 2개의 칸에 값을 입력해주세요.')
        return
    
    a = b = c = d = None
    
    if list[0] != '':
        try:
            a = float(list[0])
        except:
            label6.config(text='* 옳바른 값을 입력해주세요.')
            return
        
    if list[1] != '':
        try:
            b = float(list[1])
        except:
            label6.config(text='* 옳바른 값을 입력해주세요.')
            return
        
    if list[2] != '':
        try:
            c = float(list[2])
        except:
            label6.config(text='* 옳바른 값을 입력해주세요.')
            return
        
    if list[3] != '':
        try:
            d = float(list[3])
        except:
            label6.config(text='* 옳바른 값을 입력해주세요.')
            return
    
    if a == None:
        if b == None:
            a = round(100 * ((0.5) ** c), 1)
            b = round(d / c, 1)
            entry1.delete(0, tkinter.END)
            entry1.insert(0, str(a))
            entry2.delete(0, tkinter.END)
            entry2.insert(0, str(b))
        elif c == None:
            c = round(d / b, 1)
            a = round(100 * ((0.5) ** c), 1)
            entry1.delete(0, tkinter.END)
            entry1.insert(0, str(a))
            entry3.delete(0, tkinter.END)
            entry3.insert(0, str(c))
        elif d == None:
            a = round(100 * ((0.5) ** c), 1)
            d = round(b * c)
            entry1.delete(0, tkinter.END)
            entry1.insert(0, str(a))
            entry4.delete(0, tkinter.END)
            entry4.insert(0, str(d))
    elif b == None:
        if c == None:
            c = round((math.log10(a) - 2) / math.log10(0.5), 1)
            b = round(d / c)
            entry2.delete(0, tkinter.END)
            entry2.insert(0, str(b))
            entry3.delete(0, tkinter.END)
            entry3.insert(0, str(c))
        elif d == None:
            label6.config(text='* 이 정보로 다른 값들을 구할 수 없습니다.')
            return
    elif c == None:
        if d == None:
            c = round((math.log10(a) - 2) / math.log10(0.5), 1)
            d = round(b * c)
            entry3.delete(0, tkinter.END)
            entry3.insert(0, str(c))
            entry4.delete(0, tkinter.END)
            entry4.insert(0, str(d))
        

    # 계산 결과를 보여주는 메시지
    label6.config(text='계산 완료!')
            
label5 = tkinter.Label(window, text='3개의 값중 2개의 값을 입력하고 계산버튼을 누르면 \n나머지 값을 구할 수 있습니다.')
label5.pack()

label1 = tkinter.Label(window, text='모원소 비율(%)')
label1.pack()
entry1 = tkinter.Entry(window)
entry1.pack()

label2 = tkinter.Label(window, text='반감기(년)')
label2.pack()
entry2 = tkinter.Entry(window)
entry2.pack()

label3 = tkinter.Label(window, text='반감기 횟수(회)')
label3.pack()
entry3 = tkinter.Entry(window)
entry3.pack()

label4 = tkinter.Label(window, text='암석의 나이(년)')
label4.pack()
entry4 = tkinter.Entry(window)
entry4.pack()

btn = tkinter.Button(window, text='계산', command=func)
btn.pack()

label6 = tkinter.Label(window, text='')
label6.pack()

window.mainloop()