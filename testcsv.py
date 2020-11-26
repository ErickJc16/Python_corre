h = [1,5,-8] #Señal Enviada
x = [3,2,1,6,-7] #Señal Recibida


result = []
for i in range((len(x) + len(h)) - 1 ):
  print("-------")
  sample = 0
  for j in range(0,-len(h),-1):
    if i - j < 0:
      continue
    if i - j > len(x) - 1:
      continue 
    sample += h[-j] * x[i-j]
    print(sample)
  result.insert(i,sample)

print(result)