/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use./

db

use('warehouse_management');

db.sectors.find().pretty();

// Insert a few documents into the sales collection.
// db.sectors.insertMany([
//     {
//         _id: ObjectId("65cba1a123456789abcd0001"),
//         name: "Sector 1",
//         creator: ObjectId("65cb123456789abcd000a001"),
//         location: "New York",
//         deleted: false
//     },
//     {
//         _id: ObjectId("65cba1a123456789abcd0002"),
//         name: "Sector 2",
//         creator: ObjectId("65cb123456789abcd000a002"),
//         location: "Los Angeles",
//         deleted: false
//     },
//     {
//         "_id": ObjectId("65cba1a123456789abcd0003"),
//         "name": "Sector 3",
//         "creator": ObjectId("65cb123456789abcd000a001"),
//         "location": "Chicago",
//         "deleted": false
//         },
//         {
//         "_id": ObjectId("65cba1a123456789abcd0004"),
//         "name": "Sector 4",
//         "creator": ObjectId("65cb123456789abcd000a002"),
//         "location": "Houston",
//         "deleted": false
//         },
//         {
//         "_id": ObjectId("65cba1a123456789abcd0005"),
//         "name": "Sector 5",
//         "creator": ObjectId("65cb123456789abcd000a001"),
//         "location": "San Francisco",
//         "deleted": false
//         }
// ])

// db.warehouses.insertMany([
//     {
//         "_id": ObjectId("65cbc1a123456789abcd1001"),
//         "columns": [
//         {"title": "Day", "dataIndex": "day", "dataType": "date"},
//         {"title": "Electronics", "dataIndex": "0", "dataType": "number"},
//         {"title": "Furniture", "dataIndex": "1", "dataType": "number"}
//         ],
//         "name": "Warehouse 1",
//         "creator": ObjectId("65cb123456789abcd000a001"),
//         "sector": ObjectId("65cba1a123456789abcd0001")
//         },
//         {
//         "_id": ObjectId("65cbc1a123456789abcd1002"),
        
//         "columns": [
//         {"title": "Day", "dataIndex": "day", "dataType": "date"},
//         {"title": "Raw Materials", "dataIndex": "0", "dataType": "number"},
//         {"title": "Packaging Supplies", "dataIndex": "1", "dataType": "number"},
//         {"title": "Chemicals", "dataIndex": "2", "dataType": "number"},
//         {"title": "Safety Gear", "dataIndex": "3", "dataType": "number"}
//         ],
//         "name": "Warehouse 1",
//         "creator": ObjectId("65cb123456789abcd000a001"),
//         "sector": ObjectId("65cba1a123456789abcd0003")
//         },
//         {
//         "_id": ObjectId("65cbc1a123456789abcd1003"),
//         "columns": [
//         {"title": "Day", "dataIndex": "day", "dataType": "date"},
//         {"title": "Clothing", "dataIndex": "0", "dataType": "number"},
//         {"title": "Shoes", "dataIndex": "1", "dataType": "number"},
//         {"title": "Accessories", "dataIndex": "2", "dataType": "number"},
//         {"title": "Bags", "dataIndex": "3", "dataType": "number"},
//         {"title": "Jewelry", "dataIndex": "4", "dataType": "number"},
//         {"title": "Watches", "dataIndex": "5", "dataType": "number"},
//         {"title": "Sunglasses", "dataIndex": "6", "dataType": "number"}
//         ],
//         "name": "Warehouse 1",
//         "creator": ObjectId("65cb123456789abcd000a002"),
//         "sector": ObjectId("65cba1a123456789abcd0002")
//         },
//         {
//         "_id": ObjectId("65cbc1a123456789abcd1004"),
//         "columns": [
//         {"title": "Day", "dataIndex": "day", "dataType": "date"},
//         {"title": "Books", "dataIndex": "0", "dataType": "number"},
//         {"title": "Stationery", "dataIndex": "1", "dataType": "number"},
//         {"title": "Notebooks", "dataIndex": "2", "dataType": "number"},
//         {"title": "Pens", "dataIndex": "3", "dataType": "number"}
//         ],
//         "name": "Warehouse 2",
//         "creator": ObjectId("65cb123456789abcd000a002"),
//         "sector": ObjectId("65cba1a123456789abcd0004")
//         },
//         {
//         "_id": ObjectId("65cbc1a123456789abcd1005"),
//         "columns": [
//         {"title": "Day", "dataIndex": "day", "dataType": "date"},
        
//         {"title": "Perishable Goods", "dataIndex": "0", "dataType": "number"},
//         {"title": "Frozen Foods", "dataIndex": "1", "dataType": "number"},
//         {"title": "Beverages", "dataIndex": "2", "dataType": "number"},
//         {"title": "Dairy Products", "dataIndex": "3", "dataType": "number"},
//         {"title": "Snacks", "dataIndex": "4", "dataType": "number"},
//         {"title": "Canned Goods", "dataIndex": "5", "dataType": "number"},
//         {"title": "Spices", "dataIndex": "6", "dataType": "number"}
//         ],
//         "name": "Warehouse 2",
//         "creator": ObjectId("65cb123456789abcd000a001"),
//         "sector": ObjectId("65cba1a123456789abcd0001")
//         }
// ])

// db.logdatas.insertMany([
//     {
//         "_id": ObjectId("65cbc2a123456789abcd2001"),
//         "warehouse": ObjectId("65cbc1a123456789abcd1001"),
//         "creator": ObjectId("65cb123456789abcd000a001"),
//         "logData": {
//         "day": "2024-02-08T12:20:36.785Z",
//         "0": 250,
//         "1": 40
//         }
//         },
//         {
//         "_id": ObjectId("65cbc2a123456789abcd2002"),
//         "warehouse": ObjectId("65cbc1a123456789abcd1002"),
//         "creator": ObjectId("65cb123456789abcd000a001"),
//         "logData": {
//         "day": "2024-02-09T09:15:22.482Z",
//         "0": 1300,
//         "1": 500,
//         "2": 120,
//         "3": 200
//         }
//         },
//         {
//         "_id": ObjectId("65cbc2a123456789abcd2003"),
//         "warehouse": ObjectId("65cbc1a123456789abcd1003"),
//         "creator": ObjectId("65cb123456789abcd000a002"),
//         "logData": {
//         "day": "2024-02-10T17:45:12.129Z",
//         "0": 1200,
        
//         "1": 800,
//         "2": 300,
//         "3": 150,
//         "4": 75,
//         "5": 60,
//         "6": 90
//         }
//         },
//         {
//         "_id": ObjectId("65cbc2a123456789abcd2004"),
//         "warehouse": ObjectId("65cbc1a123456789abcd1004"),
//         "creator": ObjectId("65cb123456789abcd000a002"),
//         "logData": {
//         "day": "2024-02-11T06:30:54.873Z",
//         "0": 500,
//         "1": 300,
//         "2": 200,
//         "3": 100
//         }
//         },
//         {
//         "_id": ObjectId("65cbc2a123456789abcd2005"),
//         "warehouse": ObjectId("65cbc1a123456789abcd1005"),
//         "creator": ObjectId("65cb123456789abcd000a001"),
//         "logData": {
//         "day": "2024-02-12T23:59:59.999Z",
//         "0": 700,
//         "1": 400,
//         "2": 600,
//         "3": 350,
//         "4": 500,
//         "5": 250,
//         "6": 100
//         }
//         }
// ])


// Run a find command to view items sold on April 4th, 2014.
// const salesOnApril4th = db.getCollection('sales').find({
//   date: { $gte: new Date('2014-04-04'), $lt: new Date('2014-04-05') }
// }).count();

// // Print a message to the output window.
// console.log(`${salesOnApril4th} sales occurred in 2014.`);

// // Here we run an aggregation and open a cursor to the results.
// // Use '.toArray()' to exhaust the cursor to return the whole result set.
// // You can use '.hasNext()/.next()' to iterate through the cursor page by page.
// db.getCollection('sales').aggregate([
//   // Find all of the sales that occurred in 2014.
//   { $match: { date: { $gte: new Date('2014-01-01'), $lt: new Date('2015-01-01') } } },
//   // Group the total sales for each product.
//   { $group: { _id: '$item', totalSaleAmount: { $sum: { $multiply: [ '$price', '$quantity' ] } } } }
// ]);
