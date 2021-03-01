def compare_versions(v1, v2):  
    v1_split_integers = split_version_str_to_int_list(v1)
    v2_split_integers = split_version_str_to_int_list(v2)

    pad_smaller_list_with_zeros(v1_split_integers, v2_split_integers)
    
    for i in range(len(v1_split_integers)):
      if v1_split_integers[i] > v2_split_integers[i]:
         return 1
      elif v2_split_integers[i] > v1_split_integers[i]:
         return -1
    return 0

def split_version_str_to_int_list(version_str):
    return [int(i) for i in version_str.split(".")]

def pad_smaller_list_with_zeros(l1, l2):
    l1_len = len(l1)
    l2_len = len(l2)
    if l1_len > l2_len:
      for _ in range(l2_len, l1_len):
         l2.append(0)
    elif l2_len > l1_len:
      for _ in range(l1_len, l2_len):
         l1.append(0)