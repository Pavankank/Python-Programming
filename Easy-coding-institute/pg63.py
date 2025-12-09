project1 = {'Madison Porter', 'Paige Sanders', 'Emily Chen', 'Andrew Douglas', 'Mia Hernandez', 'Isabella Brown', 'Noah Kim', 'Piper Douglas', 'Tyler Russell', 'Mason Davis', 'Lily Ross', 'Ophelia Lane', 'Benjamin Harris', 'Harper Thompson', 'Ava Lee', 'Charlotte Taylor', 'Oliver White', 'Riley Pierce', 'Abigail Russell', 'Sophia Rodriguez', 'Hannah Norris', 'Sydney Wallace', 'Ryan Jenkins', 'Kayla Brooks', 'William Walker', 'Avery Foster', 'Samantha Pierce', 'Gabriel Powell', 'Daniel Webb', 'Sofia Jenkins', 'Lauren Jenkins', 'Zoey Lane', 'Ethan Hall', 'Anthony Bishop', 'Amelia Martin', 'Joshua Pierce', 'Logan Jackson', 'Christopher Coleman', 'Caleb Martin', 'Liam Patel', 'Elijah Watson', 'Michael Simmons', 'James Reed', 'Alexander Gray', 'Cameron Martin'}

project2 = {'Remi Sanchez', 'Piper Douglas', 'Nalani Cruz', 'Jaxon Brooks', 'Elowen Walker', 'Paisley Jenkins', 'Kalliope Martin', 'Kynzie Lee', 'August Harris', 'Kai Russell', 'Lily Ross', 'Ophelia Lane', 'Galatea Sanchez', 'Wren Porter', 'Sylvia Pierce', 'Zane Bishop', 'Sage Walker', 'Vesper Sanders', 'Journey Jenkins', 'Gavin Pierce', 'Freya Lewis', 'Willow Webb', 'Magnolia Reed', 'Aiden Foster', 'Juliana Lee', 'Sawyer White', 'Caspian Coleman', 'Marley Davis', 'Lilyana Cruz', 'Cohen Gray', 'Rowan Hall', 'Orion Wallace', 'Maverick Russell', 'Indigo Taylor', 'Kieran Harris', 'Eleanor Patel', 'Thane Patel', 'Lyric Brooks', 'Jace Foster', 'River Bishop', 'Beckett Powell', 'Caleb Martin'}

comman_emp = project1.intersection(project2)
print(len(comman_emp), "employees are working in both the projects.")

print("\nBelow are the common employees:")
for emp in comman_emp:
    print(emp)