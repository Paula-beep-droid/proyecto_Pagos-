import React, { useEffect, useState } from 'react';
import Servicio_pago from '../servicios/pagos_servicio';
import { Link } from 'react-router-dom';

const FormularioHoras = () => {


    const [cedula, setCedula] = useState('');
    const [horas_trabajadas, setHorasTrabajadas] = useState('');
    const [horas_extra, setHorasExtra] = useState('');
    const [fecha_pago, setFechaPago] = useState('');
    const [resultadoPago, setResultadoPago] = useState(null);

    const guardar_pago = (e) => {
        e.preventDefault();

        Servicio_pago.postPagoEmpleado(parseInt(cedula, 10), parseInt(horas_trabajadas, 10), parseInt(horas_extra, 10), fecha_pago)
            .then((response) => {
                console.log(response.pago);
                setResultadoPago(response.pago);
            }).catch(error => {
                console.log(error)
            })
    }

    return (
        <div>
            <div className='container'>
                <div className='row'>
                    <div className='card col-m-6 offset-md-3 offset-md-3'>
                        <h2 className='text-center'> Formulario Pagos</h2>
                        <div className='card-body'>
                            <form onSubmit={guardar_pago}>
                                <div className='form-group mb-2'>
                                    <label className='form-label'> Cédula:</label>
                                    <input
                                        type='text'
                                        placeholder='Digite su cédula'
                                        name='cedula'
                                        className='form-control'
                                        value={cedula}
                                        onChange={(e) => setCedula(e.target.value)}
                                    />
                                </div>
                                <div className='form-group mb-2'>
                                    <label className='form-label'> Horas trabajadas:</label>
                                    <input
                                        type='text'
                                        placeholder='Digite las horas trabajadas'
                                        name='horas_trabajadas'
                                        className='form-control'
                                        value={horas_trabajadas}
                                        onChange={(e) => setHorasTrabajadas(e.target.value)}
                                    />
                                </div>
                                <div className='form-group mb-2'>
                                    <label className='form-label'> Horas extra:</label>
                                    <input
                                        type='text'
                                        placeholder='Digite las horas extra'
                                        name='horas_extra'
                                        className='form-control'
                                        value={horas_extra}
                                        onChange={(e) => setHorasExtra(e.target.value)}
                                    />
                                </div>
                                <div className='form-group mb-2'>
                                    <label className='form-label'> Selecciona la fecha de pago:</label>
                                    <input
                                        type='date'
                                        placeholder='Digite la fecha'
                                        name='horas_extra'
                                        className='form-control'
                                        value={fecha_pago}
                                        onChange={(e) => setFechaPago(e.target.value)}
                                    />
                                </div>
                                <button type='submit' className='btn btn-success' > Calcular Pago</button>
                            </form>

                        </div>
                        {resultadoPago && (
                            <div className='mt-3'>
                                <h3>Resultado del Pago</h3>
                                <p>Cantidad de horas trabajadas: {resultadoPago.horas_trabajadas}</p>
                                <p>Cantidad de horas extra: {resultadoPago.horas_extra}</p>
                                <p>Valor del pago: {resultadoPago.valor_pago}</p>
                                <p>Fecha del pago: {resultadoPago.fecha_pago}</p>
                                <Link to={`/historial-pagos/${cedula}`} className='btn btn-primary mb-2'>Ver historial de pagos</Link>
                            </div>
                        )}
                    </div>
                </div>

            </div>

        </div>
    )
}

export default FormularioHoras;

