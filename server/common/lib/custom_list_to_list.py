
def custom_list_to_list(self,custom_list):
    """We define list as "_item_item_item", this function change it to python list.
    
    Args:
        custom_list: custom list we define.

    Returns
        message_list: python list.
    """
    custom_list = custom_list.split('_')
    print custom_list
    del custom_list[0]
    del custom_list[-1]
    message_list = [string.atoi(elem) for elem in custom_list]
    return message_list