export type Customer = {
    id: string
    name: string
    email: string
    branch_id: string
}

const API_URL = 'http://127.0.0.1:8000/api/v1/customers'

export const fetchCustomers = async (): Promise<Customer[]> => {
    const response = await fetch(API_URL)
    if (!response.ok) {
        throw new Error(`Failed to fetch customers (${response.status})`)
    }
    return response.json()
}

export const createCustomer = async (name: string, email: string, branchId: string): Promise<Customer> => {
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name, email: email, branch_id: branchId })
    })
    if (!response.ok) {
        throw new Error(`Failed to create customer (${response.status})`)
    }
    return response.json()
}

export const fetchCustomerById = async (customerId: string): Promise<Customer> => {
    const response = await fetch(`${API_URL}/${customerId}`)
    if (!response.ok) {
        throw new Error(`Failed to find customer (${response.status})`)
    }
    return response.json()
}

export const deleteCustomer = async (customerId: string): Promise<void> => {
    const response = await fetch(`${API_URL}/${customerId}`, {
        method: 'DELETE',
    })
    if (!response.ok) {
        throw new Error(`Failed to find customer (${response.status})`)
    }
}