#!/usr/bin/python3
if __name__ == "__main__":
    def element_at(my_list, idx):
        if idx < 0 or idx > len(my_list):
            return None
        for i in range(my_list):
            return my_list[idx]
