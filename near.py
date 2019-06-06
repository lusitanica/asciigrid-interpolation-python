from string import split
#x,y = 612615.530, 4183256.95 #LLC
x,y = 612775.53, 4183256.95 #LRC
#x,y = 612707.458,   4183401.703 #308.617
ncols = 21
nrows = 21
xcorner = 612615.530
ycorner = 4183256.95
cell = 8.0

a = open("grid.txt")
registo = a.readlines()
a.close()

vec=[]
for i in range(nrows):
    colunas = split(registo[nrows-1-i]," ")
    colunas.pop()
    vec.append(colunas)

def near(x,y,xcorner,ycorner,cell):
    n=int(round((x-xcorner)/cell))
    m=int(round((y-ycorner)/cell))
    return m,n
 
if ( xcorner <= x <= xcorner + (ncols-1) * cell ) & ( ycorner <= y <= ycorner + (nrows-1) * cell ):
  m,n = near(x,y,xcorner,ycorner,cell)
  cota = vec[m][n]
else:
  cota = "falso"
print cota
print m,n
