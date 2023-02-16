import React from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';

function DisbursementSave() {

    const navigate = useNavigate();

    const { register, handleSubmit, formState: { errors } } = useForm();

    function saveData(data){
        console.log('/////////////////');
        console.log(data);

        axios.post(`http://localhost:8000/dis/disbursment/`, data, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          });
          
        console.log('*************************');
    }

  return (
    <div>
        <form onSubmit={handleSubmit(saveData)} encType='multipart/form-data'>
            <center><h2>DISBURSTMENT MODEL</h2></center>
            <center><label htmlFor='id' ><b>ID</b></label></center>
            <input id='id' {...register('id' , { required: true, pattern: /^[0-9]+$/i })} className='form-control' /><br />
            {errors.id && <span style={{color:'Red'}}><b>This field is required</b></span>}
            {errors?.id?.type === "pattern" && (<p style={{color:'Red'}} ><b>Only numbers are allowed</b></p>)}
            
            <center><label htmlFor='loan' ><b>LOAN ID</b></label></center>
            <input id='loan' {...register('loan' , { required: true , pattern: /^[0-9]+$/i })} className='form-control' /><br />
            {errors.loan && <span style={{color:'Red'}}><b>This field is required</b></span>}
            {errors?.loan?.type === "pattern" && (<p style={{color:'Red'}} ><b>Only numbers are allowed</b></p>)}
            
            
            <center><label htmlFor='doc' ><b>INSURANCE DOCUMENT</b></label></center>
            <input id='doc' type='file' {...register('insurance_doc' , { required: true })} className='form-control' onChange={"handleFileChange"} /><br />
            {errors.insurance_doc && <span style={{color:'Red'}}><b>This field is required</b></span>}

            <center><label htmlFor='pay' ><b>PAYMENT MODE</b></label></center>
            <select id='pay' {...register('payment_mode' , { required: true })} className='form-control'>
                <option>ONLINE</option>
                <option>CASH</option>
                <option>CHEQUE</option>
            </select><br />
            {errors.payment_mode && <span style={{color:'Red'}}><b>This field is required</b></span>}

            <center><label htmlFor='net' ><b>NET DISBURSED AMOUNT</b></label></center>
            <input id='net' {...register('net_disbursed_amount' , { required: true })} className='form-control' /><br />
            {errors.net_disbursed_amount && <span style={{color:'Red'}}><b>This field is required</b></span>}
            <center><label htmlFor='acc' ><b>AMOUNT DISBURSED TO A/C</b></label></center>
            <input id='acc' {...register('disbursed_to_account_no' , { required: true })} className='form-control' /><br />
            {errors.disbursed_to_account_no && <span style={{color:'Red'}}><b>This field is required</b></span>}
            <center><label htmlFor='receipt' ><b>RECEIPT</b></label></center>
            <input id='receipt' type='file' {...register('receipt_doc' , { required: true })} className='form-control' onChange={"handleFileChange"} /><br />
            {errors.receipt_doc && <span style={{color:'Red'}}><b>This field is required</b></span>}
            <center><label htmlFor='status' ><b>STATUS</b></label></center>
            <select id='status' {...register('status' , { required: true })} className='form-control'>
                <option>PENDING</option>
                <option>DISBURSED</option>
            </select><br /><br />
            {errors.status && <span style={{color:'Red'}}><b>This field is required</b></span>}
            <center><input type='submit'  value='SAVE' className='btn btn-success col-2' />
            <input type='reset' value='RESET' className='btn btn-warning col-2' /></center>
            <br /><br />
        </form>
    </div>
  )
}

export default DisbursementSave;