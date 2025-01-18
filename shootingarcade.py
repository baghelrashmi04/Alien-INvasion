#aliean_color = ["yellow","black"]

#if 'green' in aliean_color :
 #   print("player just earned 5 points")
#if 'green' not in aliean_color:
#    print("you just earned 10 points")
##else:
#    print("invalid")
toppings = ['chilli','cucum','pepper','cheese','honey']
for tops in toppings:
    if toppings == "gren pepper":
        print('sorry we ran out of sezings') 
    else:
        print(f'adding{toppings}.')
print('\nfinished making your pizza')

hello_pie = ['cheese']
if hello_pie:
    for pie in hello_pie:
        print(f'adding{hello_pie}')
        print('\nfinished your pie')
else:
    print('are you sure want a pie?')


my_pie = ['ch','mr','na']
see_pie = ['chee','mree','naee','na']
for see in see_pie:
    if see in my_pie:
        print(f'adding{see_pie}')
    else:
        print(f'sorry we dont have {see_pie}')
print('\nfinished making your whatever')


name = ['rashmi','vijay','mayank','charu','parth','gagan','yug','kartik','nishi']
for nam in name:
    if nam == 'rashmi':
        print("hello rashmi would you like to see the report")
    else:
        print(f'hey{nam}')
    if name == []:
        print('we need to find some users')
    else:
        print('hekko')
removed_items = name.clear()         

rashmiii = {'color':'fair','points': 5}
print(rashmiii['color']) 
print(rashmiii['points']) 
new_points = rashmiii['points']
print(f'you just earned {new_points}points')
rashmiii['x_position'] = 0
rashmiii['y_position'] = 25
print(rashmiii)
rashmiii['stubborn'] = 100
print(rashmiii)
rashmii = {'color':'green'}
print(f'the person is {rashmii['color']}')
rashmii['color'] = 'yellow'
print(f'the person is now {rashmii['color']}')

rashmi = {'x_position':0, 'y_postion':25, 'speed':'fast'}
print(f'original postion: {rashmi['x_position']}')
if rashmi['speed'] == 'slow':
    x_increment = 1
elif rashmi['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast aliean
    x_increment = 3
rashmi['x_position'] = rashmi['x_position']+ x_increment
print(f'new position:{rashmi["x_position"]}')
point_value = rashmi.get('points')
print(point_value)
fav_number = {'ras':1,'vijay':2}
print(fav_number['ras'])
print(fav_number['vijay'])
for key, value in rashmi.items():
    print(f'\nkey: {key}')
    print(f'\nvalue: {value}')
for name in sorted(rashmi.keys()):
    print(f'{name.title()},thankyou for taking the poll')
for na in rashmi.values():
    print(f'{name.title()},thankyou for taking the poll')
    
Rashmi = [rashmi,rashmii,rashmiii]
for rash in Rashmi:
    print(rash)


## fleet of 30 alieans 
alieans = []
#for 30 green alieans
for aliean in range(30):
    new_alieans = {'speed':'slow','color':'green','point':5}
    alieans.append(new_alieans)
for ali in alieans[:3]:
    if ali['color'] =='green':
        ali['color'] = 'blue'
        ali['speed'] = 'medium'
        ali['points'] = 10
    elif ali['color'] == 'blue':
        ali['color'] = 'yellow'
        ali['speed'] = 'fast'
        ali['points'] = '25'
    
        
    
for ali in alieans[:5]:
    print(ali)
    print('...')
print(f'the total alieans are:{len(alieans)}') 

vijay = {'color':'fair','features':['nose','eyes','ears','height']}
print(f'vijay has good features{vijay['color']}- nice human''with the following features:')
for feature in vijay['features']:
    print('\t'+ feature)
    
mummy = {'nature':{'sometimes': 'bitter','otherwise':'sweet'},'availablity':{'sometimes':'yes','otherwise':'more'}}
for mum,mumy in mummy.items():
    print(f'\n mum :{mum}')
    comnature = f'{mumy['sometimes']},{mumy['otherwise']}'
    print(f'\ncomnature:{comnature.title()}')
    
message = input('Hey rashmi you want to be a global buissness leader: ')
print(message)
name = input('enter your name: ')
print(f'\nhello , {name}')
prompt ='If you could tell us who you are we can perosnalise your mssg you see: '
prompt += '\nwhat is yoour name'
namee = input(prompt)
print(f'\nhello,{namee}')
age = input('how old are you: ')
print(age)
age = int(age)
if age>=18:
  print('true')
else:
  print('wrong age')
  
num = input('Enter a number and we will tell you f the number is even or not: ')
num = int(num)
if num % 2 == 0:
    print(f'num is {num}even')
else:
    print(f'the number is {num} is odd')
    
restrau = input('tell me if how many people are you: ')
restrau =int(restrau)
if restrau>=8:
    print(f'\nsorry you have to wait')
else:
    print('you can have seat, table is ready')
    
current = 1
while current  <= 5:
    print(current)
    current = current+1
pro = input('tell me something i will repeat back to you: ')
pro += "\nenter 'quit' to end the program"
active = True
message = " "
while active:
    message = input(pro)
    if message == '6':
      break
    else:
        print(f'i would love to read the message{message.title()}')
#continue in while loop makes the programe ignore that particular conditionand retun to the initial stage of the program
number = 1 
while number<10 :
    number = number+1
    
    print(number)
unconlist = ['hello','night','day','rash']
conlist = []
while unconlist:
    curlist = unconlist.pop()
    print(f'verifying user: {curlist}')
    conlist.append(curlist)
    print('\nThe following user has been confirmerd: ')
    for con in conlist:
        print(conlist)
pets = ['cat','dog','ele','rat','cow','rabbit']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)    

responses = {}
active_poll = True
#while active_poll: 
 # name = input('what is your name')
 # response = input('\nwhich moutain would you like to climb today?: ')
 # responses[name] = response 
 # repeat = input('would you like to let another person repsond? (yes/no)')
  #if repeat =='no':
 #    active_poll = False
#print(f'\n Poll results')
#for name, response in responses.items():
    #print(f'{name} would you like to climb this {response}')
        

sandwich = ['bread','mayo','cheese','garlic']
finished_sandwich = []
while sandwich:
    ready_sand = sandwich.pop()
    print(f'ready sandwich: {ready_sand}')
    finished_sandwich.append(ready_sand)
print('\nThese sandwiches are ready')
for sand in finished_sandwich:
        print(sand)
        




        
    
    

    




