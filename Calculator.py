import math
import mpmath
from tkinter import *
import tkinter.messagebox

switch = None
conv = None
hyp = None
x = None


def main():
    root = Tk()
    root.geometry("475x450+500+200")
    root.title("Scientific Calculator")
    root.iconphoto(False, PhotoImage(file="calculator.png"))

    def btn_1():
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "1")

    def btn_2():
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "2")

    def btn_3():
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "3")

    def btn_4():
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "4")

    def btn_5():
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "5")

    def btn_6():
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "6")

    def btn_7():
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "7")

    def btn_8():
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "8")

    def btn_9():
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "9")

    def btn_0():
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, "0")

    def btn_plus():
        ans = disp.get()
        if ans[-1] not in ["+", "-", "/", "x", "*"]:
            pos = len(ans)
            disp.insert(pos, "+")
        else:
            tkinter.messagebox.showinfo("Value error! Enter Number")

    def btn_min():
        ans = disp.get()
        if ans[-1] not in ["+", "-", "/", "x", "*"]:
            pos = len(ans)
            disp.insert(pos, "-")
        else:
            tkinter.messagebox.showinfo("Value error! Enter Number")

    def btn_mult():
        ans = disp.get()
        if ans[-1] not in ["+", "-", "/", "x", "*"]:
            pos = len(ans)
            disp.insert(pos, "x")
        else:
            tkinter.messagebox.showinfo("Value error! Enter Number")

    def btn_div():
        ans = disp.get()
        if ans[-1] not in ["+", "-", "/", "x", "*"]:
            pos = len(ans)
            disp.insert(pos, "/")
        else:
            tkinter.messagebox.showinfo("Value error! Enter Number")

    def btn_pm():
        global x
        if float(disp.get()) > 0:
            x = disp.get()
            pos = len(disp.get())
            disp.insert(0, "-")
            disp.insert(pos, "")
        elif float(disp.get()) < 0:
            disp.delete(0, END)
            disp.insert(0, str(x))

    def btn_abs():
        y=int(disp.get())
        disp.delete(0,END)
        disp.insert(0, str(math.fabs(y)))

    def btn_dot():
        pos = len(disp.get())
        disp.insert(pos, ".")

    def btn_nlog():
        try:
            if switch is True:
                ans = disp.get()
                disp.delete(0, END)
                disp.insert(0, str(mpmath.exp(float(ans))))
            else:
                ans = float(disp.get())
                ans = mpmath.log(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showinfo("Value error! check your operator and operand ")

    def btn_clear():
        disp.delete(0, END)
        disp.insert(0, "0")

    def btn_pi():
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, str(mpmath.pi))

    def btn_exp():
        if disp.get() == "0":
            disp.delete(0, END)
        pos = len(disp.get())
        disp.insert(pos, str(mpmath.e))

    def btn_cfb():
        pos = len(disp.get())
        disp.insert(pos, "(")

    def btn_cbb():
        pos = len(disp.get())
        disp.insert(pos, ")")

    def btn_fact():
        try:
            ans = disp.get()
            disp.delete(0, END)
            disp.insert(0, str(mpmath.factorial(int(ans))))
        except Exception:
            tkinter.messagebox.showinfo("Value error! check your operator and operand")

    def btn_back():
        pos = len(disp.get())
        display = str(disp.get())
        if display == "":
            disp.insert(0, "0")
        elif display == " ":
            disp.insert(0, "0")
        elif display == "0":
            pass
        else:
            disp.delete(0, END)
            disp.insert(0, display[:pos - 1])

    def btn_sqr():
        try:
            ans = float(disp.get())
            if switch is True:
                ans = math.pow(ans, 3)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            else:
                ans = math.pow(ans, 2)
                disp.delete(0, END)
                disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showinfo("Value error! check your operator and operand")

    def btn_inv():
        try:
            ans = float(disp.get())
            ans = 1/ans
            disp.delete(0, END)
            disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Error", "Can't Divide by Zero ")

    def btn_root():
        try:
            ans = float(disp.get())
            if switch is True:
                ans = round(math.pow(ans, 1 / 3), 2)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            else:
                ans = math.sqrt(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showinfo("Value error! check your operator and operand")

    def btn_rse_pow():
        try:
            ans = float(disp.get())
            if switch is True:
                ans = math.pow(2, ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            else:
                ans = math.pow(10, ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showinfo("Value error! check your operator and operand")

    def btn_log():
        try:
            ans = float(disp.get())
            ans = mpmath.log10(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showinfo("Error", "Value error! check your operator and operand ")

    def btn_result():
        try:
            ans = disp.get()
            ans = ans.replace("x", "*")
            ans = eval(ans)
            disp.delete(0, END)
            disp.insert(0, ans)
        except Exception:
            tkinter.messagebox.showinfo("Error", "Value error! check your operator and operand ")

    def btn_round():
        ans = disp.get()
        disp.delete(0, END)
        disp.insert(0, str(round(float(ans))))

    def btn_sin():
        try:
            ans = float(disp.get())
            if switch and hyp and conv:
                ans = math.asinh(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif conv and switch and not hyp:
                ans = math.degrees(math.asin(ans))
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif switch and hyp:
                ans = math.asinh(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif switch and not hyp:
                ans = math.asin(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif hyp:
                ans = math.sinh(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif conv:
                ans = math.sin(math.radians(ans))
                disp.delete(0, END)
                disp.insert(0, str(ans))
            else:
                ans = math.sin(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Invalid input")

    def btn_cos():
        try:
            ans = float(disp.get())
            if switch and hyp and conv:
                ans = math.acosh(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif conv and switch and not hyp:
                ans = math.degrees(math.acos(ans))
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif switch and hyp:
                ans = math.acosh(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif switch and not hyp:
                ans = math.acos(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif hyp:
                ans = math.cosh(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif conv:
                ans = math.cos(math.radians(ans))
                disp.delete(0, END)
                disp.insert(0, str(ans))
            else:
                ans = math.cos(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Invalid input")

    def btn_tan():
        try:
            ans = float(disp.get())
            if switch and hyp and conv:
                ans = math.atanh(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif conv and switch and not hyp:
                ans = math.degrees(math.atan(ans))
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif switch and hyp:
                ans = math.atanh(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif switch and not hyp:
                ans = math.atan(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif hyp:
                ans = math.tanh(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif conv:
                ans = math.tan(math.radians(ans))
                disp.delete(0, END)
                disp.insert(0, str(ans))
            else:
                ans = math.tan(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Invalid input")

    def btn_sec():
        try:
            ans = float(disp.get())
            if switch and hyp and conv:
                ans = mpmath.asech(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif conv and switch and not hyp:
                ans = mpmath.degrees(mpmath.asec(ans))
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif switch and hyp:
                ans = mpmath.asech(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif switch and not hyp:
                ans = mpmath.asec(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif hyp:
                ans = mpmath.sech(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif conv:
                ans = mpmath.sec(mpmath.radians(ans))
                disp.delete(0, END)
                disp.insert(0, str(ans))
            else:
                ans = mpmath.sec(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Invalid input")

    def btn_cosec():
        try:
            ans = float(disp.get())
            if switch and hyp and conv:
                ans = mpmath.acsch(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif conv and switch and not hyp:
                ans = mpmath.degrees(mpmath.acsc(ans))
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif switch and hyp:
                ans = mpmath.acsch(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif switch and not hyp:
                ans = mpmath.acsc(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif hyp:
                ans = mpmath.csch(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif conv:
                ans = mpmath.csc(mpmath.radians(ans))
                disp.delete(0, END)
                disp.insert(0, str(ans))
            else:
                ans = mpmath.csc(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Invalid input")

    def btn_cot():
        try:
            ans = float(disp.get())
            if switch and hyp and conv:
                ans = mpmath.acoth(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif conv and switch and not hyp:
                ans = math.degrees(mpmath.acot(ans))
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif switch and hyp:
                ans = mpmath.acoth(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif switch and not hyp:
                ans = mpmath.acot(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif hyp:
                ans = mpmath.coth(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
            elif conv:
                ans = mpmath.cot(math.radians(ans))
                disp.delete(0, END)
                disp.insert(0, str(ans))
            else:
                ans = mpmath.cot(ans)
                disp.delete(0, END)
                disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Invalid input")

    def btn_hyp():
        global switch
        global hyp
        if hyp is None:
            hyp = True
            if switch:
                sin_btn["text"] = "sinh-1"
                sin_btn["font"] = "segue 10 bold"
                cos_btn["text"] = "cosh-1"
                cos_btn["font"] = "segue 10 bold"
                tan_btn["text"] = "tanh-1"
                tan_btn["font"] = "segue 10 bold"
                sec_btn["text"] = "sech-1"
                sec_btn["font"] = "segue 10 bold"
                csec_btn["text"] = "cosceh-1"
                csec_btn["font"] = "segue 9 bold"
                cot_btn["text"] = "coth-1"
                cot_btn["font"] = "segue 11 bold"
            else:
                sin_btn["text"] = "sinh"
                sin_btn["font"] = "segue 11 bold"
                cos_btn["text"] = "cosh"
                cos_btn["font"] = "segue 11 bold"
                tan_btn["text"] = "tanh"
                tan_btn["font"] = "segue 11 bold"
                sec_btn["text"] = "sech"
                sec_btn["font"] = "segue 11 bold"
                csec_btn["text"] = "cosceh"
                csec_btn["font"] = "segue 10 bold"
                cot_btn["text"] = "coth"
                cot_btn["font"] = "segue 12 bold"
        else:
            hyp = None
            if switch:
                sin_btn["text"] = "sin-1"
                sin_btn["font"] = "segue 10 bold"
                cos_btn["text"] = "cos-1"
                cos_btn["font"] = "segue 11 bold"
                tan_btn["text"] = "tan-1"
                tan_btn["font"] = "segue 10 bold"
                sec_btn["text"] = "sec-1"
                sec_btn["font"] = "segue 10 bold"
                csec_btn["text"] = "cosce-1"
                csec_btn["font"] = "segue 10 bold"
                cot_btn["text"] = "cot-1"
                cot_btn["font"] = "segue 11 bold"
            else:
                sin_btn["text"] = "sin"
                sin_btn["font"] = "segue 15"
                cos_btn["text"] = "cos"
                cos_btn["font"] = "segue 14"
                tan_btn["text"] = "tan"
                tan_btn["font"] = "segue 15"
                sec_btn["text"] = "sec"
                sec_btn["font"] = "segue 14"
                csec_btn["text"] = "cosce"
                csec_btn["font"] = "segue 11 bold"
                cot_btn["text"] = "cot"
                cot_btn["font"] = "segue 15 bold"

    def btn_conv():
        global conv
        if conv is None:
            conv = True
            conv_btn["text"] = "DEG"
        else:
            conv = None
            conv_btn["text"] = "RAD"

    def shift():
        global switch
        global hyp
        if switch is None:
            shift_btn["bg"] = "Blue"
            switch = True
            if hyp:
                sin_btn["text"] = "sinh-1"
                sin_btn["font"] = "segue 10 bold"
                cos_btn["text"] = "cosh-1"
                cos_btn["font"] = "segue 9 bold"
                tan_btn["text"] = "tanh-1"
                tan_btn["font"] = "segue 9 bold"
                sec_btn["text"] = "sech-1"
                sec_btn["font"] = "segue 9 bold"
                csec_btn["text"] = "cosceh-1"
                csec_btn["font"] = "segue 8 bold"
                cot_btn["text"] = "coth-1"
                cot_btn["font"] = "segue 10 bold"
            else:
                sin_btn["text"] = "sin-1"
                sin_btn["font"] = "segue 10 bold"
                cos_btn["text"] = "cos-1"
                cos_btn["font"] = "segue 11 bold"
                tan_btn["text"] = "tan-1"
                tan_btn["font"] = "segue 10 bold"
                sec_btn["text"] = "sec-1"
                sec_btn["font"] = "segue 10 bold"
                csec_btn["text"] = "cosce-1"
                csec_btn["font"] = "segue 10 bold"
                cot_btn["text"] = "cot-1"
                cot_btn["font"] = "segue 11 bold"
                sqr_btn["text"] = "x^3"
                root_btn["text"] = "3√x"
                rse_pow_btn["text"] = "2^x"
                rse_pow_btn["font"] = "segue 13 bold"
                nlog_btn["text"] = "e^x"
                nlog_btn["font"] = "segue 9 bold"
        else:
            switch = None
            shift_btn["bg"] = "Black"
            if hyp:
                sin_btn["text"] = "sinh"
                sin_btn["font"] = "segue 11 bold"
                cos_btn["text"] = "cosh"
                cos_btn["font"] = "segue 11 bold"
                tan_btn["text"] = "tanh"
                tan_btn["font"] = "segue 11 bold"
                sec_btn["text"] = "sech"
                sec_btn["font"] = "segue 11 bold"
                csec_btn["text"] = "cosceh"
                csec_btn["font"] = "segue 10 bold"
                cot_btn["text"] = "coth"
                cot_btn["font"] = "segue 12 bold"
            else:
                sin_btn["text"] = "sin"
                sin_btn["font"] = "segue 15"
                cos_btn["text"] = "cos"
                cos_btn["font"] = "segue 14"
                tan_btn["text"] = "tan"
                tan_btn["font"] = "segue 15"
                sec_btn["text"] = "sec"
                sec_btn["font"] = "segue 14"
                csec_btn["text"] = "cosce"
                csec_btn["font"] = "segue 11 bold"
                cot_btn["text"] = "cot"
                cot_btn["font"] = "segue 15 bold"
                sqr_btn["text"] = "x^2"
                root_btn["text"] = "2√x"
                rse_pow_btn["text"] = "10^x"
                rse_pow_btn["font"] = "segue 10 bold"
                nlog_btn["text"] = " ln"
                nlog_btn["font"] = "segue 12 bold"

    disp = Entry(root, font="Verdana 30", fg="White", bg="Black", bd=0, justify=RIGHT)
    disp.insert(0, "0")
    disp.pack(expand=TRUE, fill=BOTH)
    # FRAME__1
    row1 = Frame(root, bg="#000000")
    row1.pack(expand=TRUE, fill=BOTH)
    conv_btn = Button(row1, text="RAD", font="segue 13 bold", command=btn_conv, relief=GROOVE, bd=0, fg="white", bg="Black")
    conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    hyp_btn = Button(row1, text="hyp", font="segue 14 bold", command=btn_hyp, relief=GROOVE, bd=0, fg="white", bg="Black")
    hyp_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    round_btn = Button(row1, text="Round", font="segue 13 bold", command=btn_round, relief=GROOVE, bd=0, fg="white", bg="Black")
    round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    inv_btn = Button(row1, text="1/x", font="segue 13 bold", command=btn_inv, relief=GROOVE, bd=0, fg="white", bg="Black")
    inv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    abs_btn = Button(row1, text="|x|", font="segue 15", command=btn_abs, relief=GROOVE, bd=0, fg="white", bg="Black")
    abs_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    # FRAME__2
    row2 = Frame(root, bg="#000000")
    row2.pack(expand=TRUE, fill=BOTH)
    shift_btn = Button(row2, text="Shift", font="segue 11 bold", command=shift, relief=GROOVE, bd=0, fg="white", bg="Black")
    shift_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    sin_btn = Button(row2, text="sin", font="segue 15", command=btn_sin, relief=GROOVE, bd=0, fg="white", bg="Black")
    sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    pi_btn = Button(row2, text="π", font="segue 15 bold", command=btn_pi, relief=GROOVE, bd=0, fg="white", bg="Black")
    pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    exp_btn = Button(row2, text="e", font="segue 17", command=btn_exp, relief=GROOVE, bd=0, fg="white", bg="Black")
    exp_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    clear_btn = Button(row2, text="C", font="segue 15", command=btn_clear, relief=GROOVE, bd=0, fg="white", bg="Black")
    clear_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    back_btn = Button(row2, text="⌫", font="segue 13 bold", command=btn_back, relief=GROOVE, bd=0, fg="white", bg="Black")
    back_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    # FRAME__3
    row3 = Frame(root, bg="#000000")
    row3.pack(expand=TRUE, fill=BOTH)
    sqr_btn = Button(row3, text="x^2", font="segue 13 bold", command=btn_sqr, relief=GROOVE, bd=0, fg="white", bg="Black")
    sqr_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    cos_btn = Button(row3, text="cos", font="segue 14 ", command=btn_cos, relief=GROOVE, bd=0, fg="white", bg="Black")
    cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    cfb_btn = Button(row3, text="(", font="segue 13 bold", command=btn_cfb, relief=GROOVE, bd=0, fg="white", bg="Black")
    cfb_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    cbb_btn = Button(row3, text=")", font="segue 13 bold", command=btn_cbb, relief=GROOVE, bd=0, fg="white", bg="Black")
    cbb_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    fact_btn = Button(row3, text="n!", font="segue 15 bold", command=btn_fact, relief=GROOVE, bd=0, fg="white", bg="Black")
    fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    div_btn = Button(row3, text="➗", font="segue 7 bold", command=btn_div, relief=GROOVE, bd=0, fg="white", bg="Black")
    div_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    # FRAME__4
    row4 = Frame(root, bg="#000000")
    row4.pack(expand=TRUE, fill=BOTH)
    root_btn = Button(row4, text="2√x", font="segue 13 bold", command=btn_root, relief=GROOVE, bd=0, fg="white", bg="Black")
    root_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    tan_btn = Button(row4, text="tan", font="segue 15", command=btn_tan, relief=GROOVE, bd=0, fg="white", bg="Black")
    tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    seven_btn = Button(row4, text="7", font="segue 14 bold", command=btn_7, relief=GROOVE, bd=0, fg="white", bg="Black")
    seven_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    eight_btn = Button(row4, text="8", font="segue 14 bold", command=btn_8, relief=GROOVE, bd=0, fg="white", bg="Black")
    eight_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    nine_btn = Button(row4, text="9", font="segue 14 bold", command=btn_9, relief=GROOVE, bd=0, fg="white", bg="Black")
    nine_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    mult_btn = Button(row4, text="X", font="segue 13 bold", command=btn_mult, relief=GROOVE, bd=0, fg="white", bg="Black")
    mult_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    # FRAME__5
    row5 = Frame(root, bg="#000000")
    row5.pack(expand=TRUE, fill=BOTH)
    rse_pow_btn = Button(row5, text="10^x", font="segue 10 bold", command=btn_rse_pow, relief=GROOVE, bd=0, fg="white", bg="Black")
    rse_pow_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    sec_btn = Button(row5, text="sec", font="segue 14", command=btn_sec, relief=GROOVE, bd=0, fg="white", bg="Black")
    sec_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    four_btn = Button(row5, text="4", font="segue 14 bold", command=btn_4, relief=GROOVE, bd=0, fg="white", bg="Black")
    four_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    five_btn = Button(row5, text="5", font="segue 14 bold", command=btn_5, relief=GROOVE, bd=0, fg="white", bg="Black")
    five_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    six_btn = Button(row5, text="6", font="segue 14 bold", command=btn_6, relief=GROOVE, bd=0, fg="white", bg="Black")
    six_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    min_btn = Button(row5, text="—", font="segue 12 bold", command=btn_min, relief=GROOVE, bd=0, fg="white", bg="Black")
    min_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    # FRAME__6
    row6 = Frame(root, bg="#000000")
    row6.pack(expand=TRUE, fill=BOTH)
    nlog_btn = Button(row6, text=" ln", font="segue 12 bold", command=btn_nlog, relief=GROOVE, bd=0, fg="white", bg="Black")
    nlog_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    csec_btn = Button(row6, text="cosec", font="segue 11 bold", command=btn_cosec, relief=GROOVE, bd=0, fg="white", bg="Black")
    csec_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    one_btn = Button(row6, text="1", font="segue 14 bold", command=btn_1, relief=GROOVE, bd=0, fg="white", bg="Black")
    one_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    two_btn = Button(row6, text="2", font="segue 14 bold", command=btn_2, relief=GROOVE, bd=0, fg="white", bg="Black")
    two_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    three_btn = Button(row6, text="3", font="segue 14 bold", command=btn_3, relief=GROOVE, bd=0, fg="white", bg="Black")
    three_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    plus_btn = Button(row6, text="+", font="segue 14 bold", command=btn_plus, relief=GROOVE, bd=0, fg="white", bg="Black")
    plus_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    # FRAME__7
    row7 = Frame(root, bg="#000000")
    row7.pack(expand=TRUE, fill=BOTH)
    log_btn = Button(row7, text="log", font="segue 10 bold", command=btn_log, relief=GROOVE, bd=0, fg="white", bg="Black")
    log_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    cot_btn = Button(row7, text="cot", font="segue 15 bold", command=btn_cot, relief=GROOVE, bd=0, fg="white", bg="Black")
    cot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    pm_btn = Button(row7, text="±", font="segue 15 bold", command=btn_pm, relief=GROOVE, bd=0, fg="white", bg="Black")
    pm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    zero_btn = Button(row7, text="0", font="segue 13 bold", command=btn_0, relief=GROOVE, bd=0, fg="white", bg="Black")
    zero_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    dot_btn = Button(row7, text=".", font="segue 14 bold", command=btn_dot, relief=GROOVE, bd=0, fg="white", bg="Black")
    dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    result_btn = Button(row7, text="=", font="segue 13 bold", command=btn_result, relief=GROOVE, bd=0, fg="white", bg="blue")
    result_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
    root.mainloop()


if __name__ == "__main__":
    main()
