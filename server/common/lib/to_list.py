#Author ChenXionghui
import string
import logging
def custom_list_to_list(custom_list,is_num = True):
    """We define list as "_item_item_item", this function change it to python list.
    
    Args:
        custom_list: custom list we define.
        is_num: change string num to int num if is_num is true.
    Returns
        message_list: python list.
    """
    # logging.info("custom_list is %s"%custom_list)
    custom_list = custom_list.split('_')
    # logging.info("custom_list %s"%custom_list)
    del custom_list[0]
    del custom_list[-1]
    if is_num:
        message_list = [string.atoi(elem) for elem in custom_list]
    else:
        message_list = custom_list
    return message_list