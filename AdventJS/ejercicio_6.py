class Regalo:
    def in_box(self, box):
        for subarray in box:
            if subarray[0] == '*' or subarray[(len(subarray)-1)] == '*':
                return False
        
        box_plano = [elemento for sublista in box[1:-1] for elemento in sublista]
        if box_plano.count('*') >= 1:
            return True
        else: 
            return False


box = ([
  "###",
  "#*#",
  "###"])
obj = Regalo()
print(obj.in_box(box))
