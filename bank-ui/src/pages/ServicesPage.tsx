import { useState } from 'react'
import { fetchCustomers, createCustomer, type Customer } from '../services/customerService'

const ServicesPage = () => {
    const [customers, setCustomers] = useState<Customer[]>([])
    const [error, setError] = useState('')
    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [branchId, setBranchId] = useState('')

    const handleLoadCustomers = async () => {
        setError('')
        try {
            const data = await fetchCustomers()
            setCustomers(data)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Unknown error')
        }
    }

    const handleAddCustomer = async () => {
        setError('')
        try {
            await createCustomer(name, email, branchId)
            setName('')
            setEmail('')
            setBranchId('')
        } catch (err) {
            setError(err instanceof Error ? err.message : "Unknown error")
        }
    }

    return (
        <div style={{ padding: '20px' }}>
            <h1>Customers</h1>
            <input
                placeholder="Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
            <input
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <input
                placeholder="Branch ID"
                value={branchId}
                onChange={(e) => setBranchId(e.target.value)}
            />
            <button onClick={handleAddCustomer}>Add Customer</button>
            <button onClick={handleLoadCustomers}>Load Customers</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <ul>
                {customers.map((c) => (
                    <li key={c.id}>{c.name} - {c.email} - {c.branch_id}</li>
                ))}
            </ul>
        </div>
        
    )
}

export default ServicesPage