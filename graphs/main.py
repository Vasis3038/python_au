import matplotlib.pyplot as plt
import operator
from generator import *


def read_file(file_name):
    file = open(file_name)
    result = file.readlines()
    file.close()
    return result


def from_str_to_dict(lst):
    lst = list(map(lambda st: st.split(', '), lst))
    lst_dict = []
    if len(lst[0]) == 4:
        list(map(lambda l: lst_dict.append(dict(zip([lst[0][0], lst[0][1], lst[0][2], lst[0][3].replace('\n', '')], l))), lst))
        for dic in lst_dict:
            dic['staff_id'] = dic['staff_id'].replace('\n', '')
    else:
        list(map(lambda l: lst_dict.append(dict(zip([lst[0][0], lst[0][1], lst[0][2].replace('\n', '')], l))), lst))
        for dic in lst_dict:
            dic['count'] = dic['count'].replace('\n', '')
    lst_dict.pop(0)
    return lst_dict


def show_graph(title, x_lable, y_lable, x_data, y_data):
    plt.plot(x_data, y_data, color='red', marker='o')
    plt.title(title)
    plt.xlabel(x_lable)
    plt.ylabel(y_lable)
    plt.show()


def staff_id_graph(staff_id, lst_dict):
    if "staff_id" in lst_dict[0]:
        lst_dict = list(filter(lambda k: k['staff_id'] == str(staff_id), lst_dict))
        lst_dict.sort(key=operator.itemgetter('date'))
        x_data = [lst_dict[i]['date'] for i in range(len(lst_dict))]
        y_data = [int(lst_dict[i]['count']) for i in range(len(lst_dict))]
        show_graph(f'Staff_id: {staff_id}', 'Date', 'Count', x_data, y_data)
    else:
        return


def resource_graph(resource, lst_dict):
    lst_dict = list(filter(lambda d: d['resource'] == str(resource), lst_dict))
    lst_dict.sort(key=operator.itemgetter('date'))
    x_data = [lst_dict[i]['date'] for i in range(len(lst_dict))]
    y_data = [int(lst_dict[i]['count']) for i in range(len(lst_dict))]
    show_graph(f'Resource: {resource}', 'Date', 'Count', x_data, y_data)


def staff_ids_comparison_graph(lst_dict):
    staff_list = {}
    for i in range(len(lst_dict)):
        if lst_dict[i]['staff_id'] not in staff_list:
            staff_list[lst_dict[i]['staff_id']] = 0
    for i in range(len(lst_dict)):
        staff_list[lst_dict[i]['staff_id']] += int(lst_dict[i]['count'])
    x_data = [key for key in staff_list]
    y_data = [staff_list[key] for key in staff_list]
    show_graph('Comparison graph', 'Staff id', 'General count', x_data, y_data)


def resources_comparison_graph(lst_dict):
    resources_list = {}
    for i in range(len(lst_dict)):
        if lst_dict[i]['resource'] not in resources_list:
            resources_list[lst_dict[i]['resource']] = 0
    for i in range(len(lst_dict)):
        resources_list[lst_dict[i]['resource']] += int(lst_dict[i]['count'])
    x_data = [key for key in resources_list]
    y_data = [resources_list[key] for key in resources_list]
    show_graph('Comparison graph', 'Resources', 'General count', x_data, y_data)


def main():
    generate_data_and_write(12, 'file', 4)
    lst = read_file('file')
    lst_dict = from_str_to_dict(lst)
    print(lst_dict)
    resources_comparison_graph(lst_dict)
    staff_id_graph(2, lst_dict)
    resource_graph(2, lst_dict)
if __name__ == '__main__':
    main()

