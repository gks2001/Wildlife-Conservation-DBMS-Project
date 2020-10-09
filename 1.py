import sqlite3


conn = sqlite3.connect('wild.db')
c = conn.cursor()

# Create table for CLASSIFICATIONS


c.execute("CREATE TABLE cla (species text, cla text)")
conn.commit()

# Create table WILDLIFE with attributes species name and population size


c.execute("""CREATE TABLE wildlife(species text, population integer)""")
conn.commit()

# Create table for INVASIVE species


c.execute("""CREATE TABLE invasive(species text, oldpopulation integer, population integer)""")
conn.commit()

# Insert statements for the WILDLIFE table


c.execute("""INSERT INTO wildlife VALUES ('Polar Bear','20000')""")
c.execute("""INSERT INTO wildlife VALUES ('Panda','2000')""")
c.execute("""INSERT INTO wildlife VALUES ('Cheetah','10000')""")
c.execute("""INSERT INTO wildlife VALUES ('Dolphin','1000')""")
c.execute("""INSERT INTO wildlife VALUES ('Elephant','50000')""")
c.execute("""INSERT INTO wildlife VALUES ('Leopard','7000')""")
c.execute("""INSERT INTO wildlife VALUES ('Lion','50000')""")
c.execute("""INSERT INTO wildlife VALUES ('Orangutan','7000')""")
c.execute("""INSERT INTO wildlife VALUES ('Rhinoceros','20000')""")
c.execute("""INSERT INTO wildlife VALUES ('Tiger','3500')""")

conn.commit()

# Insert statements for the INVASIVE species table


c.execute("""INSERT INTO invasive VALUES ('fox','300','500')""")
c.execute("""INSERT INTO invasive VALUES ('locust','20000','34000')""")
c.execute("""INSERT INTO invasive VALUES ('Monitor','200','250')""")
c.execute("""INSERT INTO invasive VALUES ('dormice','1000','3000')""")

conn.commit()

# Create table DREASON with attributes species name and decrease in population size and the cause


c.execute("""CREATE TABLE dreason(species text, populationdecrease integer, reason text)""")
conn.commit()

# Insert initial values into the CLASSIFICATION table


c.execute("""INSERT INTO cla VALUES ('Polar Bear','Threatened')""")
c.execute("""INSERT INTO cla VALUES ('Panda','Endangered')""")
c.execute("""INSERT INTO cla VALUES ('Cheetah','Threatened')""")
c.execute("""INSERT INTO cla VALUES ('Dolphin','Critically Endangered')""")
c.execute("""INSERT INTO cla VALUES ('Elephant','Threatened')""")
c.execute("""INSERT INTO cla VALUES ('Leopard','Threatened')""")
c.execute("""INSERT INTO cla VALUES ('Lion','Threatened')""")
c.execute("""INSERT INTO cla VALUES ('Orangutan','Threatened')""")
c.execute("""INSERT INTO cla VALUES ('Rhinoceros','Threatened')""")
c.execute("""INSERT INTO cla VALUES ('Tiger','Endangered')""")

conn.commit()
conn.close()
'''
species and population sizes

polar bear - 20000
panda - 2000
cheetah - 10000
dolphins - 1000
elephant - 50000
leopard - 7000
lion - 50000
orangutan - 7000
rhinoceros - 20000
tiger - 3500

categories


threatened <= 10000
endangered <= 5000
critically endangered <= 2000
'''
