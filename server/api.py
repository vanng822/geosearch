# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, jsonify, request
from flask.ext.cors import cross_origin

from search import Engine, TagFilter, sort_by_popularity

api = Blueprint('api', __name__)

searcher = None


def create_searcher(index_name):
    global searcher
    searcher = Engine(index_name)


@api.route('/search', methods=['GET'])
@cross_origin()
def search():
    # TODO: use some form binding for validation
    lng = float(request.args.get('lng'))
    lat = float(request.args.get('lat'))
    radius = float(request.args.get('radius'))
    count = int(request.args.get('count', 10))
    tags = request.args.getlist('tags[]')
    # print lng, lat, tags, radius

    if tags:
        filts = (TagFilter(tags),)
    else:
        filts = tuple()

    try:
        res = searcher.find(lng,
                            lat,
                            radius,
                            filters=filts,
                            count=count,
                            sort_func=sort_by_popularity)
    except Exception as exc:
        print 'exc', exc
        res = []

    return jsonify({'products': [p.to_dict() for p in res]})
