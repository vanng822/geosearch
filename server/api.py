# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request, abort
from flask.ext.cors import cross_origin

from search import Engine, TagFilter, sort_by_popularity
from form_schema import SearchForm
api = Blueprint('api', __name__)

searcher = None


def create_searcher(index_name):
    global searcher
    searcher = Engine(index_name)


@api.route('/search', methods=['GET'])
@cross_origin()
def search():

    form = SearchForm(request.args)
    if not form.validate():
        abort(400)

    if form.tags.data:
        filts = (TagFilter(form.tags.data),)
    else:
        filts = tuple()

    try:
        res = searcher.find(form.lng.data,
                            form.lat.data,
                            form.radius.data,
                            filters=filts,
                            count=form.count.data,
                            sort_func=sort_by_popularity)
    except Exception as exc:
        print 'exc', exc
        res = []

    return jsonify({'products': [p.to_dict() for p in res]})
