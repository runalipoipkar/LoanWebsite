import React from 'react'
import { useState } from "react"

function Gst() {
    const [loan,setloan]=useState();
    const [tax,settax]=useState();
    const[gst,setgst]=useState();
     
    function Calculate()
    {
        console.log(loan);
        let tax = (loan * 0.02 * gst)/100;
        settax(tax);
        console.log(tax);
    }


  return (
    <div classNameName="container">
        <h3>GST Calculator</h3>
        <div className="form-group">
            <label>Loan Amount</label>
            <input type="number" onChange={ event =>setloan(event.target.value)} className="form-control" placeholder='Enter Loan Amount'/>
            
        </div>

        <div className="form-group">
            <label>GST Rate</label>
            <input type="text" className="form-control"  placeholder='18 % on services ' onChange={ event =>setgst(event.target.value)} />
        </div>

        <div className="form-group">
            <label>Tax Amount</label>
            <input type="number" className="form-control" placeholder='Tax' value={ tax }/>
        </div>

        <button type="submit" onClick={Calculate} className="btn btn-primary mt-4">Submit</button>
    </div>
  )
}

export default Gst;