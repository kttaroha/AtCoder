import math


def main():
    A, B, H, M = map(int, input().split())
    h_theta = 2*math.pi * H / 12 + (2*math.pi / 12) * M /60
    m_theta = 2*math.pi * M / 60
    theta_diff = h_theta - m_theta
    diff = (A**2+B**2-2*A*B*math.cos(theta_diff))**0.5
    print(diff)


if __name__ == '__main__':
    main()
