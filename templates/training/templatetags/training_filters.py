from django import template

register = template.Library()

@register.filter(name='filter_by_module')
def filter_by_module(progress_list, module):
    if not progress_list:
        return None
    for progress in progress_list:
        if progress.module == module:
            return progress
    return None