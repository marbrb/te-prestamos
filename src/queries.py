import MySQLdb

def serializar(campos, valores):
    """serializar estructuras a json"""
    r = []
    for y in valores:
        r.append([str(x) for x in y])

    json = []
    for x in r:
        d = {}
        for i in range(len(campos)):
            d[campos[i]] = x[i]
        json.append(d)
        del d

    return json

def actualizar_credito(id_credito, concepto_cliente):
    db = MySQLdb.connect(passwd="teamito123", db="teprestamos")
    c = db.cursor()

    if concepto_cliente == "aceptado":
        c.execute("update creditos set concepto_cliente=%s where id_credito=%s",("aceptado", id_credito))
        db.commit()
        c.close()
        return 1

    elif concepto_cliente == "rechazado":
        c.execute(
        "UPDATE creditos SET concepto_cliente=%s, activo=%s WHERE id_credito=%s",
        ("rechazado",False,id_credito))
        db.commit()
        c.close()
        return 1

    else:
        c.close()
        return 0

def crear_credito(id_cliente, interes, monto):
    """regitrar nuevo credito en la BD"""
    if int(monto) > 10000000:
        estado = 'denegado'
    elif int(monto) < 1000000:
        estado = 'pendiente'
    else:
        estado = 'aprobado'

    if estado != 'denegado':
        activo = True
    else:
        activo = False

    db = MySQLdb.connect(passwd="teamito123", db="teprestamos")
    c = db.cursor()
    res = c.execute(
    """
    INSERT INTO creditos (id_cliente,estado,activo,monto,interes) VALUES
    (%s,%s,%s,%s,%s)""",(id_cliente,estado,activo,monto,interes)
    )
    db.commit()
    return res

def actualizar_pago(id_pago, estado):
    """actualizar un pago realizado"""
    if (estado != 'hecho' and estado == 'pendiente'):
        return 0
    db = MySQLdb.connect(passwd="teamito123", db="teprestamos")
    c = db.cursor()
    res = c.execute("UPDATE pagos SET estado=%s WHERE id_pago=%s",(estado, id_pago))
    c.close()
    db.commit()
    return res

def obtener_pagos(id_credito):
    """obtenr pagos del credito id_credito"""
    db = MySQLdb.connect(passwd="teamito123", db="teprestamos")
    c = db.cursor()
    c.execute("SELECT * FROM pagos WHERE id_credito=%s",(id_credito,))
    res = c.fetchall()
    campos = ("id_pago",'id_credito','fecha_pago','monto','estado')
    r = []


    if res:
        json = serializar(campos, res)
        return json
    else:
        return r

def obtener_creditos(id_cliente):
    """obtener creditos del cliente id_cliente"""
    db = MySQLdb.connect(passwd="teamito123", db="teprestamos")
    c = db.cursor()
    c.execute('SELECT * FROM creditos WHERE id_cliente=%s',(id_cliente,))
    res = c.fetchall()
    c.close()
    campos = (
        'id_credito','id_cliente','estado','fecha_solicitud',
        'activo','monto','interes','concepto_cliente'
        )
    r = []
    if res:
        json = serializar(campos, res)
        return json
    else:
        return r


def obtener_cliente(cookie):
    """ verificar si la cookie que tiene el usuiario existe en la BD """
    db = MySQLdb.connect(passwd="teamito123", db="teprestamos")
    c = db.cursor()
    c.execute("SELECT id_cliente FROM cookies WHERE cookie=%s",(cookie,))
    res = c.fetchone()
    c.close()
    if res:
        return res[0]
    else:
        return ""

def registrar_cookie(id_cliente, passwd, cookie):
    """registrar la cookie  del usuiario en la BD"""
    db = MySQLdb.connect(passwd="teamito123", db="teprestamos")
    c = db.cursor()
    c.execute(
        "SELECT id_cliente, password FROM clientes WHERE id_cliente=%s AND password=%s",(id_cliente,passwd,)
    )

    if c.fetchall():
        c.execute("UPDATE cookies SET cookie=%s WHERE id_cliente=%s",(cookie, id_cliente))
        db.commit()
        c.close()
        return True
    else:
        return False
