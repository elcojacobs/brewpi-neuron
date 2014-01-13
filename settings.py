# -*- coding: utf-8 -*-

"""
    brewpi-neuron settings
    ~~~~~~~~~~~~~~~~~~~~~~

    Settings file for our (mock) api

    ** copied from eve-demo:

    PLEASE NOTE: We don't need to create the two collections in MongoDB.
    Actually, we don't even need to create the database: GET requests on an
    empty/non-existant DB will be served correctly ('200' OK with an empty
    collection); DELETE/PATCH will receive appropriate responses ('404' Not
    Found), and POST requests will create database and collections when needed.
    Keep in mind however that such an auto-managed database will most likely
    perform poorly since it lacks any sort of optimized index.

    :copyright: (c) 2014, BrewPi/Elco Jacobs.
    :license: GPLv3, see LICENSE for more details.
"""

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# MONGO_USERNAME = 'user'
# MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'test'

# let's not forget the API entry point
SERVER_NAME = '127.0.0.1:5000'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']


# Our API will expose two resources (MongoDB collections): 'people' and
# 'works'. In order to allow for proper data validation, we define beaviour
# and structure.

# bots are Arduinos, Spark cores, e.g. embedded devices that communicate with the service layer
bots = {
    # by default the standard item entry point is defined as
    # '/bots/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/bots/<name>/'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
        'schema': {
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'required': True,
            # 'name' is an API entry-point, so we need it to be unique.
            'unique': True,
        },
        'devices': {
            'schema': {
                'slot': {
                    'type': 'integer',
                    'min': 0,
                    'max': 15,
                    'required': True
                },
                'device-type': {
                    'type': 'string',
                    'allowed': ['temperature-sensor', 'switch-sensor', 'switch-actuator']
                },
                'hardware-type': {
                    'type': 'string',
                    'allowed': ['pin', 'onewire-temperature', 'onewire-2413' ]
                },
                'function': {
                    'type': 'string',
                    'allowed': ['chamber-door',
                                'chamber-heater',
                                'chamber-cooler',
                                'chamber-light',
                                'chamber-room-temperature',
                                'chamber-temperature',
                                'chamber-fan',
                                'beer-temperature',
                                'beer-heater',
                                'beer-cooler',
                                ]
                },
                'chamber': {
                    'type': 'integer'
                },
                'beer': {
                    'type': 'integer'
                },
                'arduino-pin': {
                    'type': 'integer'
                },
                'onewire-address': {
                    'type': 'string'
                }
            }
        },

        'controllers': {
            'name': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 15,
            },
            'inputs': {

            },
            'outputs': {

            },
            'type':{
                'allowed': ['pid', 'pwm']
            }
        }
    }
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'bots': bots,
}
