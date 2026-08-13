import { NavLink } from 'react-router-dom'

const HeaderComponent = () => {
  const navStyle = ({ isActive }: { isActive: boolean }) => ({
    color: isActive ? '#93c5fd' : 'white',
    textDecoration: 'none',
    marginRight: '20px',
  })

  return (
    <header style={{ background: '#0f172a', padding: '12px 24px' }}>
      <nav style={{ display: 'flex' }}>
        <NavLink to="/" style={navStyle} end>Home</NavLink>
        <NavLink to="/about" style={navStyle}>About</NavLink>
        <NavLink to="/services" style={navStyle}>Services</NavLink>
      </nav>
    </header>
  )
}

export default HeaderComponent