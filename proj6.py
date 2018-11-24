'''Project_6'''

def KUW_DINAR(pound):
    return pound * 2.56

def DOL(pound):
    return pound * 0.78

def CAN_DOL(pound):
    return pound * 0.59

def NZ_DOL(pound):
    return pound * 0.53

def GT_QET(pound):
    return pound * 0.1

def ARG_PESO(pound):
    return pound * 0.021

def RUB(pound):
    return pound * 0.012

def JAP_YEN(pound):
    return pound * 0.0069

def main():
    K_R = int(input())
    D = int(input())
    C_D = int(input())
    NZ_D = int(input())
    GT_Q = int(input())
    ARG_P = int(input())
    R = int(input())
    J = int(input())
    POUND = KUW_DINAR(K_R) + DOL(D) + CAN_DOL(C_D) + NZ_DOL(NZ_D) + GT_QET(GT_Q) + ARG_PESO(ARG_P) + RUB(R) + JAP_YEN(J)
    POUND_I = int(POUND)
    PEN = int((POUND - POUND_I) * 100)
    print(POUND_I, 'POUNDS STERLING')
    print(PEN, 'PENNY')

if __name__ == '__main__':
    main()