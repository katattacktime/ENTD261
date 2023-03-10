//var json = require('./shopItems.json');
/*{
        {
            "itemName": "Mint Tea",
            "SKU": "001",
            "price": "10.00",
            "type": "Loose Leaf Tea",
            "size": "4 oz."
        },
        {
            "itemName": "Chamomile Tea",
            "SKU": "002",
            "price": "10.00",
            "type": "Loose Leaf Tea",
            "size": "4 oz."
        },
        {
            "itemName": "Earl Gray Tea",
            "SKU": "003",
            "price": "10.00",
            "type": "Loose Leaf Tea",
            "size": "4 oz."
        },
        {
            "itemName": "Ginger Honey Tea",
            "SKU": "004",
            "price": "10.00",
            "type": "Loose Leaf Tea",
            "size": "4 oz."
        },
        {
            "itemName": "Measuring Spoon",
            "SKU": "005",
            "price": "5.00",
            "type": "Tea Accessory",
            "size": "1 tsp."
        }
};
*/
$.getJSON(path.join(_dirname, 'shopItems.json'), function (data) {
    var html = '';
    $.each(data, function (key, value) {
        html += '<div id="itemBox" class="col-md-10">'
        html += '<label>"+value.itemName+"</label>'
    });
});