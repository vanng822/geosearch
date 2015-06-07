# -*- coding: utf-8 -*-

from search.engine import Engine
from models import Shop, Product

import csv
import os


def data_path(filename):
    parent = os.path.dirname(__file__)
    data_path = os.path.join(parent, '..', 'data')
    return u'{}/{}'.format(data_path, filename)


class ProductIndexer(Engine):

    def index(self, products, shops, taggings, tags):
        """ Take datasets and create an index of them

        """
        shops.next()
        shop_dict = {}
        for shop in shops:
            # id,name,lat,lng
            shop_dict[shop[0]] = Shop(
                shop[0], shop[1], float(shop[2]), float(shop[3]))

        # tags
        # id,tag
        tag_dict = {}
        tags.next()
        for tag in tags:
            tag_dict[tag[0]] = tag[1]

        # tagging
        # id,shop_id,tag_id

        taggings.next()
        for tagging in taggings:
            shop_dict[tagging[1]].add_tag(tag_dict[tagging[2]])

        # now index the product
        # id,shop_id,title,popularity,quantity
        products.next()
        for product in products:
            shop = shop_dict[product[1]]
            #id, shop_id, title, popularity, quantity, lng, lat
            self.index_product(
                Product(product[0],
                        product[1],
                        product[2],
                        product[3],
                        product[4],
                        shop.lng,
                        shop.lat,
                        tags=shop.tags))

    def index_product(self, product):
        """ Take a product and insert into the index

        """
        self.idx.insert(int(product.id, 16),
                        (product.lat, product.lng, product.lat, product.lng),
                        obj=product)

    def search_test(self):
        try:
            self.find(18.0649000, 59.3325800, 100, 10)
        except Exception as exc:
            print exc

    def full_index(self):
        products_file = open(data_path('products.csv'))
        shops_file = open(data_path('shops.csv'))
        taggings_file = open(data_path('taggings.csv'))
        tags_file = open(data_path('tags.csv'))
        self.index(csv.reader(products_file),
                   csv.reader(shops_file),
                   csv.reader(taggings_file),
                   csv.reader(tags_file))
        products_file.close()
        shops_file.close()
        taggings_file.close()
        tags_file.close()

        print len(self.search_test())
