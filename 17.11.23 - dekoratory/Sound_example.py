from matplotlib import pyplot as plt
from math import sin, pi

# x = [float(x) for x in range(3000)] # wyrażenie listowe
# s = [sin(xi/(2*pi)/10) for xi in x]
#
# sd1 = [y**3 for y in s]
# #sd2 = [y*sin(i/(200*pi
#
# plt.plot(x,sd1)
# plt.plot(x,s)
# plt.show()
# #plt.savefig("p.png")

x = [float(x) for x in range(1000)]

def Sound_sample():
    return [sin(xi/(2*pi)/10) for xi in x]

def Power3_sample(jakis_sound):
    n = len(jakis_sound)
    for i in range(n):
        jakis_sound[i] = (jakis_sound[i]**3)
    return jakis_sound

s = Sound_sample()
po_dekoracji = Power3_sample(s)

plt.plot(x,s)
plt.plot(x,po_dekoracji)
plt.show()