#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import json

    string_of_json_data = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
    json_data_as_python_value = json.loads(string_of_json_data)
    print(json_data_as_python_value)

    string_of_json_data = json.dumps(json_data_as_python_value)
    print(string_of_json_data)


if __name__ == '__main__':
    main()
