import React from 'react'
import { NavLink } from 'react-router-dom';
function Layout() {
  return (
    <>
        <nav className="navbar navbar-expand-lg navbar-dark bg-info">
  <div className="container-fluid">
    <NavLink className="navbar-brand" to="#">Navbar</NavLink>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div className="navbar-nav">
        <NavLink className="nav-link active" aria-current="page" to="#">Home</NavLink>
        <NavLink className="nav-link" to="#">About</NavLink>
        <NavLink className="nav-link" to="#">Contact</NavLink>
        <NavLink className="nav-link" to="/add">Add User</NavLink>
        <NavLink className="nav-link" to="/show">Show User</NavLink>
        <NavLink className="nav-link" to="/gst">GST</NavLink>
        <NavLink className="nav-link" to="/disadd">Add Disbursement</NavLink>
        <NavLink className="nav-link" to="/disshow">Show Disbursement</NavLink>

        <NavLink className="nav-link disabled" to="#" tabindex="-1" aria-disabled="true">Disabled</NavLink>
      </div>
    </div>
  </div>
</nav>
    </>
  );
}

export default Layout;