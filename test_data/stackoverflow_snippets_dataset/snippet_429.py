# Extracted from https://stackoverflow.com/questions/6130768/return-a-default-value-if-a-dictionary-key-is-not-available
my_dict = {'level_1': {
             'level_2': {
                  'level_3': 'more_data'
                  }
              }
           }
result = my_dict.get('level_1', {}).get('level_2', {}).get('level_3')
# result -> 'more_data'
none_result = my_dict.get('level_1', {}).get('what_level', {}).get('level_3')
# none_result -> None

