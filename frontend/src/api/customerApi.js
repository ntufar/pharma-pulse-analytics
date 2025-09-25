const API_BASE_URL = "http://localhost:8000/api"; // Assuming backend runs on port 8000

export const getAllCustomers = async () => {
    try {
        const response = await fetch(`${API_BASE_URL}/customers`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Error fetching customers:", error);
        return [];
    }
};

export const getCustomerById = async (id) => {
    try {
        const response = await fetch(`${API_BASE_URL}/customers/${id}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Error fetching customer with id ${id}:`, error);
        return null;
    }
};

export const createCustomer = async (customerData) => {
    try {
        const response = await fetch(`${API_BASE_URL}/customers`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(customerData),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Error creating customer:", error);
        return null;
    }
};

export const updateCustomer = async (id, customerData) => {
    try {
        const response = await fetch(`${API_BASE_URL}/customers/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(customerData),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Error updating customer with id ${id}:`, error);
        return null;
    }
};

export const deleteCustomer = async (id) => {
    try {
        const response = await fetch(`${API_BASE_URL}/customers/${id}`, {
            method: "DELETE",
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Error deleting customer with id ${id}:`, error);
        return null;
    }
};
