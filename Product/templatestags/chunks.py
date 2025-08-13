from django import template

register = template.Library()

@register.filter(name='chunk')
def chunks(data_list, chunk_size):
    chunk = []
    i=1
    for item in data_list:
        chunk.append(item)
        i=i+1
        if i == chunk_size:
            yield chunk
            chunk = []
    yield chunk