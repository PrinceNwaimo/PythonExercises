def cel_to_fahr(celsius_value ):
    #doctest using docstring in  python just like TDD in java
 #   """
 #  :param celsius_value: float
 #   :return: float
 #   >>> cel_to_fahr(16)
 #  60.8
 #   >>> cel_to_fahr(23)
  #  73.4
   # """

    fahr = celsius_value * 1.8 + 32.0
    return fahr


celsius_value = 16
print(cel_to_fahr(celsius_value))

