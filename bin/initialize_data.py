#!/usr/bin/env python

import os

from bot.messages import get_mongo


def add_data(mongo, key, data):
    mongo[key].insert_many(data)

mongo = get_mongo(os.environ.get('MONGOLAB_URI'))

mongo.sentences.delete_many({})
mongo.words.delete_many({})

sentences = [
    {'type': 'adjective', 'sentence': 'You are a shining example of a {0} person.'},
    {'type': 'adjective', 'sentence': 'I really appreciate how {0} you are.'},
    {'type': 'adjective', 'sentence': 'You are an empowering example of a {0} person.'},
    {'type': 'adjective', 'sentence': 'I am so impressed by how {0} you are.'},
    {'type': 'adjective', 'sentence': 'You are an inspiring example of a {0} person.'},
    {'type': 'adjective', 'sentence': 'You are a beautiful example of a {0} person.'},
    {'type': 'noun', 'sentence': 'I am touched by your {0}.'},
    {'type': 'noun', 'sentence': 'I have the deepest respect for your {0}.'},
    {'type': 'noun', 'sentence': 'I greatly admire your {0}.'},
    {'type': 'noun', 'sentence': 'I am truly grateful for your {0}.'},
    {'type': 'noun', 'sentence': 'I deeply value the great {0} you bring to the world.'},
    {'type': 'noun', 'sentence': 'Your {0} is a great inspiration.'},
    {'type': 'noun', 'sentence': 'Your {0} is compelling.'},
    {'type': None,
     'sentence': 'You are such a bright light and I am so glad you are here with me.'},
    {'type': None, 'sentence': 'My world is a better place with you in it.'},
    {'type': None, 'sentence': 'Your contributions bring great value.'},
    {'type': None, 'sentence': 'Your smile brightens my day. :)'},
    {'type': None, 'sentence': 'I keep finding new wonderful things about you!'},
    {'type': None, 'sentence': 'I treasure your unique presence in the world.'},
    {'type': None, 'sentence': 'Just by being alive you add something special to the world.'},
    {'type': None, 'sentence': 'You bring a special glow to all that you do.'}
]
add_data(mongo, 'sentences', sentences)

words = [
    {'type': 'adjective', 'word': 'generous'},
    {'type': 'adjective', 'word': 'smart'},
    {'type': 'adjective', 'word': 'helpful'},
    {'type': 'adjective', 'word': 'kind'},
    {'type': 'adjective', 'word': 'hard-working'},
    {'type': 'adjective', 'word': 'meticulous'},
    {'type': 'adjective', 'word': 'diligent'},
    {'type': 'adjective', 'word': 'courageous'},
    {'type': 'adjective', 'word': 'considerate'},
    {'type': 'adjective', 'word': 'caring'},
    {'type': 'adjective', 'word': 'brilliant'},
    {'type': 'adjective', 'word': 'adventurous'},
    {'type': 'adjective', 'word': 'energetic'},
    {'type': 'adjective', 'word': 'imaginative'},
    {'type': 'adjective', 'word': 'inventive'},
    {'type': 'adjective', 'word': 'thoughtful'},
    {'type': 'adjective', 'word': 'intrepid'},
    {'type': 'adjective', 'word': 'creative'},
    {'type': 'noun', 'word': 'intelligence'},
    {'type': 'noun', 'word': 'fortitude'},
    {'type': 'noun', 'word': 'kindness'},
    {'type': 'noun', 'word': 'diligence'},
    {'type': 'noun', 'word': 'courage'},
    {'type': 'noun', 'word': 'versatility'},
    {'type': 'noun', 'word': 'commitment'},
    {'type': 'noun', 'word': 'brilliance'},
    {'type': 'noun', 'word': 'persistence'},
    {'type': 'noun', 'word': 'imagination'},
    {'type': 'noun', 'word': 'generosity'},
    {'type': 'noun', 'word': 'creativity'},
]
add_data(mongo, 'words', words)
