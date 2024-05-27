import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Servicio_pago from '../servicios/pagos_servicio';

const Historial_pagos = () => {

    const { cedula } = useParams();
    const [todos_los_pagos, setPagos] = useState([]);

    useEffect(() => {
        Servicio_pago.getHistorialPagosEmpleado(cedula)

            .then((response) => {
                console.log(response.pagos_del_empleado);
                setPagos(response.pagos_del_empleado);
            }).catch((error) => {
                console.log(error.message_error);
            });
    }, [])

    return (
        <div className='container'>
            <h2 className='text-center'>Historial de Pagos</h2>
            <table className='table table-bordered table-striped'>
                <thead>
                    <tr>
                        <th>Cantidad horas trabajadas</th>
                        <th>Cantidad Horas Extra</th>
                        <th>Valor pago</th>
                        <th>Fecha pago</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        todos_los_pagos?.map((pagos,index) => (
                            <tr key={index}>
                                <td>{pagos.cantidadHorasTrabajadas}</td>
                                <td>{pagos.cantidadHorasExtra}</td>
                                <td>{pagos.valorPago}</td>
                                <td>{pagos.fecha_pago}</td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
        </div>
    );
}


export default Historial_pagos;
