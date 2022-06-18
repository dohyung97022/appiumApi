def snake_case_to_camel_case(snake_case: str) -> str:
    components = snake_case.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
