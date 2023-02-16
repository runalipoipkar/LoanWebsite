import React from 'react'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import Layout from './Components/Layout/Layout';
import {BrowserRouter ,Router,Route, Routes} from 'react-router-dom';
import AddUser from './Components/Apps/admin_app/AddUser';
import GST from './Components/GST/Gst';
import UserShow from './Components/Apps/admin_app/ShowUser';
import DisbursementSave from './Components/Apps/disburstment/Disbursmentmodel/DisbursementAdd';
import Disbursement from './Components/Apps/disburstment/Disbursmentmodel/Disbusement';

function App() {
  return (
    <div>
      <BrowserRouter>
      <Layout />
      <Routes>
      <Route path="/add" element={<AddUser />} />
      <Route path="/show" element={<UserShow />}/>
      <Route path="/gst" element={<GST />}/>
      <Route path="/disadd" element={<DisbursementSave />}/>
      <Route path='/disshow' element={<Disbursement />} />
        
      </Routes>
      </BrowserRouter>
      
    </div>
  )
}

export default App;