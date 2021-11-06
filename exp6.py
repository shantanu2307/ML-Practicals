import pandas as pd
hoola_loop=pd.DataFrame({"Sky":["Sunny", "Sunny", "Rainy", "Sunny"], "AirTemp":["Warm", "Warm", "Cold", "Warm"], "Humidity":["Normal", "High", "High", "High"],
                         "Wind":["Strong", "Strong", "Strong", "Strong"], "Water":["Warm", "Warm", "Warm", "Cool"], "Forecast":["Same", "Same", "Change", "Change"],"EnjoySport":["Yes", "Yes", "No", "Yes"]})
print(hoola_loop)

hoola_loop['EnjoySport']=pd.Series(map(lambda x:'+' if x is "Yes" else '-',hoola_loop['EnjoySport']))
print(hoola_loop)

answer=['phi', 'phi', 'phi', 'phi', 'phi', 'phi']
p=hoola_loop.count()
p
len(hoola_loop)
for x in range(len(hoola_loop)):
  if hoola_loop["EnjoySport"][x] is '+':
    for y in range(6):
      if answer[y] is 'phi':
        answer[y]=hoola_loop.iloc[x, y]
      elif answer[y] is not hoola_loop.iloc[x, y]:
        answer[y]='?'
print(answer)