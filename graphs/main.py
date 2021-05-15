import math
import matplotlib.pyplot as plt
import datetime
import random
import operator


def generate_counts(n):
    step = math.pi / n
    start = 0
    x_data = [start + i * step for i in range(n)]
    return [str(int(10 + 40 * math.sin(x))) for x in x_data]


def generate_dates(n):
    start = datetime.datetime(2020, 1, 6)
    return [(start + datetime.timedelta(days=i * 30)).strftime('%Y-%m') for i in range(n)]


def generate_resources(n):
    return [str(random.randint(1, 3)) for i in range(n)]


def generate_staff_ids(n):
    return [str(random.randint(20, 25)) for i in range(n)]


def generate_data_and_write(n, file_name):
    dates = generate_dates(n)
    counts = generate_counts(n)
    resources = generate_resources(n)
    staff_ids = generate_staff_ids(n)
    data = [dates[i] + ', ' + resources[i] + ', ' + staff_ids[i] + ', ' + counts[i] + '\n' for i in range(n)]
    data.insert(0, 'date, resource, staff_id, count\n')
    file = open(file_name, 'w')
    for i in data:
        file.write(i)
    file.close()


def read_file(file_name):
    file = open(file_name)
    result = file.readlines()
    file.close()
    return result


def from_str_to_dict(lst):
    lst = list(map(lambda st: st.split(', '), lst))
    lst_dict = []
    list(map(lambda l: lst_dict.append(dict(zip([lst[0][0], lst[0][1], lst[0][2], lst[0][3]], l))), lst))
    lst_dict.pop(0)
    return lst_dict


def show_graph(title, x_lable, y_lable, x_data, y_data):
    plt.plot(x_data, y_data, color='red', marker='o')
    plt.title(title)
    plt.xlabel(x_lable)
    plt.ylabel(y_lable)
    plt.show()


def staff_id_graph(staff_id, lst_dict):
    lst_dict = list(filter(lambda k: k['staff_id'] == str(staff_id), lst_dict))
    lst_dict.sort(key=operator.itemgetter('date'))
    x_data = [lst_dict[i]['date'] for i in range(len(lst_dict))]
    y_data = [int(lst_dict[i]['count\n']) for i in range(len(lst_dict))]
    show_graph(f'Staff_id: {staff_id}', 'Date', 'Count', x_data, y_data)


def resource_graph(resource, lst_dict):
    lst_dict = list(filter(lambda d: d['resource'] == str(resource), lst_dict))
    lst_dict.sort(key=operator.itemgetter('date'))
    x_data = [lst_dict[i]['date'] for i in range(len(lst_dict))]
    y_data = [int(lst_dict[i]['count\n']) for i in range(len(lst_dict))]
    show_graph(f'Resource: {resource}', 'Date', 'Count', x_data, y_data)


def staff_ids_comparison_graph(lst_dict):
    staff_list = {}
    for i in range(len(lst_dict)):
        if lst_dict[i]['staff_id'] not in staff_list:
            staff_list[lst_dict[i]['staff_id']] = 0
    for i in range(len(lst_dict)):
        staff_list[lst_dict[i]['staff_id']] += int(lst_dict[i]['count\n'])
    x_data = [key for key in staff_list]
    y_data = [staff_list[key] for key in staff_list]
    show_graph('Comparison graph', 'Staff id', 'General count', x_data, y_data)


def resources_comparison_graph(lst_dict):
    resources_list = {}
    for i in range(len(lst_dict)):
        if lst_dict[i]['resource'] not in resources_list:
            resources_list[lst_dict[i]['resource']] = 0
    for i in range(len(lst_dict)):
        resources_list[lst_dict[i]['resource']] += int(lst_dict[i]['count\n'])
    x_data = [key for key in resources_list]
    y_data = [resources_list[key] for key in resources_list]
    show_graph('Comparison graph', 'Resources', 'General count', x_data, y_data)


def main():
    # generate_data_and_write(12, 'file')
    lst = read_file('file')
    lst_dict = from_str_to_dict(lst)
    print(lst_dict)
    # staff_id_graph(23, lst_dict)
    # staff_ids_comparison_graph(lst_dict)


if __name__ == '__main__':
    main()

