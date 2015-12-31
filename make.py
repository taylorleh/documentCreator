from Tkinter import *
import pyperclip
import datetime

string = '''

To the hiring team at {COMPANY_NAME},

As someone with a strong interest in the future of the {INDUSTRY} industry, I am really impressed with how {COMPANY_NAME} {DESCRIPTION}. I would love to bring my passion for technology and problem solving to help {COMPANY_NAME} revolutionize the {INDUSTRY} industry. I am a full stack generalist with a strong mathematical background and a proven track record in building data driven web applications and as such I would be a perfect fit for the {POSITION} position.

My experience with a wide spectrum of web technologies makes me an ideal candidate for the role. Recently, I have built a social media website for recommending and sharing cosmetic products. I wrote the recommendation system in Python and crafted an angular view for a d3.js visualization of the user products. The products were displayed as a configurable decision tree. Each level of the tree had groups based on a user selected filter (i.e. size, brand, type). Moreover, each node and level could be toggled allowing both depth first and breadth first exploration.

I have proven experience in shipping applications and can start contributing effectively as a {POSITION} at {COMPANY_NAME}. Thank you for your consideration, and I look forward to hearing from you soon.

All the best,

Michael Sova

'''
class Field:
   def __init__(self,text,boxtype='Entry'):
      self.text = text
      self.boxtype = boxtype

fields = [Field("company name"),Field("job role"),Field("industry name"),Field("I am impressed how your company ... ",boxtype='Text')]

def write_to_file(fileName,name):
   f = open(fileName,'a')
   f.write(' name : '+name+', time applied: '+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n') 
   f.close() 

def read_the_day(fileName):
   f = open('companies','r')
   timeNow = datetime.datetime.now().strftime('%Y-%m-%d') 
   a = f.read().split('\n')
   counter = 0
   res = ''
   for i in a:
      x = i.split(': ')
      if len(x)>2:
         if x[2][:10] == timeNow:
            res+= '\n'+x[1].split(',')[0]
            counter +=1
         if counter >20:
            res = "congrats finished for the day!"

   label1.config(text='today applied to : '+str(counter)+' companies'+res)

def fetch(entries):
   input_result = [entry[1].get() for entry in entries
]
   result = string.format(COMPANY_NAME=input_result[0],POSITION=input_result[1],INDUSTRY=input_result[2],DESCRIPTION=input_result[3])
   pyperclip.copy(result)

   write_to_file('companies',input_result[0])
   read_the_day('companies')

   label.config(text='Copied '+input_result[0])


def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field.text, anchor='w')
      if field.boxtype == 'Entry':
         ent = Entry(row)
      elif field.boxtype == 'Text':
         ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Copy and show',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   label = Label(root,fg="#3333ff")
   label.pack()
   label1 = Label(root,fg="#3333ff")
   label1.pack(side=BOTTOM)
   read_the_day('companies')
   root.mainloop()