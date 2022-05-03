
# python
import turtle
import math
def l_v_t(t, s):  # Draws left vertical top half line
    t.lt(90)
    t.fd(s)
    t.pu()
    t.bk(s)
    t.pd()
    t.rt(90)
def l_v_b(t, s):  # Draws left vertical bottom half line
    t.lt(90)
    t.bk(s)
    t.pu()
    t.fd(s)
    t.pd()
    t.rt(90)
def l_v_f(t, s):  # Draws left vertical full line
    l_v_t(t, s)
    l_v_b(t, s)
def m_v_p(t, s):  # Positions cursor for middle line
    t.pu()
    t.fd(s / 2)
    t.pd()
def m_v_t(t, s):  # Draws middle vertical top half line
    m_v_p(t, s)
    l_v_t(t, s)
    m_v_r(t, s)
def m_v_b(t, s):  # Draws middle vertical bottom half line
    m_v_p(t, s)
    l_v_b(t, s)
    m_v_r(t, s)
def m_v_f(t, s):  # Draws middle vertical full line
    m_v_p(t, s)
    l_v_f(t, s)
    m_v_r(t, s)
def m_v_r(t, s):  # Returns curson from middle line
    t.pu()
    t.bk(s / 2)
    t.pd()
def r_v_p(t, s):  # Positions cursor for left line
    t.pu()
    t.fd(s)
    t.pd()
def r_v_t(t, s):  # Draws right vertical top half line
    r_v_p(t, s)
    l_v_t(t, s)
    r_v_r(t, s)
def r_v_b(t, s):  # Draws right vertical bottom half line
    r_v_p(t, s)
    l_v_b(t, s)
    r_v_r(t, s)
def r_v_f(t, s):  # Draws right vertical full line
    r_v_p(t, s)
    l_v_f(t, s)
    r_v_r(t, s)
def r_v_r(t, s):  # Returns cursor from right line
    t.pu()
    t.bk(s)
    t.pd()
def m_h_l(t, s):  # Draws middle horizontal left half line
    t.fd(s / 2)
    t.pu()
    t.bk(s / 2)
    t.pd()
def m_h_r(t, s):  # Draws middle horizontal right half line
    t.pu()
    t.fd(s / 2)
    t.pd()
    t.fd(s / 2)
    t.pu()
    t.bk(s)
    t.pd()
def m_h_f(t, s):  # Draws middle horizontal full line
    m_h_l(t, s)
    m_h_r(t, s)
def t_h_p(t, s):  # Positions cursor for top line
    t.pu()
    t.lt(90)
    t.fd(s)
    t.pd()
    t.rt(90)
def t_h_l(t, s):  # Draws top horizontal left half line
    t_h_p(t, s)
    m_h_l(t, s)
    t_h_r(t, s)
def t_h_r(t, s):  # Draws top horizontal right half line
    t_h_p(t, s)
    m_h_r(t, s)
    t_h_r(t, s)
def t_h_f(t, s):  # Draws top horizontal full line
    t_h_p(t, s)
    m_h_l(t, s)
    m_h_r(t, s)
    t_h_r(t, s)
def t_h_r(t, s):  # Returns cursor from top line
    t.pu()
    t.lt(90)
    t.bk(s)
    t.pd()
    t.rt(90)
def b_h_p(t, s):  # Positions cursor for bottom line
    t.pu()
    t.lt(90)
    t.bk(s)
    t.pd()
    t.rt(90)
def b_h_l(t, s):  # Draws bottom horizontal left half line
    b_h_p(t, s)
    m_h_l(t, s)
    b_h_r(t, s)
def b_h_r(t, s):  # Draws bottom horizontal right half line
    b_h_p(t, s)
    m_h_r(t, s)
    b_h_r(t, s)
def b_h_f(t, s):  # Draws bottom horizontal full line
    b_h_p(t, s)
    m_h_l(t, s)
    m_h_r(t, s)
    b_h_r(t, s)
def b_h_r(t, s):  # Returns cursor from bottom line
    t.pu()
    t.lt(90)
    t.fd(s)
    t.pd()
    t.rt(90)
def d_d_f(t, s):  # Draws diagonal down full line
    t_h_p(t, s)
    t.rt(94 - math.degrees(math.tan(s / (s * 2))))
    t.fd(math.hypot(s * 2, s))
    t.pu()
    t.bk(math.hypot(s * 2, s))
    t.pd()
    t.lt(94 - math.degrees(math.tan(s / (s * 2))))
    t_h_r(t, s)
def d_u_f(t, s):  # Draws diagonal up full line
    b_h_p(t, s)
    t.lt(94 - math.degrees(math.tan(s / (s * 2))))
    t.fd(math.hypot(s * 2, s))
    t.pu()
    t.bk(math.hypot(s * 2, s))
    t.pd()
    t.rt(94 - math.degrees(math.tan(s / (s * 2))))
    b_h_r(t, s)
def t_l_a(t, s):  # Draws top left accent
    t_h_p(t, s)
    t.bk(s / 10)
    t.pu()
    t.fd(s / 10)
    t.pd()
    t_h_r(t, s)
def b_l_a(t, s):  # Draws bottom left accent
    b_h_p(t, s)
    t.bk(s / 10)
    t.pu()
    t.fd(s / 10)
    t.pd()
    b_h_r(t, s)
def b_r_a(t, s):  # Draws bottom right accent
    b_h_p(t, s)
    t.pu()
    t.fd(s)
    t.fd(s / 10)
    t.pd()
    t.bk(s / 10)
    t.pu()
    t.bk(s)
    t.pd()
    b_h_r(t, s)
def next_char(t, s):
    t.pu()
    t.fd(s * 2)
    t.pd()
def let_a(t, s):  # Draws A
    l_v_f(t, s)
    r_v_f(t, s)
    m_h_f(t, s)
    t_h_f(t, s)
def let_b(t, s):  # Draws B
    l_v_f(t, s)
    r_v_f(t, s)
    m_h_f(t, s)
    t_h_f(t, s)
    b_h_f(t, s)
    t_l_a(t, s)
    b_l_a(t, s)
def let_d(t, s):  # Draws D
    l_v_f(t, s)
    r_v_f(t, s)
    t_h_f(t, s)
    b_h_f(t, s)
    t_l_a(t, s)
    b_l_a(t, s)
def let_e(t, s):  # Draws E
    l_v_f(t, s)
    m_h_f(t, s)
    t_h_f(t, s)
    b_h_f(t, s)
def let_i(t, s):  # Draws I
    m_v_f(t, s)
    t_h_f(t, s)
    b_h_f(t, s)
def let_k(t, s):  # Draws K
    l_v_f(t, s)
    m_v_t(t, s)
    r_v_b(t, s)
    m_h_f(t, s)
def let_m(t, s):  # Draws M
    l_v_f(t, s)
    m_v_t(t, s)
    r_v_f(t, s)
    t_h_f(t, s)
def let_r(t, s):  # Draws R
    l_v_f(t, s)
    m_v_b(t, s)
    r_v_t(t, s)
    m_h_f(t, s)
    t_h_f(t, s)
def let_u(t, s):  # Draws U
    l_v_f(t, s)
    r_v_f(t, s)
    b_h_f(t, s)
    b_r_a(t, s)
def main():
    size= 24
    wn = turtle.Screen()
    wn.setup(1500, size+ 40)
    t = turtle.Turtle()
    t.speed(0)
    name = "Eid Mubarak" # abdeikmru
    turtle.bgcolor("gray")
    t.pencolor("white")
    t.pu()
    t.bk(720)
    t.pd()
    next_char(t, size)
    next_char(t, size)
    for char in name:
        if char.lower() == "a":
            let_a(t, size)
        elif char.lower() == "b":
            let_b(t, size)
        elif char.lower() == "d":
            let_d(t, size)
        elif char.lower() == "e":
            let_e(t, size)
        elif char.lower() == "i":
            let_i(t, size)
        elif char.lower() == "k":
            let_k(t, size)
        elif char.lower() == "m":
            let_m(t, size)
        elif char.lower() == "r":
            let_r(t, size)
        elif char.lower() == "u":
            let_u(t, size)
        next_char(t, size)
    t.color("gray")
    wn.exitonclick()
if __name__ == "__main__":
    main()

