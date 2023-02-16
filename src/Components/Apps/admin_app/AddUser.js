import React, { useState } from 'react';
import { useForm } from "react-hook-form";
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { addFile } from '../APIServices/APIservices';

function AddUser() {
    const {register,handleSubmit} = useForm();
   


    const navigate=useNavigate();

    async function SaveData(data){
        const resp = await addFile(data)
        if (resp.status==201){
            navigate('/show')
        }
        console.log(data);

    }
  return (
    <>
    <div className='container mt-3'>
        <h1><u><center>USER REGISTRATION FORM</center></u></h1>
        <form onSubmit={handleSubmit(SaveData)} className='mt-5'>
            
                <label htmlFor='first_name'><b>First Name:</b></label>                           
                <input type='text' id='first_name' className='form-control' {...register('first_name',{ required: true, maxLength: 20 })}/>
                <br/><br/>

                <label htmlFor='last_name'><b>Last Name:</b></label>                        
                <input type='text' id='last_name' className='form-control' {...register('last_name',{ required: true, maxLength: 10 })}/>
                <br/><br/>

                <label htmlFor='bod'><b>Birth Date:</b></label>                          
                <input type='date' id='bod' className='form-control' {...register('bod')}/>
                <br/><br/>

                <label htmlFor='gender'><b>Gender:</b></label>                          
                <select id='gender' {...register('gender')}>
                    <option value='Male'>Male</option>
                    <option value='Female'>Female</option>
                    <option value='Other'>Other</option>
                </select>
                <br/><br/>

                <label htmlFor='email'><b>Email:</b></label>                            
                <input type='text' id='email' className='form-control' {...register('email'),{ required: true, maxLength: 10 }}/>
                <br/><br/>

                <label htmlFor='address'><b>Address :</b></label>                      
                <input type='text' id='address' className='form-control' {...register('address'),{ required: true, maxLength: 200 }}/>
                <br/><br/>


                <label htmlFor='city'><b>City:</b></label>                              
                <input type='text' id='city' className='form-control' {...register('city',{ required: true, maxLength: 20 })}/>
                <br/><br/>


                <label htmlFor='state'><b>State:</b></label>                           
                <input type='text' id='state' className='form-control' {...register('state',{ required: true, maxLength: 20 })}/>
                <br/><br/>


                <label htmlFor='country'><b>Country:</b></label>                        
                <input type='text' id='country' className='form-control' {...register('country'{ required: true, maxLength: 20 })}/>
                <br/><br/>


                <label htmlFor='pincode'><b>Pin code:</b></label>                       
                <input type='text' id='pincode' className='form-control' {...register('pincode',{ required: true, maxLength: 10 })}/>
                <br/><br/>


                <label htmlFor='mobile'><b>Mobile:</b></label>                          
                <input type='text' id='mobile' className='form-control' {...register('mobile',{ required: true, maxLength: 10 })}/>
                <br/><br/>


                <label htmlFor='username'><b>Username:</b></label>
                <input type='text' id='username' className='form-control' {...register('username',{ required: true, maxLength: 20 })}/>
                <br/><br/>

                <label htmlFor='password'><b>Password:</b></label>
                <input type='text' id='password' className='form-control' {...register('password',{ required: true, maxLength: 20 })}/>
                <br/><br/>


                <label htmlFor='photo'><b>Photo:</b></label>
                <input type='file' accept=".jpg, .jpeg, .png, .txt, .pdf" id='photo' className='form-control' {...register('photo')}/>
                <br/><br/>


                <label htmlFor='signature'><b>Signature:</b></label>
                <input type='file' accept=".jpg, .jpeg, .png, .txt, .pdf" id='signature' className='form-control' {...register('signature')}/>
                <br/><br/>


                <label htmlFor='role'><b>Role:</b></label>
                <select {...register('role')}>
                    <option value="Customer">Customer</option>
                    <option value="Loan Representative">Loan Representative</option>
                    <option value="Operational Head">Operational Head</option>
                    <option value="Loan Sanction Officer">Loan Sanction Officer</option>
                    

                </select>
                <br/><br/>

                <input type='submit' value='Add User' className='btn btn-outline-success col-6'/>
                <input type='reset' value='RESET' className='btn btn-outline-warning col-6'/>

            </form>

    </div>
    </>
  )
}

export default AddUser;