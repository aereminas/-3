from typing import List, Union, Any

def process_data(search_type: str, condition: bool, *positional_args: Any, **keyword_args: Any) -> Union[List[int], str]:
    number_list: List[int] = []
    text_string: str = ""

    if search_type == "positional":
        if condition:
            for arg in positional_args:
                if isinstance(arg, int):
                    number_list.append(arg)
            return number_list
        else:
            for arg in positional_args:
                text_string += str(arg)
            return text_string
    elif search_type == "keywords":
        for key, value in keyword_args.items():
            text_string += f"Ключ: {key}, Значение: {value}; "
        return text_string
    else:
        raise ValueError("Некорректный тип поиска")
