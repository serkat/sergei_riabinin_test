def satisfied_input(start, end):
    """
        check if end point is greater or equal than start point
    :param start: start point of segment
    :param end: end point of segment
    :return: True or print error
    """
    if start.isdigit() and end.isdigit():
        if end < start:
            return print('\nEnd point must be greater than {}'.format(start))
        else:
            return True
    else:
        print('\nMust be integers and not empty')


def segments_overlap():
    """
        Task:
        Write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis
        and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

        My answer:
        def segments_intersect(x1, x2, y1, y2):
            return x2 >= y1 and y2 >= x1 and x2 >= x1 and y2 >= y1


        Returning result of interval comparison
        Testcases:
        [
            ((2, 5), (3, 7))
            , ((3, 7), (2, 5))
            , ((5, 2), (7, 3))
            , ((7, 3), (5, 2))

            , ((2, 5), (6, 7))
            , ((6, 7), (2, 5))
            , ((5, 2), (7, 6))
            , ((7, 6), (5, 2))

            , ((5, 5), (6, 8))
            , ((6, 8), (5, 5))
            , ((5, 5), (8, 6))
            , ((8, 6), (5, 5))

            , ((7, 7), (6, 8))
            , ((6, 8), (7, 7))
            , ((7, 7), (8, 6))
            , ((8, 6), (7, 7))

            , ((-3, 1), (1, 5))
            , ((1, 5), (-3, 1))
            , ((1, -3), (5, 1))
            , ((5, 1), (1, -3))

            , ((-1, -6), (5, -3))
            , ((5, -3), (-1, -6))
            , ((-6, -1), (-3, 5))
            , ((-3, 5), (-6, -1))

            , ((4, 4), (5, 5))
            , ((4, 4), (4, 4))
            , ((0, 0), (0, 0))
            , ((5, 7), (2, 9))

        ]
    :return: true or false
    """
    # enter start and end points of first segment
    start_point_of_a = input("Enter start point of A segment: ")
    end_point_of_a = input("Enter end point of A segment: ")

    if satisfied_input(start_point_of_a, end_point_of_a):

        # enter start and end points of second segment
        start_point_of_b = input("Enter start point of B segment: ")
        end_point_of_b = input("Enter end point of B segment: ")

        if satisfied_input(start_point_of_b, end_point_of_b):
            # segments overlaps if (A2 >= B1) and (B2 >= A1)
            result = end_point_of_a >= start_point_of_b and end_point_of_b >= start_point_of_a
            print('\n{} and {} are overlapping - {}'.format((start_point_of_a, end_point_of_a), (start_point_of_b, end_point_of_b), result))

segments_overlap()
