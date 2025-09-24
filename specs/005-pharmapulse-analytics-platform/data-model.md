# Data Model: PharmaPulse Analytics Platform

## Core Data Entities

### Sales Transactions
- **Transaction ID**: Unique identifier for each sales transaction (Primary Key)
- **Date**: Date of the transaction
- **Amount**: Total amount of the transaction
- **Product**: Product involved in the transaction (Foreign Key to Product Master)
- **Territory**: Sales territory where the transaction occurred (Foreign Key to Territory & Geography)
- **Sales Rep**: Sales representative responsible for the transaction
- **Customer**: Customer involved in the transaction (Foreign Key to Customer & Accounts)
- **Channel**: Sales channel (e.g., online, retail)
- **Promotional Code**: Code used for any promotions
- **Quantity**: Quantity of product sold
- **Unit Price**: Price per unit of the product
- **Discount**: Discount applied to the transaction
- **Commission**: Commission earned on the transaction

### Product Master
- **Product ID**: Unique identifier for each product (Primary Key)
- **Name**: Name of the product
- **Category**: Product category
- **Therapeutic Area**: Therapeutic area the product belongs to
- **Launch Date**: Date the product was launched
- **Status**: Current status of the product (e.g., active, discontinued)
- **Pricing**: Pricing information for the product
- **Manufacturer**: Manufacturer of the product
- **Regulatory Information**: Relevant regulatory details
- **Indication**: Medical indication for the product

### Territory & Geography
- **Territory ID**: Unique identifier for each territory (Primary Key)
- **Name**: Name of the territory
- **Region**: Region the territory belongs to
- **Country**: Country the territory is in
- **Population Demographics**: Demographic information of the territory's population
- **Market Size**: Estimated market size of the territory
- **Assigned Sales Representatives**: List of sales representatives assigned to the territory

### Customer & Accounts
- **Customer ID**: Unique identifier for each customer (Primary Key)
- **Name**: Name of the customer
- **Type**: Type of customer (e.g., hospital, pharmacy, individual)
- **Specialty**: Medical specialty of the customer (if applicable)
- **Address**: Customer's address
- **Contact Information**: Contact details (e.g., phone, email)
- **Tier**: Customer tier (e.g., gold, silver, bronze)
- **Prescribing History**: History of prescriptions (if applicable)
- **Preferences**: Customer preferences

## Analytical Data Marts

### Sales Performance Mart
- Aggregated sales by various dimensions
- Year-over-year comparisons
- Target vs. actual performance
- Ranking and percentile calculations

### Market Intelligence Mart
- Competitive analysis data
- Market share calculations
- Trend analysis and forecasting
- External market research integration
