

def sort_by_popularity(items):
    return sorted(items, key=lambda product: product.popularity, reverse=True)
