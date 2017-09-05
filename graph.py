import matplotlib as np 
import pylab as pl 
pl.plot([1,2,3,4,5,6],[8.33, 7.5, 9, 8.8, 7.5, 7.5], 'k', linewidth=1.0)
pl.annotate('8.33', xy=(1,8.33), xytext=(0.9,8.5), color='b')
pl.annotate('7.5', xy=(2,7.5), xytext=(1.9,7), color='b')
pl.annotate('9', xy=(3,9), xytext=(3,8.5), color='b')
pl.annotate('8.8', xy=(4,8.8), xytext=(3.8,8), color='b')
pl.annotate('7.5', xy=(5,7.5), xytext=(4.9,8), color='b')
pl.annotate('7.5', xy=(5,7.5), xytext=(5.9,8), color='b')
pl.ylabel('Promedio')
pl.xlabel('Semestre')
pl.title('Promedio en los semestres')
pl.axis([0.5, 6.5, 5.5, 10])
pl.grid(True)
# Guarda la grafica en formato png
pl.savefig('graph.png')
