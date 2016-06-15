from collections import OrderedDict

def calculate_age(age):
    age_fields = OrderedDict([
        ("year", age.years),
        ("month", age.months),
        ("day", age.days),
        ("hour", age.hours),
        ("minute", age.minutes)
    ])

    first = None
    second = None

    for f in age_fields.keys():
        if age_fields[f]:
            plural = f + "" if age_fields[f] == 1 else f + "s"
            if not first:
                first = "{0} {1}".format(age_fields[f], plural)
            else:
                second = "{0} {1}".format(age_fields[f], plural)
                break

    if first and second:
        return "{0}, {1}".format(first, second)
    elif first:
        return "{0}".format(first)
    else:
        return "recently"
