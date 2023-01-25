def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(),key = lambda kvp:(-len(kvp[1]), kvp[0]))
    result = []

    print(sorted_data)

    for cheese_name, quantity in sorted_data:
        result.append(cheese_name)
        result.extend(sorted(quantity,reverse=True))
    return '\n'.join([str(el) for el  in result])

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
