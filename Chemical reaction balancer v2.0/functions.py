from os import startfile
import sympy
import re

ELEMENT_CLAUSE = re.compile("([A-Z][a-z]?)([0-9]*)")

def parse_compound(compound):
    assert "(" not in compound, "This parser doesn't grok subclauses"
    return {el: (int(num) if num else 1) for el, num in ELEMENT_CLAUSE.findall(compound)}

def Calculate(L,R):
    try:
        
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
        
        

        File=open('D:/history.txt','a')
        File.write(ANS+'\n')
        File.close()
        return ANS
    except Exception as Error:
        return Error

    




def History():
    try: startfile('D:/history.txt')
    except:
        a=open('D:/history.txt','w')
        a.close()
        try: startfile('D:/history.txt')
        except: pass
