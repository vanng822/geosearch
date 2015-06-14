
def sort_by_property(prop):
    def _sort_by_property(items):
        return sorted(items,
                      key=lambda item: getattr(item, prop),
                      reverse=True)

    return _sort_by_property

sort_by_popularity = sort_by_property('popularity')
