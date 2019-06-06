from string import split
#x,y = 612619.530, 4183260.95
#x,y = 612779.53, 4183256.95
x,y = 612707.458,   4183401.703 #308.617
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
    
def biaux(x,y,xcorner,ycorner,cell):
    deltax=((x-xcorner)/cell)
    n=int(deltax)
    deltax=deltax-n
    deltay=((y-ycorner)/cell)
    m=int(deltay)
    deltay=deltay-m
    return deltax,deltay,m,n

if ( xcorner < x < xcorner + (nrows-1) * cell ) & (ycorner < y < ycorner + (nrows-1) * cell ):
  deltax,deltay,m,n = biaux(x,y,xcorner,ycorner,cell)
  if divmod((x-xcorner), cell)[1] == 0:
    cota = vec[m][n]
  else:
    cota=float(vec[m][n])+deltay*(float(vec[m+1][n])-float(vec[m][n]))+deltax*(float(vec[m][n+1])-float(vec[m][n]))+deltax*deltay*(float(vec[m+1][n+1])-float(vec[m+1][n])-float(vec[m][n+1])+float(vec[m][n]))
else:
  cota = "-9999"
print m,n
print cota
