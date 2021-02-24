#CodeWars
#Jaden Casing Strings

quote = "How can mirrors be real if our eyes aren't real"

def to_jaden_case(parameter):
    """
    Your task is to convert strings to how they would be written by
    Jaden Smith. The strings are actual quotes from Jaden Smith, but
    they are not capitalized in the same way he originally typed them.
    """
    return " ".join(traveler.capitalize() for traveler in parameter.split())

print(to_jaden_case(quote))

#test.assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
