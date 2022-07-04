import my_dbase


def get_names_obj_list():
    names = my_dbase.get_all_coin_names()
    names_obj_list = [my_dbase.get_last_update_of_coin(name)
                      for name in names]
    # for name in names:
    #     names_obj_list.append(my_dbase.get_last_update_of_coin(name))
    return names_obj_list
