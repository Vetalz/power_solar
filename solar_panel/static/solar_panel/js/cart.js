function qty_up(id) {
    let input_qty = document.getElementById(id);
    let prev_value = parseInt(input_qty.value);
    let max_value = parseInt(input_qty.max)

    if (max_value > prev_value) {
        input_qty.setAttribute('value', ++prev_value);
    }
}

function qty_down(id) {
    let input_qty = document.getElementById(id);
    let prev_value = parseInt(input_qty.value);
    let min_value = parseInt(input_qty.min)

    if (min_value < prev_value) {
        input_qty.setAttribute('value', --prev_value);
    }
}

function add_cart(id_product, id_category) {
    let id = id_product.slice('_')[0]
    let id_name = id + '_name_'+ id_category;
    let id_url = id + '_url_' + id_category;
    let id_image = id + '_image_' + id_category;
    let id_qty = id + '_qty_' + id_category;
    let id_price = id + '_price_' + id_category;

    let name = document.getElementById(id_name).textContent;
    name = name.replace(/\s/g,'')
    let url = document.getElementById(id_url).href;
    let image = document.getElementById(id_image).src;
    let qty = document.getElementById(id_qty).value;
    let price = document.getElementById(id_price).textContent;

    let equipment = {
        id_equipment: Number(id),
        id_category: id_category,
        name: name,
        url: url,
        image: image,
        qty: Number(qty),
        price: Number(price)
    }
    add_local_storage(equipment)

}

function add_local_storage(equipment){
    let n = 0;
    equipment.id = n;
    let all_equipments = [];
    if (localStorage.getItem('equipments')) {
        all_equipments = JSON.parse(localStorage.getItem('equipments'));
        n = all_equipments.length + n;
        equipment.id = n;
    }
    if(all_equipments.length !== 0) {
        let flag = true
        for (let i in all_equipments) {
            if (isEqual(all_equipments[i], equipment)) {
                all_equipments[i].qty = Number(all_equipments[i].qty) + Number(equipment.qty)
                flag = false
                break
            }
        }
        if(flag){
            all_equipments.push(equipment);
        }
    }
    else{
        all_equipments.push(equipment);
    }
    localStorage.setItem('equipments', JSON.stringify(all_equipments));
    update_cart_badge(all_equipments.length)
}

function isEqual(object1, object2){
    return object1.id_category === object2.id_category && object1.id_equipment === object2.id_equipment;
}

function update_cart_badge(qty){
    let span_cart = document.getElementById('cart')
    span_cart.innerHTML = String(qty)
}

document.addEventListener("DOMContentLoaded", (event)=>{
    let all_equipments = JSON.parse(localStorage.getItem('equipments'));
    if (all_equipments){
        let cart_qty = all_equipments.length
        let span_cart = document.getElementById('cart')
        span_cart.innerHTML = cart_qty
    }
})

let cart_equipment = document.getElementById('cart_equipment')

if(cart_equipment){
    let all_equipment = JSON.parse(localStorage.getItem('equipments'));
    if(all_equipment.length !== 0){
        let empty_cart = document.getElementsByClassName('empty')
        empty_cart = Array.from(empty_cart)
        for (let item in empty_cart){
            empty_cart[item].classList.toggle('hidden')
        }

        for (let i in all_equipment) {
            render(all_equipment[i])
        }
    }
}

function render(equipment) {
    let equipment_item = '';
    let total_price_equipment = equipment.qty * equipment.price;
    equipment_item = `<div class="row cart-item" id="${equipment.id}">
                        <div class="col-md-2 d-flex align-items-center justify-content-center mt-1 mb-1">
                            <div class="img-cart">
                                <img src="${equipment.image}" alt="${equipment.name}" class="cart-image">
                            </div>
                       </div>
                       <div class="col-md-3 d-flex align-items-center justify-content-center">
                           <h3><a href="${equipment.url}" class="equipment-link">${equipment.name}</a></h3>
                       </div>
                       <div class="col-md-2 d-flex flex-column justify-content-end">
                           
                       </div>
                       <div class="col-md-2 d-flex align-items-center justify-content-center mt-1 mb-1">
                           <div class="amount-item d-flex">
                               <button class="btn btn-warning plus-minus" value="-" onClick="qty_down_cart('${equipment.id}_qty')">-</button>
                               <input type="number" class="form-control ms-3 qty" min="1" max="999" value="${equipment.qty}" id="${equipment.id}_qty">
                               <button class="btn btn-warning plus-minus" value="+" onClick="qty_up_cart('${equipment.id}_qty')">+</button>
                           </div>
                       </div>
                       <div class="col-md-2 d-flex align-items-center justify-content-center mt-1 mb-1">
                           <p class="price cart-price"><span id="${equipment.id}_price">${total_price_equipment}</span> грн</p>
                       </div>
                       <div class="col-md-1 d-flex align-items-center justify-content-center mt-2 mb-2">
                            <button type="button" class="btn-close" aria-label="Delete" onClick="del_product(${equipment.id})"></button>
                       </div>
                   </div>`;
    cart_equipment.innerHTML += equipment_item;
    update_total_price(total_price_equipment)
}

function update_total_price(price){
    let span_total = document.getElementById('total');
    let total = Number(span_total.innerText);
    span_total.innerText = total + price;
}

function qty_up_cart(input_id) {
    let operation = 'add';
    let input_qty = document.getElementById(input_id);
    let prev_value = parseInt(input_qty.value);
    let max_value = parseInt(input_qty.max);
    let new_value;
    let id = input_id.slice('_')[0];

    if (max_value > prev_value) {
        new_value = ++prev_value
        input_qty.setAttribute('value', new_value);
        change_total_product_price(id, new_value, operation);
    }

    update_product(id, new_value);
}

function qty_down_cart(input_id) {
    let operation = 'take';
    let input_qty = document.getElementById(input_id);
    let prev_value = parseInt(input_qty.value);
    let min_value = parseInt(input_qty.min);
    let new_value;
    let id = input_id.slice('_')[0];

    if (min_value < prev_value) {
        new_value = --prev_value
        input_qty.setAttribute('value', new_value);
        change_total_product_price(id, new_value, operation);
    }
    else{
            new_value = 1
        }

    update_product(id, new_value);
}

function change_total_product_price(product_id, qty, operation){
    let span_price = document.getElementById(`${product_id}_price`)
    let all_products = JSON.parse(localStorage.getItem('equipments'));
    let price;
    let total_price;
    for (let i in all_products){
        if(all_products[i].id === Number(product_id)) {
            price = Number(all_products[i].price)
        }
    }
    total_price = price * qty;
    span_price.innerText = total_price;
    if(operation === 'add'){
        update_total_price(price);
    }
    else {
        update_total_price(-price);
    }
}

function update_product(product_id, qty){
    let all_products = JSON.parse(localStorage.getItem('equipments'));
    let new_all_products = [];
    for (let item in all_products) {
        if (parseInt(all_products[item].id) === parseInt(product_id)){
            let product = {
                id_equipment: all_products[item].id_equipment,
                qty: qty,
                id_category: all_products[item].id_category,
                name: all_products[item].name,
                url: all_products[item].url,
                image: all_products[item].image,
                price: all_products[item].price,
                id: all_products[item].id
            };
            new_all_products.push(product);
        }
        else{
            let product = {
                id_equipment: all_products[item].id_equipment,
                qty: all_products[item].qty,
                id_category: all_products[item].id_category,
                name: all_products[item].name,
                url: all_products[item].url,
                image: all_products[item].image,
                price: all_products[item].price,
                id: all_products[item].id
            };
            new_all_products.push(product);
        }
    }
    localStorage.setItem('equipments', JSON.stringify(new_all_products));
}

function del_product(product_id) {
    let span_product_price = document.getElementById(`${product_id}_price`);
    let product_price = Number(span_product_price.innerText);
    update_total_price(-product_price);

    document.getElementById(product_id).remove();
    let all_products = JSON.parse(localStorage.getItem('equipments'));
    let new_all_products = [];
    for (let item in all_products) {
        if (parseInt(all_products[item].id) !== product_id){
            let product = {
                id_equipment: all_products[item].id_equipment,
                qty: all_products[item].qty,
                id_category: all_products[item].id_category,
                name: all_products[item].name,
                url: all_products[item].url,
                image: all_products[item].image,
                price: all_products[item].price,
                id: all_products[item].id
            };
            new_all_products.push(product);
        }
    }

    check_items(new_all_products);
    localStorage.setItem('equipments', JSON.stringify(new_all_products));
}

function check_items(products) {
    if(products.length === 0){
        let empty_cart = document.getElementsByClassName('empty')
        empty_cart = Array.from(empty_cart)
        for (let item in empty_cart){
            empty_cart[item].classList.toggle('hidden')
        }
    }
}