from django import template

register = template.Library()


@register.simple_tag()
def denormalize_measurement(unit, value):
    # print(unit, value)

    if unit == 'ft':
        return round(
            (round(float(value), 2) * 3.28 / 100),
            2
        )
    else:
        return round(
            (float(value) / 100),
            2
        )
