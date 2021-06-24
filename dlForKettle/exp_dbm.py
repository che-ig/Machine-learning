import dbm

db = dbm.open('captions', 'c')

db['cleese.png'] = 'Фотография Ивана Клизина.'

print(db['cleese.png'].decode('utf-8'))

db.close()

formatStr = 'It costs %d dollars' % 23
print(formatStr)