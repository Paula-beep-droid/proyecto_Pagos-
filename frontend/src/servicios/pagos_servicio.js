


class Servicio_pago {
    postPagoEmpleado(cedula, horas_trabajadas, horas_extra, fecha_pago) {
        return fetch('http://127.0.0.1:5000/calcularpagoempleado', {
            method: 'POST',
            body: JSON.stringify({
                cedula: parseInt(cedula, 10),
                horas_trabajadas: parseInt(horas_trabajadas, 10),
                horas_extra: parseInt(horas_extra, 10),
                fecha_pago: fecha_pago


            }),
            headers: {
                'Content-type': 'application/json; charset=UTF-8',
            },
        }).then((response) => response.json());
    }

    getHistorialPagosEmpleado = (cedula) => {
        return fetch(`http://127.0.0.1:5000/listar_todos_los_pagos_un_empleado`+ `/`+cedula )
        .then ((response) => response.json());
    }
}



export default new Servicio_pago;

