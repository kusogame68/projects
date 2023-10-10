const tableSelect = document.getElementById('tableSelect');
const customersTable = document.getElementById('customersTable');
const productsTable = document.getElementById('productsTable');
const ordersTable = document.getElementById('ordersTable');

tableSelect.addEventListener('change', function() {
  const selectedTable = tableSelect.value;
  customersTable.style.display = 'none';
  productsTable.style.display = 'none';
  ordersTable.style.display = 'none';

  if (selectedTable === 'customers') {
    customersTable.style.display = 'block';
  } else if (selectedTable === 'products') {
    productsTable.style.display = 'block';
  } else if (selectedTable === 'orders') {
    ordersTable.style.display = 'block';
  }
});