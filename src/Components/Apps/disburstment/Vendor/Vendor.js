import React from 'react';
import {useForm} from 'react-hook-form';
import {useNavigate} from 'react-router-dom';                           
import { addVendorFile } from '../../APIServices/APIservices';

function Vendor() {

                const {register, handleSubmit} = useForm();
                const navigate = useNavigate()
                
                async function sendData(data){
                  const resp = await addVendorFile(data)
                  if (resp.status === 201){
                    navigate('/show')

                  
                }
             
              
              }
  return (                                                      
    <>
        <h1 style={{color:'red'}}><center><b>VENDOR DEPT </b></center></h1>
        <div className='bg-light'>
            
            <form onSubmit={handleSubmit(sendData)} className='container jumbotron'>
                <label htmlFor='application'><b>Application </b></label>
                <input type='text' id='application' className='form-control' {...register('application',{ required: true, maxLength: 10 })}></input>
                <br></br>
                <label htmlFor='name'><b>Name </b></label>
                <input type='text' id='name' className='form-control' {...register('name',{ required: true, maxLength: 20 })}></input>
                <br></br>
                <label htmlFor='vendor_type'><b>Vendor_Type </b></label>
                <input type='text' id='vendor_type' className='form-control' {...register('vendor_type',{ required: true, maxLength: 30 })}></input>
                <br></br>
                <label htmlFor='email'><b>Email </b></label>
                <input type='email' id='email' className='form-control' {...register('email',{ required: true, maxLength: 50 })}></input>
                <br></br>
                <label htmlFor='address'><b>Address </b></label>
                <input type='textfield' id='address' className='form-control' {...register('address',{ required: true, maxLength: 50 })}></input>
                <br></br>
                <label htmlFor='city'><b>City </b></label>
                <input type='text' id='city' className='form-control' {...register('city',{ required: true, maxLength: 20 })}></input>
                <br></br>
                <label htmlFor='state'><b>State </b></label>
                <input type='text' id='state' className='form-control' {...register('state',{ required: true, maxLength: 20 },)}></input>
                <br></br>
                <label htmlFor='country'><b>Country </b></label>
                <input type='text' id='country' className='form-control'{...register('country',{ required: true, maxLength: 5 })}></input>
                <br></br>
                <label htmlFor='pin_code'><b>Pin_Code </b></label>
                <input type='number' id='pin_code' className='form-control'{...register('pin_code',{ required: true, maxLength: 6 })}></input>
                <br></br>
                <label htmlFor='mobile'><b>Mobile </b></label>
                <input type='text' id='mobile' className='form-control'{...register('mobile',{ required: true, maxLength: 10 })}></input>
                <br></br>
                <label htmlFor='bank_name'><b>Bank_Name </b></label>
                <input type='text' id='bank_name' className='form-control'{...register('bank_name',{ required: true, maxLength: 15 })}></input>
                <br></br>
                <label htmlFor='passbook_copy'><b>Passbook_Copy </b></label>
                <input type='file' name='passbook_copy' accept=".jpg, .jpeg, .png,.pdf" id='passbook_copy' value=""  className='form-control' {...register('passbook_copy')}></input>
                <br></br>
                <label htmlFor='current_account_no'><b>Current_account_no </b></label>
                <input type='text' id='current_account_no' className='form-control'{...register('current_account_no',{ required: true, maxLength: 12 })}></input>
                <br></br>
                <label htmlFor='ifsc_code'><b>IFSC_code </b></label>
                <input type='text' id='ifsc_code' className='form-control'{...register('ifsc_code',{ required: true, maxLength: 8 })}></input>
                <br></br>
                <input type='submit' value='ADD VENDOR' className='btn btn-success col-4'></input>
        
                <input type='reset' value='RESET' className='btn btn-danger col-4 float-end'></input>
        
            </form>
        </div>
    
    </>
  )
}

export default Vendor;