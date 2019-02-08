import math

def Start():
    z0=float(input("Enter characteristic impedance: "))
    freq=input("Enter frequency: ")
    prefix=freq[len(freq)-1]
    value=float(freq.split(prefix)[0])
    if (prefix.lower=="k"):
        value=value*1000
    elif (prefix=="M"):
        value=value*1000000
    elif (prefix=="G"):
        value=value*1000000000
    elif (prefix=="m"):
        value=value/1000
    elif (prefix=="u"):
        value=value/1000000
    elif (prefix=="n"):
        value=value/1000000000
    elif (prefix=="p"):
        value=value/1000000000000
    Main(value, z0)


def Main(freq, z0):
    for x in range(3):
        print("")
    inp=input("Enter inductance: ")
    prefix=inp[len(inp)-1]
    value=float(inp.split(prefix)[0])
    if (prefix=="m"):
        value=value/1000
    elif (prefix=="u"):
        value=value/1000000
    elif (prefix=="n"):
        value=value/1000000000
    elif (prefix=="p"):
        value=value/1000000000000

    wl=(2*math.pi*freq*value)
    denom=(z0*z0)+(wl*wl)
    real=((wl*wl)-(z0*z0))/denom
    imag=(z0*2*wl)/denom
    print(str(real)+" + j"+str(imag))
    Main(freq, z0)


Start()
