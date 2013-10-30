import sqlite3
conn = sqlite3.connect('LEIA.db')
c = conn.cursor()
c.execute('''CREATE TABLE location (loc_id integer primary key asc, city text default "", postal_code text default "", state text default "", street text default "", latitude real default 0.0, longitude real default 0.0)''')
c.execute('''create table restaurant (rest_id integer primary key asc, rest_name text not null, rating real default 5.0, rest_location int not null, phone text, open int default 0, foreign key (rest_location) references location(loc_id))''')
conn.commit()
conn.close()
