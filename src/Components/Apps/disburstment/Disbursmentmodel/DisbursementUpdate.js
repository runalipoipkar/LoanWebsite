import React, { useEffect } from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function DisbursementUpdate() {

    const {userID} = useParams();

    const { register, setValue, handleSubmit } = useForm();

    async function fetchDisbursement(){
        const result = await axios.get(`http://127.0.0.1:8000/dis/disbursement/${userID}/`);
        console.log(userID);
        console.log(result.data);
        setValue('id', result.data.id);
        setValue('loan', result.data.loan);
        setValue('insurance_doc', result.data.insurance_doc);
        setValue('payment_mode', result.data.payment_mode);
        setValue('net_disbursed_amount', result.data.net_disbursed_amount);
        setValue('disbursed_to_account_no', result.data.disbursed_to_account_no);
        setValue('receipt_doc', result.data.receipt_doc);
        setValue('status', result.data.status);
    }

    function saveData(data){
        console.log(data);
        console.log(userID);
        axios.put(`http://127.0.0.1:8000/pro/disbursement/${userID}/`, data, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          });
    }

    useEffect(()=>{fetchDisbursement()}, []);

  return (
    <div>
        <form onSubmit={handleSubmit(saveData)}>
            <center><h2>UPDATE DISBURSTMENT MODEL</h2></center>
            <center><label htmlFor='id' ><b>ID</b></label></center>
            <input id='id' {...register('id')} className='form-control' readOnly='true' /><br />
            <center><label htmlFor='loan' ><b>LOAN ID</b></label></center>
            <input id='loan' {...register('loan')} className='form-control' readOnly='true' /><br />
            <center><label htmlFor='doc' ><b>INSURANCE DOCUMENT</b></label></center>
            <input id='doc' type='file' {...register('insurance_doc')} className='form-control' /><br />
            <center><label htmlFor='pay' ><b>PAYMENT MODE</b></label></center>
            <select id='pay' {...register('payment_mode')} className='form-control'>
                <option>ONLINE</option>
                <option>CASH</option>
                <option>CHEQUE</option>
            </select><br />
            <center><label htmlFor='net' ><b>NET DISBURSED AMOUNT</b></label></center>
            <input id='net' {...register('net_disbursed_amount')} className='form-control' /><br />
            <center><label htmlFor='acc' ><b>AMOUNT DISBURSED TO A/C</b></label></center>
            <input id='acc' {...register('disbursed_to_account_no')} className='form-control' /><br />
            <center><label htmlFor='receipt' ><b>RECEIPT</b></label></center>
            <input id='receipt' type='file' {...register('receipt_doc')} className='form-control' /><br />
            <center><label htmlFor='status' ><b>STATUS</b></label></center>
            <select id='status' {...register('status')} className='form-control'>
                <option>PENDING</option>
                <option>DISBURSED</option>
            </select><br /><br />
            <center><input type='submit'  value='UPDATE' className='btn btn-success col-2' />
            <input type='reset' value='RESET' className='btn btn-warning col-2' /></center>
            <br /><br />
        </form>
    </div>
  )
}

export default DisbursementUpdate;