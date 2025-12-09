from random import choice
fname = [
    "Chiranjeevi",
    "Pawan Kalyan",
    "Mahesh Babu",
    "Rama Rao",
    "Allu Arjun",
    "Ram Charan",
    "Prabhas",
    "Vijay Deverakonda",
    "Nani",
    "Sai Dharam Tej"
]

# List of smaller locations in Hyderabad
lname = [
    "Malakpet",
    "Lalapet",
    "Ameerpet",    
    "Kachiguda",
    "Chikkadpally",
    "Miyapur",    
    "Attapur",
    "Saidabad",
    "Shaikpet"
]

for k in range(25):
    l = choice(lname)
    f = choice(fname)
    fn = f'{l} {f}'
    print(fn)