import random
import pprint


pp = pprint.PrettyPrinter(indent=1, width=110)


def create_grid(grid_size):
    grid = []
    for i in range(1, grid_size+1):
        grid.append([random.randrange(1, 10) for i in range(i, grid_size + i)])
        # grid.append([i for i in range(i, grid_size + i)])
    return grid


def find_greatest(totals):
    greatest = totals[0]  # first element in first list --> compared to the rest of the elements
    for dict in totals:
        if list(dict.keys())[0] > list(greatest.keys())[0]:
            greatest = dict
    return greatest


def get_single_result(short):
    product = short[0]
    for i, el in enumerate(short):
        if i != 0:
            product *= el
    return product


def horizontal_rows(grid, multipliers):
    totals = []
    for i, row in enumerate(grid):
        shorts_list = []
        for j, el in enumerate(row):
            if j <= len(row) - multipliers:
                shorts_list.append({get_single_result(row[j:j+multipliers]): row[j:j+multipliers]})
        totals.extend(shorts_list)

    return find_greatest(totals)


def vertical_rows(grid, multipliers):
    totals = []
    for i, el in enumerate(grid):
        if i <= len(grid) - multipliers:
            shorts_list = []
            for j in range(len(grid)):
                short = []
                for row in grid[i:i+multipliers]:
                    short.append(row[j])
                shorts_list.append({get_single_result(short): short})
            totals.extend(shorts_list)

    return find_greatest(totals)


def diagonal_down(grid, multipliers):
    totals = []
    size = len(grid)
    for row_i in range(size - (multipliers - 1)):
            shorts_list = []
            for col_i in range(size - (multipliers-1)):
                shorts = []
                for i in range(multipliers):
                    shorts.append(grid[row_i + i][col_i + i])
                shorts_list.append({get_single_result(shorts): shorts})
            totals.extend(shorts_list)

    return find_greatest(totals)


def diagonal_up(grid, multipliers):
    totals = []
    size = len(grid)
    for row_i in range(size - 1, size - (size - multipliers) - 1, - 1):
            shorts_list = []
            for col_i in range(size - (multipliers-1)):
                shorts = []
                for i in range(multipliers):
                    shorts.append(grid[row_i - i][col_i + i])
                shorts_list.append({get_single_result(shorts): shorts})
            totals.extend(shorts_list)

    return find_greatest(totals)


def find_greatest_result(grid_size, multipliers):
    grid = create_grid(grid_size)
    pp.pprint(grid)
    greatest_list = [
        horizontal_rows(grid, multipliers),
        vertical_rows(grid, multipliers),
        diagonal_down(grid, multipliers),
        diagonal_up(grid, multipliers)
    ]
    greatest = greatest_list[0]

    for item in greatest_list:
        if list(item.keys())[0] > list(greatest.keys())[0]:
            greatest = item

    print('The greatest product is: {}'.format(greatest))
    num_len = len(str(list(greatest.keys())[0]))
    print('The length of the result is: {}'.format(num_len))


find_greatest_result(20, 5)
