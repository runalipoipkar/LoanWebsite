import axios from 'axios';


//To add User file

export const addFile=(data)=>{
    return axios.post(`http://127.0.0.1:8000/admin_app/user/`,data,{headers:{'content-type':'multipart/form-data'}});
}

export const showUser=(data)=>{
    return axios.get(`http://localhost:8000/admin_app/user/`);
}

{/* Vendor link */}
export const addVendorFile = (data) => {
    // console.log('submitted data----->', data)
    // data.file = data.file[0];
    return axios.post(`http://127.0.0.1:8000/dis/vendor/`,data, {headers:{'content-type':'multipart/form-data'}});

}
//for show vendor
export const showvendor = (data) => {
    return axios.get(`http://127.0.0.1:8000/dis/vendor/`);
}

//for update vendor
export const fetechvendor = (userId) =>{
    return axios.get(`http://127.0.0.1:8000/dis/vendor/${userId}/`, {headers:{'content-type':'multipart/form-data'}});
    
}

export const putVendorData = (userId, data) =>{
    return axios.put(`http://127.0.0.1:8000/dis/vendor/${userId}/`,data,{headers:{'content-type':'multipart/form-data'}});
    
}