import './App.css';


import FormularioHoras from './componentes/formulario_horas';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Historial_pagos from './componentes/historial_pagos';



function App() {
  return (
    <div>
      <BrowserRouter>
        <div className='container-form'>
          <Routes>
            <Route exact path='/' element={<FormularioHoras/>} />
            <Route exact path='/historial-pagos/:cedula' element={<Historial_pagos/>} />
          </Routes>
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
