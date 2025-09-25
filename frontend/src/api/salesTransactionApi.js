const API_BASE_URL = "http://localhost:8000/api"; // Assuming backend runs on port 8000

export const getAllSalesTransactions = async () => {
    try {
        const response = await fetch(`${API_BASE_URL}/sales-transactions`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Error fetching sales transactions:", error);
        return [];
    }
};

export const getSalesTransactionById = async (id) => {
    try {
        const response = await fetch(`${API_BASE_URL}/sales-transactions/${id}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Error fetching sales transaction with id ${id}:`, error);
        return null;
    }
};

export const createSalesTransaction = async (salesTransactionData) => {
    try {
        const response = await fetch(`${API_BASE_URL}/sales-transactions`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(salesTransactionData),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Error creating sales transaction:", error);
        return null;
    }
};

export const updateSalesTransaction = async (id, salesTransactionData) => {
    try {
        const response = await fetch(`${API_BASE_URL}/sales-transactions/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(salesTransactionData),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Error updating sales transaction with id ${id}:`, error);
        return null;
    }
};

export const deleteSalesTransaction = async (id) => {
    try {
        const response = await fetch(`${API_BASE_URL}/sales-transactions/${id}`, {
            method: "DELETE",
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Error deleting sales transaction with id ${id}:`, error);
        return null;
    }
};
