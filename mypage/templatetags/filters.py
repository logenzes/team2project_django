from django import template

register = template.Library()

@register.filter
def get_ranking(dictionary, key):
    results = []

    if dictionary.get(key) != None:
        results = dictionary.get(key)
        # i = 0
        # for item in results:
        #     i += 1
        #     item.ranking = i
        results = results[0:5]

    return results


@register.filter
def get_my_rank(dictionary, key):
    return_value = []
    results = []
    print(dictionary.get(key))
    if len(dictionary.get(key)) > 0:
        results = dictionary.get(key)
        return_value.append(results[0])

    return return_value