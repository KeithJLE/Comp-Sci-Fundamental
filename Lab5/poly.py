# CPE 101-01
# LAB 5: Polynomial Functions
# Name: Keith Lee
# Section: 7

# 1) purpose statement: This function takes two polynomials of degree 2 as lists. The values in the list will represent
# the coefficients of the terms and the indices will represent the exponents. The function then returns a new list,
# also representing a polynomial in the same way, that adds the other two lists together.
# signature: list list -> list
def poly_add2(poly1, poly2):
    poly3 = []
    poly3.append(poly1[0] + poly2[0])
    poly3.append(poly1[1] + poly2[1])
    poly3.append(poly1[2] + poly2[2])
    return poly3


# 1) purpose statement: This function takes two polynomials of degree 2 as lists. The values in the list will represent
# the coefficients of the terms and the indices will represent the exponents. The function then returns a new list,
# also representing a polynomial in the same way, that multiplies the other two lists together.
# signature: list list -> list
def poly_mult2(poly1, poly2):
    poly3 = []
    poly3.append(poly1[0] * poly2[0])
    poly3.append(poly1[0] * poly2[1] + poly1[1] * poly2[0])
    poly3.append(poly1[0] * poly2[2] + poly1[1] * poly2[1] + poly1[2] * poly2[0])
    poly3.append(poly1[1] * poly2[2] + poly1[2] * poly2[1])
    poly3.append(poly1[2] * poly2[2])
    return poly3

