def total_value(queryset, field):
    return sum(queryset.values_list(field, flat=True))
