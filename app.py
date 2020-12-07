import psycopg2

conn = psycopg2.connect(
        user='mkrawiec',
        password='password',
        host='10.0.10.3',
        port='3306',
        database='mkrawiec_db',
        )

cur = conn.cursor()
create_table = 'CREATE TABLE "Uzytkownicy" (id SERIAL PRIMARY KEY, "Imie" varchar(30) NOT NULL, "Nazwisko" varchar(30) NOT NULL);'
insert_init_values = 'INSERT INTO "Uzytkownicy" ("Imie", "Nazwisko" VALUES ("Jan", "Kowalski"), ("Adam", "Malinowski"), ("Zbigniew", "Wodecki");'
select = 'SELECT * FROM "Uzytkownicy";'
cur.execute(create_table)
conn.commit()
cur.execute(insert_init_values)
conn.commit()
while True:
    number = input("1 - dodaj uzytkownika\n 2 - usun uzytkownika\n 3-aktualizuj dane uzytkownika\n 4-wyswietl uzytkownikow\n 5-koniec\n")
    if number == '1':
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        cur.execute('INSERT INTO "Uzytkownicy" ("Imie", "Nazwisko" VALUES ("%s", "%s");',imie, nazwisko)
        conn.commit()
    elif number == '2':
        id = input("Id uzytkownika: ")
        cur.execute('DELETE WHERE id=%s;', id)
        conn.commit()
    elif number == '3':
        id = input("Id uzytkownika: ")
        imie = input("Nowe imie: ")
        nazwisko = input("Nowe nazwisko: ")
        cur.execute('UPDATE "Uzytkownicy" SET "Imie"=%s, "Nazwisko"=%s WHERE id=%s;', imie, nazwisko, id)
        conn.commit()
    elif number == '4':
        cur.execute(select)
        conn.commit()
    elif number == '5':
        break
    else:
        continue

cur.close()