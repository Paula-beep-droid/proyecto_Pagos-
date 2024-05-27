from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import configuration
from flask_cors import CORS



app = Flask (__name__)

# Connection DB
app.config.from_object(configuration['development'])
conex = MySQL(app)
CORS(app)


# Main
@app.route('/')
def root():
    return jsonify({'message':'Root Proyecto - Pagos Horas'})


# CRUD empleado

#Leer todos los empleados registrados
@app.route('/listar_empleados', methods=['GET'])
def listar_empleados():
        try:
             mycursor = conex.connection.cursor()
             querySql = "SELECT * FROM empleado ORDER BY cedula ASC"
             mycursor.execute(querySql)
             data = mycursor.fetchall()
             empleados = []
             for row in data:
                empleado = {'id':row[0], 'cedula':row[1], 'nombre':row[2], 'celular':row[3], 'correo':row[4], 'password':row[5], 'id_cargo':row[6]} 
                empleados.append(empleado)
            #print(data)
             return jsonify({'empleados': empleados, 'message': 'Listado de Empleados'})   
        except Exception as ex:
            return jsonify({'message': 'Ha ocurrido un fallo, por favor intente mas tarde.'})   
        
#Leer el registro de un solo empleado
@app.route('/listar_un_empleado/<cedula>', methods=['GET'])
def leer_empleado(cedula):
        try:
             mycursor = conex.connection.cursor()
             querySql = "SELECT * FROM empleado WHERE cedula = '{0}'".format(cedula)
             mycursor.execute(querySql)
             data = mycursor.fetchone()
             if data != None:
                  empleado = {'id':data[0], 'cedula':data[1], 'nombre':data[2], 'celular':data[3], 'correo':data[4], 'password':data[5], 'id_cargo':data[6]} 
                  return jsonify({'empleado': empleado, 'message': 'Empleado encontrado.'})   
             else: 
                  return jsonify({'message': 'Empleado no encontrado.'})   
        except Exception as ex:
            return jsonify({'message': 'Ha ocurrido un fallo, por favor intente mas tarde.'})  
        
#Registrar un empleado
@app.route('/registrar_empleados', methods=['POST'])
def registrar_empleado():
        try:
              #print(request.json)
              mycursor = conex.connection.cursor()
              querySql = """INSERT INTO empleado (cedula,nombre,celular,correo,password,id_cargo)
              VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')""".format(request.json['cedula'],request.json['nombre'],
              request.json['celular'],request.json['correo'],request.json['password'],request.json['id_cargo'])
              mycursor.execute(querySql)
              conex.connection.commit()#Confirma la acción de inserción
              return jsonify({'message': 'Empleado registrado.'})   
        except Exception as ex:
            return jsonify({'message': 'Ha ocurrido un fallo, por favor intente mas tarde.'})   

#Actualizar los datos de un empleado
@app.route('/actualizar_datos_empleado/<cedula>', methods=['PUT'])
def actualizar_empleado(cedula):
        try:
              mycursor = conex.connection.cursor()
              querySql = """UPDATE empleado SET celular ='{0}', correo ='{1}',
                      password ='{2}', id_cargo = '{3}' WHERE cedula ={4}""".format(
                      request.json['celular'], request.json['correo'], request.json['password'],
                      request.json['id_cargo'], cedula)
              mycursor.execute(querySql)
              conex.connection.commit()
              return jsonify({'message': 'Empleado actualizado.'})   
        except Exception as ex:
            return jsonify({'message': 'Ha ocurrido un fallo, por favor intente mas tarde.'})   

#Eliminar un empleado
@app.route('/eliminar_empleado/<cedula>', methods=['DELETE'])
def eliminar_empleado(cedula):
        try:
              mycursor = conex.connection.cursor()
              querySql = "DELETE FROM empleado WHERE cedula = {0}".format(cedula)
              mycursor.execute(querySql)
              conex.connection.commit()#Confirma la acción de inserción
              return jsonify({'message': 'Empleado eliminado.'})   
        except Exception as ex:
            return jsonify({'message': 'Ha ocurrido un fallo, por favor intente mas tarde.'})   
        
#CRUD pagos

#Generar el pago de un empleado por cédula 
@app.route('/calcularpagoempleado', methods = ['POST'])
     
def calcular_pago_empleado():
        try:
             
             request_data = request.json
             cedula = request_data['cedula']
             horas_trabajadas = request_data['horas_trabajadas']
             horas_extra = request_data['horas_extra']
             fecha_pago = request_data['fecha_pago']
        
             mycursor = conex.connection.cursor()
             
             querySqlcalcularpago = """SELECT valorHoraTrabajada, valorHoraExtra 
             FROM cargo JOIN empleado ON cargo.id = empleado.id_cargo WHERE empleado.cedula = '{0}'""".format(cedula)
             mycursor.execute(querySqlcalcularpago)
             data = mycursor.fetchone()
             if data:
                valorHoraTrabajada = data[0]
                valorHoraExtra = data[1]
                pago = (horas_trabajadas * valorHoraTrabajada) + (horas_extra*valorHoraExtra)
                query_agregar_pago = """INSERT INTO pagos (cedula, cantidadHorasTrabajadas, cantidadHorasExtra, valorPago, fecha_pago) VALUES
                 ('{0}','{1}','{2}','{3}','{4}')""".format(cedula,horas_trabajadas,horas_extra,pago,fecha_pago)
                mycursor.execute(query_agregar_pago)
                conex.connection.commit()
                return jsonify({
                'pago': {
                    'horas_trabajadas': horas_trabajadas,
                    'horas_extra': horas_extra,
                    'valor_pago': pago,
                    'fecha_pago': fecha_pago
                }
                })
             else:
                return jsonify({'message': 'No se encontraron registros para el empleado con cédula {0}.'.format(cedula)})
             
            
        except Exception as ex:
            return jsonify({'message': 'Ha ocurrido un fallo, por favor intente mas tarde.'})


        
@app.route('/listar_todos_los_pagos_un_empleado/<cedula>', methods=['GET'])
def listar_pagos_empleado(cedula):
         try:
             mycursor = conex.connection.cursor()
             querySql = "SELECT cantidadHorasTrabajadas, cantidadHorasExtra, valorPago, fecha_pago FROM pagos WHERE cedula ='{0}' ORDER BY id_pago ASC ".format(cedula)
             mycursor.execute(querySql)
             
             data = mycursor.fetchall()
             pagos = []
             for row in data:
                pago = {'cantidadHorasTrabajadas':row[0], 'cantidadHorasExtra':row[1], 'valorPago':row[2], 'fecha_pago':row[3]} 
                pagos.append(pago)
             return jsonify({'pagos_del_empleado': pagos, 'message': 'Listado de Pagos'})   
         except Exception as ex:
            return jsonify({'message_error': 'Ha ocurrido un fallo, por favor intente mas tarde.'}) 
        
        
        



# Funcion Pagina no encontrada
def pagina_no_encontrada(error):
        return "<h1>La URL a la que estás accediendo no fué encontrada.</h1>", 404

if __name__ == '__main__':
    app.config.from_object(configuration['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()