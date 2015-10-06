__author__ = 'psinha4'

# O(n) space and time
# see use of extend in this function
def rotate_by_copy(l_to_rotate, i_rotate_by):
    l_rotated_Arr = l_to_rotate[i_rotate_by:len(l_to_rotate)]
    l_rotated_Arr.extend(l_to_rotate[0:i_rotate_by])
    print l_rotated_Arr


# calls bubble i_rotate_by number of times
def rotate_by_bubbling(l_to_rotate, i_rotate_by):
    for i in range(0, i_rotate_by):
        l_to_rotate = bubble(l_to_rotate)
    print l_to_rotate


# shift one element to the left
def bubble(l_original_list):
    i_size = len(l_original_list)
    temp = l_original_list[0]
    for i in range(0, i_size-1):
        l_original_list[i] = l_original_list[i+1]
    l_original_list[i_size-1] = temp
    return l_original_list


# reverse the list starting from i_rotate_from up to i_rotate_upto
def reverse(l_to_reverse, i_rotate_from, i_rotate_upto):
    # midpoint till where loop needs to run
    i_midpoint = int((i_rotate_upto - i_rotate_from)/2)
    # i_count is needed to get the element at the opposite end
    # can't use i when reversing from somewhere in the middle
    i_count = 0
    for i in range(i_rotate_from, i_rotate_from+i_midpoint):
        temp = l_to_reverse[i]
        l_to_reverse[i] = l_to_reverse[i_rotate_upto-1-i_count]
        l_to_reverse[i_rotate_upto-1-i_count] = temp
        i_count += 1
    return l_to_reverse


def rotate_by_reverse(l_original, i_rotate_by):
    l_original = reverse(l_original, 0, i_rotate_by)
    l_original = reverse(l_original, i_rotate_by, len(l_original))
    l_original = reverse(l_original, 0, len(l_original))
    print l_original


if __name__ == '__main__':
    l_to_rotate = [1,2,3,4,5,6,7,8, 9]
    i_rotate_by = 3
    print l_to_rotate
    rotate_by_copy(l_to_rotate, i_rotate_by)
    l_to_rotate = [1,2,3,4,5,6,7,8, 9]
    rotate_by_bubbling(l_to_rotate, i_rotate_by)
    l_to_rotate = [1,2,3,4,5,6,7,8, 9]
    rotate_by_reverse(l_to_rotate, i_rotate_by)