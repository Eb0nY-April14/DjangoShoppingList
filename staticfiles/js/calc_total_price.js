let price = document.getElementById('id_unit_price');
console.log("The Price is: ", price);
price.addEventListener('change', function(event) {
    let newPrice = parseFloat(price.value);
    console.log("The New Price is: ", newPrice);

    let qty = document.getElementById('id_quantity');
    console.log("The Quantity is: ", qty);

    let newQty = parseInt(qty.value, 10);
    console.log("The New Quantity is: ", newQty);
    
    let total = newQty * newPrice;
    console.log("Total Price is: ", total); 

    document.getElementById("id_total_price").value = total;
    let totalPrice = document.getElementById('id_total_price');
    console.log("The Total Price of your item is:", totalPrice);
});

let qty = document.getElementById('id_quantity');
console.log("The Quantity is: ", qty);
qty.addEventListener('change', function(event) {
    let newQty = parseInt(qty.value, 10);
    console.log("The New Quantity is: ", newQty);

    let price = document.getElementById('id_unit_price');
    console.log("The Price is: ", price);
    
    let newPrice = parseFloat(price.value);
    console.log("The New Price is: ", newPrice);

    let total = newQty * newPrice;
    console.log("Total Price is: ", total);

    document.getElementById("id_total_price").value = total;
    let totalPrice = document.getElementById('id_total_price');
    console.log("The Total Price of your item is:", totalPrice);
});
