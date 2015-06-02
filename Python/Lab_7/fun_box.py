__author__ = 'ilya_rubinshteyn'


def fun_box():
    fucking_awesome = True
    count = 0
    while fucking_awesome:
        count = count + 1
        if count == 1:
            box()
        else:
            break

def box():
    box_list = (
                "\n┏┄┄┄┄┄╥┄┄┄┄┄┓┏┄┄┄┄┄╥┄┄┄┄┄┓"
                "\n╞══╗  ╠══╗  ┊╞══╗  ╠══╗  ┊"
                "\n┊  ║ ╔╬╗ ║  ┊┊  ║ ╔╬╗ ║  ┊"
                "\n╞══╬═╣║╠═╬══╡╞══╬═╣║╠═╬══╡"
                "\n┊  ║ ╚╬╝ ║  ┊┊  ║ ╚╬╝ ║  ┊"
                "\n╞══╝  ╠══╝  ┊╞══╝  ╠══╝  ┊"
                "\n┗┄┄┄┄┄╨┄┄┄┄┄┛┗┄┄┄┄┄╨┄┄┄┄┄┛"

    )
    print(box_list*2)


if __name__ == '__main__':
    fun_box()