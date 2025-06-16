db.restaurants.insertMany([
    {
        'address': {
            'building': '1007',
            'coord': [ -73.856077, 40.848447 ],
            'street': 'Morris Park Ave',
            'zipcode': '10462'
        },
        'borough': 'Bronx',
        'cuisine': 'Bakery',
        'grades': [
            { 'date': { '$date': 1393804800000 }, 'grade': 'A', 'score': 2 },
            { 'date': { '$date': 1378857600000 }, 'grade': 'A', 'score': 6 },
            { 'date': { '$date': 1358985600000 }, 'grade': 'A', 'score': 10 },
            { 'date': { '$date': 1322006400000 }, 'grade': 'A', 'score': 9 },
            { 'date': { '$date': 1299715200000 }, 'grade': 'B', 'score': 14 }
        ],
        'name': 'Morris Park Bake Shop',
        'restaurant_id': '30075445'
    },
    {
        'address': {
            'building': '138',
            'coord': [ -74.0002413, 40.7191137 ],
            'street': 'Lafayette St',
            'zipcode': '10013'
        },
        'borough': 'Lower Manhattan',
        'cuisine': 'French',
        'grades': [
             { 'date': { '$date': 1393804800000 }, 'grade': 'A', 'score': 2 },
            { 'date': { '$date': 1378857600000 }, 'grade': 'A', 'score': 6 },
            { 'date': { '$date': 1358985600000 }, 'grade': 'A', 'score': 10 },
            { 'date': { '$date': 1322006400000 }, 'grade': 'A', 'score': 9 },
            { 'date': { '$date': 1299715200000 }, 'grade': 'B', 'score': 14 }
        ],
        'name': 'Le Couocou',
        'restaurant_id': '30075391'
    }
 
])

db.restaurants.find(
    {}, { 
        'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1, '_id': 0
    }
)