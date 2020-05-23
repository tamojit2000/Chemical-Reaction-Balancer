from tkinter import Tk,Entry,Label,Button,font
from os import startfile
import sympy
import re

ELEMENT_CLAUSE = re.compile("([A-Z][a-z]?)([0-9]*)")

def parse_compound(compound):
    assert "(" not in compound, "This parser doesn't grok subclauses"
    return {el: (int(num) if num else 1) for el, num in ELEMENT_CLAUSE.findall(compound)}

def main(L,R):
    ans_label.config(text='')
    
    lhs_strings = L.replace(' ','').split('+')
    lhs_compounds = [parse_compound(compound) for compound in lhs_strings]

    rhs_strings = R.replace(' ','').split('+')
    rhs_compounds = [parse_compound(compound) for compound in rhs_strings]

    els = sorted(set().union(*lhs_compounds, *rhs_compounds))
    els_index = dict(zip(els, range(len(els))))

    w = len(lhs_compounds) + len(rhs_compounds)
    h = len(els)
    A = [[0] * w for _ in range(h)]
    
    for col, compound in enumerate(lhs_compounds):
        for el, num in compound.items():
            row = els_index[el]
            A[row][col] = num
    for col, compound in enumerate(rhs_compounds, len(lhs_compounds)):
        for el, num in compound.items():
            row = els_index[el]
            A[row][col] = -num

    
    A = sympy.Matrix(A)    
    
    coeffs = A.nullspace()[0]    
    coeffs *= sympy.lcm([term.q for term in coeffs])

    lhs = " + ".join(["{} {}".format(coeffs[i], s) for i, s in enumerate(lhs_strings)])
    rhs = " + ".join(["{} {}".format(coeffs[i], s) for i, s in enumerate(rhs_strings, len(lhs_strings))])

    ANS=">>>  {} -> {}".format(lhs, rhs)
    
    ans_label.config(text=ANS )

    File=open('history.txt','a')
    File.write(ANS+'\n')
    File.close()


def balance(event=None):
    try: main(L.get(),R.get())
    except: ans_label.config(text='>>>  Error!')

def reset(event=None):
    L.delete(0,'end')
    R.delete(0,'end')
    ans_label.config(text='')

def history():
    try: startfile('history.txt')
    except:
        a=open('history.txt','w')
        a.close()
        try: startfile('history.txt')
        except: pass
    
def f():
    pass

def Exit(event=None):
    root.destroy()

root=Tk()
root.geometry('700x200+300+200')
root.config(background='navyblue')
root.overrideredirect(True)

Label(root,text='Enter the equation/reaction.',bg='navyblue',fg='white').place(x=10,y=10)
Label(root,text='CHEMICAL REACTION BALANCER',bg='navyblue',fg='white',font=('Algerian')).place(x=210,y=10)
Label(root,text='Format: CaO2H2+HCl  -->  CaCl2+H2O',bg='navyblue',fg='white').place(x=482,y=10)

L=Entry(root,width=53)
L.place(x=10,y=50)

Label(root,text='-->',bg='navyblue',fg='white').place(x=338,y=48)

R=Entry(root,width=53)
R.place(x=365,y=50)

Button(root,text='Balance',bg='navyblue',fg='white',command=balance,relief='groove').place(x=320,y=100)

ans_label=Label(root,text='',bg='navyblue',fg='white')
ans_label.place(x=10,y=140)

Label(root,text='@ TD',bg='navyblue',fg='white').place(x=10,y=170)
Label(root,text='v 1.0',bg='navyblue',fg='white').place(x=90,y=170)
Label(root,text='Standard keyboard key included.',bg='navyblue',fg='white').place(x=250,y=170)
Button(root,text='Exit',bg='navyblue',fg='white',command=Exit,relief='groove').place(x=660,y=170)
Button(root,text='Reset',bg='navyblue',fg='white',command=reset,relief='groove').place(x=610,y=170)
Button(root,text='History',bg='navyblue',fg='white',command=history,relief='groove').place(x=550,y=170)

root.bind('<Return>',balance)  # press enter to automatiocally clivck balance button
root.bind('<Escape>',Exit)      # to destroy root window 
root.bind('<F5>',reset)         # to reset Entry label and others

root.mainloop()

