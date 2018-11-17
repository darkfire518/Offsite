original_String = input()
if original_String.count('h') < 3:
    print(original_String)
else:
    first_h_Index = original_String.index('h') + 1
    last_h_Index = original_String.rfind('h')
    prefix_String = original_String[:first_h_Index]
    middle_String = original_String[first_h_Index:last_h_Index]
    suffix_String = original_String[last_h_Index:]
    upperCase_MiddleString = middle_String.replace('h','H')
    new_String = prefix_String + upperCase_MiddleString + suffix_String
    print(new_String)