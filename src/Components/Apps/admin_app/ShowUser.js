import React, { useState } from 'react';
import { useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import { showUser } from '../APIServices/APIservices';

function UserShow() {
    const [users,setUsers]=useState([]);
    
    
    async function FetchAllUser(){
       const result= await showUser()
       console.log('result',result.data);
       setUsers(result.data);

    }

    useEffect(() => {
      FetchAllUser();
    }, [])
    
  
  
    return (
    <>
    <table className='table table-dark'>
        <thead>
            <tr>
                
                <th>First Name</th>
                <th>Last Name</th>
                <th>birth date</th>
                <th>Gender</th>
                <th>Email</th>
                <th>Address</th>
                <th>City</th>
                <th>State</th>
                <th>Country</th>
                <th>Pin Code</th>
                <th>Mobile</th>
                <th>Photo</th>
                <th>Signature</th>
                <th>Role</th>
                <th>Action</th>

            </tr>
        </thead>
        <tbody>
        {
            users.map(obj=>{
                return(
                    <tr>
                        <td>{obj.first_name}</td>
                        <td>{obj.last_name}</td>
                        <td>{obj.bod}</td>
                        <td>{obj.gender}</td>
                        <td>{obj.email}</td>
                        <td>{obj.address}</td>
                        <td>{obj.city}</td>
                        <td>{obj.state}</td>
                        <td>{obj.country}</td>
                        <td>{obj.pincode}</td>
                        <td>{obj.mobile}</td>
                        <td>{obj.photo}</td>
                        <td>{obj.signature}</td>
                        <td>{obj.role}</td>
                        <td>
                            <NavLink to={`/update/${obj.id}`}><button className='btn btn-outline-warning'>Update</button></NavLink>
                            <NavLink to={`/delete/${obj.id}`}><button className='btn btn-outline-danger ms-3'>Delete</button></NavLink>
                        </td>
                    </tr>
                )
            })
        }
        </tbody>
    </table>
    
    </>
  )
}

export default UserShow;