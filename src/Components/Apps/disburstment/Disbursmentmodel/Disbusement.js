import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { NavLink } from 'react-router-dom';

function Disbursement() {

  const [ disburse, setDisburse ] = useState([]);

  async function fetchDisbursement(){
    const result = await axios.get(`http://127.0.0.1:8000/dis/disbursement/`);
    console.log(result.data);
    setDisburse(result.data);
  }
 
  useEffect(()=> {fetchDisbursement()}, []);

  return (
    <div>
      <table className='table table-bordered table-hover'>
        <thead>
          <tr>
            <th>ID</th>
            <th>LOAN</th>
            <th>INSURANCE DOCUMENT</th>
            <th>PAYMENT MODE</th>
            <th>NET DISBURSED AMOUNT</th>
            <th>AMOUNT DISBURSED TO A/C</th>
            <th>RECEIPT</th>
            <th>STATUS</th>
            <th>RESPONSED</th>
            <th>ACTIONS</th>
          </tr>
        </thead>
        <tbody>
          {
            disburse.map(obj=>{
              return (
                <tr>
                    <td>{obj.id}</td>
                    <td>{obj.loan}</td>
                    <td>{obj.insurance_doc}</td>
                    <td>{obj.payment_mode}</td>
                    <td>{obj.net_disbursed_amount}</td>
                    <td>{obj.disbursed_to_account_no}</td>
                    <td>{obj.receipt_doc}</td>
                    <td>{obj.status}</td>
                    <td>{obj.response_timestamp}</td>
                    <td>
                      <NavLink to={`/update/disbursement/${obj.id}`}><button>UPDATE</button></NavLink>
                    </td>
                </tr>
              )
            })
          }
        </tbody>
      </table>
    </div>
  )
}

export default Disbursement;