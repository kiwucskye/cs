import tkinter as tk

def click_name_button():
    name = en_name.get()
    lbl_name.config(text=f"제 이름은 {name}입니다")

window = tk.Tk()
window.title("클라우드서비스 깃/깃허브 실습")
window.geometry("500x200")

en_name = tk.Entry(window)
btn_name = tk.Button(window, text="클릭", command=click_name_button)
lbl_name = tk.Label(window, text="이름 입력 : ")

lbl_name.pack()
en_name.pack()
btn_name.pack()
window.mainloop()
