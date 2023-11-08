import serial
import sqlite3

database_path = 'instance/db.sqlite'

def get_db():
    db = sqlite3.connect(
            database_path,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
    db.row_factory = sqlite3.Row    
    return db

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)  # open serial port
print(f"se conectó a {ser.name}")       

try:
    while True:
        if (ser.inWaiting() > 0):
            valor = int(ser.readline())
            print(f"se leyó: {valor}")
            db = get_db()
            db.execute("INSERT INTO sensor_values (value) VALUES (?)",
                                (valor,))
            db.commit()
except KeyboardInterrupt:
    print('!!FINISH!!')
    db.close()
    ser.close()
    
# cosas para la presentacionmostrar que sensa y la intervencion esa seria la presentacion osea
#  basicamente mostrar para que
# sirve y explicar lo que haciendo 





