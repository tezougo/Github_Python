# Essa classe abaixo é onde você deve implementar
# seu robô.

# Módulo para avaliação automática do exercício
from gofer import ok

# Módulo que simula o robô de dois elos
from robot2link import Robot

# Provavelmente vamos precisar também do
import numpy as np


class MyRobot(Robot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def pos(self, l1, l2, theta1, theta2):
        self.l1 = l1
        self.l2 = l2
        self.theta1 = theta1
        self.theta2 = theta2

        self.p = np.array([(self.l1 * np.cos(self.theta1) + self.l2 * np.cos(self.theta1 + self.theta2)), \
                      (self.l1 * np.sin(self.theta1) + self.l2 * np.sin(self.theta1 + self.theta2))])
        return self.p

    def cost(self, mx, my):
        self.mx = mx
        self.my = my

        fun_cust = (self.mx - self.l1 * np.cos(self.theta1) - self.l2 * np.cos(self.theta1 + self.theta2)) ** 2 \
                   + (self.my - self.l1 * np.sin(self.theta1) - self.l2 * np.sin(self.theta1 + self.theta2)) ** 2
        return fun_cust

    def grad(self):
        self.result_grad = np.array(
            [(2 * self.mx * (self.l1 * np.sin(self.theta1) + self.l2 * np.sin(self.theta1 + self.theta2)) \
              - 2 * self.my * self.l1 * np.cos(self.theta1) - 2 * self.my * self.l2 * np.cos(
                        self.theta1 + self.theta2)), \
             (2 * self.l2 * (np.sin(self.theta1 + self.theta2) * (self.mx - self.l1 * np.cos(self.theta1))) \
              + np.cos(self.theta1 + self.theta2) * (self.l1 * np.sin(self.theta1) - self.my))])
        return self.result_grad

    def optimize(self, step):
        self.step = step
        self.p = self.p - self.step*self.result_grad

        # xi = np.array([0.5, 3.0])
        # xs = []
        # zs = []
        # for i in range(100):
        #
        #     zi = cost(xi)
        #     xs.append(xi)
        #     zs.append(zi)
        #     xi = optimize(xi)
        return self.p
